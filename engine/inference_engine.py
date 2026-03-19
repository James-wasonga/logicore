"""
LogiCore Expert System - Inference Engine
Implements Forward Chaining to derive conclusions from student facts and rules.
"""

from knowledge.knowledge_base import RULES, PROJECT_TOPICS, PROJECT_CATEGORIES, FACTS


class WorkingMemory:
    """Stores asserted facts during a reasoning session"""
    def __init__(self, student_data: dict):
        self.facts = dict(student_data)
        self.derived_facts = {}
        self.fired_rules = []
        self.agenda = []  # Rules waiting to fire

    def assert_fact(self, key, value):
        self.derived_facts[key] = value

    def get(self, key, default=None):
        return self.facts.get(key, self.derived_facts.get(key, default))

    def get_all(self):
        combined = dict(self.facts)
        combined.update(self.derived_facts)
        return combined


class InferenceEngine:
    """
    Forward Chaining Inference Engine
    - Iterates through all rules
    - Evaluates conditions against working memory
    - Fires matching rules and asserts conclusions
    - Repeats until no new rules can fire (fixpoint)
    """

    def __init__(self):
        self.rules = RULES
        self.trace = []  # Explanation trace

    def evaluate_condition(self, condition: dict, memory: WorkingMemory) -> bool:
        """Evaluate a single condition against working memory"""
        attr = condition["attribute"]
        op = condition["operator"]
        val = condition["value"]

        fact_value = memory.get(attr)
        if fact_value is None:
            return False

        if op == ">=":
            return float(fact_value) >= float(val)
        elif op == "<=":
            return float(fact_value) <= float(val)
        elif op == ">":
            return float(fact_value) > float(val)
        elif op == "<":
            return float(fact_value) < float(val)
        elif op == "==":
            return fact_value == val
        elif op == "!=":
            return fact_value != val
        elif op == "contains":
            if isinstance(fact_value, list):
                return val in fact_value
            return val in str(fact_value)
        elif op == "contains_any":
            if isinstance(fact_value, list):
                return any(v in fact_value for v in val)
            return False
        elif op == "in":
            return fact_value in val
        return False

    def evaluate_rule(self, rule: dict, memory: WorkingMemory) -> bool:
        """Check if ALL conditions of a rule are satisfied"""
        return all(self.evaluate_condition(c, memory) for c in rule["conditions"])

    def format_explanation(self, rule: dict, memory: WorkingMemory) -> str:
        """Format rule explanation with actual values"""
        explanation = rule.get("explanation", rule["description"])
        try:
            explanation = explanation.format(**memory.get_all())
        except (KeyError, ValueError):
            pass
        return explanation

    def run(self, student_data: dict) -> dict:
        """
        Execute forward chaining inference.
        Returns: dict with fired rules, derived conclusions, and trace.
        """
        memory = WorkingMemory(student_data)
        fired = set()
        changed = True
        iteration = 0
        max_iterations = 50  # safety cap

        self.trace = []
        self.trace.append({
            "step": "INITIALIZATION",
            "message": "Working memory initialized with student profile.",
            "facts": dict(student_data)
        })

        while changed and iteration < max_iterations:
            changed = False
            iteration += 1

            for rule in self.rules:
                rule_id = rule["id"]
                if rule_id in fired:
                    continue

                if self.evaluate_rule(rule, memory):
                    # Fire the rule
                    fired.add(rule_id)
                    changed = True

                    # Assert each conclusion into working memory
                    for key, value in rule["conclusion"].items():
                        existing = memory.derived_facts.get(key)
                        if isinstance(existing, list) and isinstance(value, list):
                            # Merge lists (e.g., boost_categories accumulates)
                            memory.assert_fact(key, list(set(existing + value)))
                        else:
                            memory.assert_fact(key, value)

                    explanation = self.format_explanation(rule, memory)
                    self.trace.append({
                        "step": f"RULE FIRED: {rule_id}",
                        "rule_name": rule["name"],
                        "rule_type": rule.get("type", "general"),
                        "message": explanation,
                        "weight": rule["weight"],
                        "conclusion": rule["conclusion"]
                    })
                    memory.fired_rules.append({
                        "id": rule_id,
                        "name": rule["name"],
                        "type": rule.get("type", "general"),
                        "explanation": explanation,
                        "weight": rule["weight"]
                    })

        self.trace.append({
            "step": "COMPLETION",
            "message": f"Forward chaining complete after {iteration} iteration(s). {len(fired)} rules fired.",
            "fired_count": len(fired)
        })

        return {
            "working_memory": memory.get_all(),
            "fired_rules": memory.fired_rules,
            "derived_facts": memory.derived_facts,
            "trace": self.trace
        }


class ProjectMatcher:
    """
    Matches projects to student profiles based on inference results
    and computes a match score for ranking.
    """

    def score_project(self, topic_id: str, topic: dict, inference_result: dict) -> dict:
        """Compute a compatibility score for a project given inference results"""
        wm = inference_result["working_memory"]
        derived = inference_result["derived_facts"]
        student_skills = wm.get("skills", [])
        career_goal = wm.get("career_goal", "")
        priorities = wm.get("priorities", [])

        score = 0.0
        reasons = []
        warnings = []

        # ── Complexity Check ──
        allowed_complexity = derived.get("allow_complexity", ["beginner", "intermediate", "advanced", "expert"])
        excluded_complexity = derived.get("exclude_complexity", [])
        project_complexity = topic.get("complexity", "intermediate")

        if project_complexity in excluded_complexity:
            return None  # Hard exclude
        if project_complexity in allowed_complexity:
            score += 25
            reasons.append(f"Complexity level ({project_complexity}) matches your academic profile.")
        else:
            warnings.append(f"This project's {project_complexity} complexity may be challenging given your GPA.")

        # ── Time/Duration Check ──
        max_weeks = derived.get("max_duration_weeks", 16)
        if topic["duration_weeks"] <= max_weeks:
            score += 15
            reasons.append(f"Duration of {topic['duration_weeks']} weeks fits your availability.")
        else:
            warnings.append(f"This project ({topic['duration_weeks']} weeks) may exceed your available time.")
            score -= 10

        # ── Category Boosting ──
        boosted_categories = derived.get("boost_categories", [])
        preferred_categories = derived.get("preferred_categories", [])
        topic_category = topic["category"]

        if topic_category in preferred_categories:
            score += 30
            reasons.append(f"Category ({PROJECT_CATEGORIES[topic_category]['name']}) aligns with your career goals.")
        if topic_category in boosted_categories:
            score += 20
            reasons.append(f"Your technical skills are a strong match for {PROJECT_CATEGORIES[topic_category]['name']}.")

        # ── Skill Overlap ──
        topic_skills = set(topic.get("skills", []))
        student_skill_set = set(student_skills)
        overlap = topic_skills & student_skill_set
        if topic_skills:
            skill_ratio = len(overlap) / len(topic_skills)
            score += skill_ratio * 25
            if skill_ratio >= 0.8:
                reasons.append(f"Excellent skill match: you have {int(skill_ratio*100)}% of required skills.")
            elif skill_ratio >= 0.5:
                reasons.append(f"Good skill overlap: {int(skill_ratio*100)}% of required skills covered.")
            else:
                missing = topic_skills - student_skill_set
                warnings.append(f"Missing skills: {', '.join(list(missing)[:3])}.")

        # ── Career Alignment ──
        if career_goal in topic.get("career_alignment", []):
            score += 20
            reasons.append("Directly aligned with your chosen career path.")

        # ── Risk Check ──
        allowed_risk = derived.get("allow_risk", ["low", "medium", "high"])
        project_risk = topic.get("risk", "medium")
        if project_risk in allowed_risk:
            score += 5
        else:
            warnings.append("This project carries higher risk than recommended for your profile.")
            score -= 5

        # ── Novelty Preference ──
        preferred_novelty = derived.get("prefer_novelty", None)
        if preferred_novelty == "high" and topic.get("novelty") == "high":
            score += 10
            reasons.append("High-novelty project matches your innovation preference.")
        elif "feasibility" in priorities and topic.get("risk") == "low":
            score += 8
            reasons.append("Low-risk project matches your feasibility preference.")

        return {
            "topic_id": topic_id,
            "title": topic["title"],
            "category": topic_category,
            "category_name": PROJECT_CATEGORIES[topic_category]["name"],
            "category_icon": PROJECT_CATEGORIES[topic_category]["icon"],
            "category_color": PROJECT_CATEGORIES[topic_category]["color"],
            "complexity": topic["complexity"],
            "duration_weeks": topic["duration_weeks"],
            "tools": topic["tools"],
            "description": topic["description"],
            "score": round(min(score, 100), 1),
            "reasons": reasons,
            "warnings": warnings,
            "risk": topic.get("risk", "medium"),
            "novelty": topic.get("novelty", "medium"),
            "career_alignment": topic.get("career_alignment", []),
        }

    def get_recommendations(self, inference_result: dict, top_n: int = 5) -> list:
        """Return top-N ranked project recommendations"""
        results = []
        for topic_id, topic in PROJECT_TOPICS.items():
            scored = self.score_project(topic_id, topic, inference_result)
            if scored is not None:
                results.append(scored)

        # Sort by score descending
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:top_n]


class ExpertSystem:
    """
    Main facade for the LogiCore Expert System
    Combines inference engine + project matcher
    """

    def __init__(self):
        self.engine = InferenceEngine()
        self.matcher = ProjectMatcher()

    def consult(self, student_data: dict) -> dict:
        """
        Full consultation pipeline:
        1. Run inference engine
        2. Match projects
        3. Return structured results
        """
        # Add derived skill level facts for rules that need them
        for skill in student_data.get("skills", []):
            student_data[f"skill_level_{skill}"] = student_data.get("skill_levels", {}).get(skill, 3)

        # Run forward chaining
        inference_result = self.engine.run(student_data)

        # Get recommendations
        recommendations = self.matcher.get_recommendations(inference_result, top_n=6)

        # Build explanation summary
        rule_summary = self._build_rule_summary(inference_result["fired_rules"])

        return {
            "student": student_data,
            "recommendations": recommendations,
            "inference_trace": inference_result["trace"],
            "fired_rules": inference_result["fired_rules"],
            "rule_summary": rule_summary,
            "derived_facts": inference_result["derived_facts"],
            "total_rules_fired": len(inference_result["fired_rules"]),
        }

    def _build_rule_summary(self, fired_rules: list) -> dict:
        """Organize fired rules by type for the explanation module"""
        summary = {}
        for rule in fired_rules:
            rtype = rule.get("type", "general")
            if rtype not in summary:
                summary[rtype] = []
            summary[rtype].append(rule)
        return summary
