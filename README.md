# 🧠 LogiCore Expert System
### CCS 430: Expert Systems · Maseno University, School of Computing & Informatics

> A complete rule-based expert system for Final Year Project Advisory, built for undergraduate Computer Science students.

---

## 👥 Team

| Admission Number | Name           | Role                                    |
|-----------------|----------------|-----------------------------------------|
| CCS/00057/022   | James Wasonga  | Inference Engine & Backend Architecture |
| CCS/03003/022   | Felix Awere    | Knowledge Base & Rule Engineering       |
| CCS/00055/022   | Amina Michael  | UI/UX Design & Explanation Module       |

---

## 📦 Project Structure

```
logicore/
├── app.py                    ← Flask web application (main entry)
├── requirements.txt          ← Python dependencies
├── README.md                 ← This file
│
├── engine/
│   ├── __init__.py
│   └── inference_engine.py   ← Inference Engine + Forward Chaining + Project Matcher
│
├── knowledge/
│   ├── __init__.py
│   └── knowledge_base.py     ← Knowledge Base: Rules, Facts, Project Topics
│
├── templates/
│   ├── base.html             ← Base layout with navbar/footer
│   ├── index.html            ← Homepage / Landing page
│   ├── consult.html          ← Multi-step consultation form
│   ├── results.html          ← Recommendations + Explanation + Trace
│   ├── knowledge_base.html   ← Browse rules & project categories
│   └── about.html            ← About the system & team
│
└── static/
    ├── css/                  ← (optional extra stylesheets)
    ├── js/                   ← (optional extra scripts)
    └── images/               ← (optional images/logos)
```

---

## 🚀 Setup & Installation

### Step 1: Prerequisites
Make sure you have **Python 3.8+** installed.

```bash
python --version
```

### Step 2: Clone or Copy the Project Folder
Place the entire `logicore/` folder anywhere on your computer.

### Step 3: (Recommended) Create a Virtual Environment

```bash
# Navigate into the project folder
cd logicore

# Create virtual environment
python -m venv venv

# Activate it:
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the Application

```bash
python app.py
```

### Step 6: Open in Browser

Visit: **http://localhost:5000**

---

## 🧩 Expert System Components

### 1. Knowledge Base (`knowledge/knowledge_base.py`)
- **`PROJECT_CATEGORIES`** — 10 CS domains (AI/ML, Web Dev, Blockchain, etc.)
- **`PROJECT_TOPICS`** — 14 specific project templates with metadata
- **`RULES`** — 20+ IF-THEN expert rules covering:
  - GPA-complexity eligibility
  - Time/availability constraints
  - Skill-category matching
  - Career goal alignment
  - Risk tolerance assessment
  - Group dynamics
  - Innovation preferences
- **`FACTS`** — Domain facts (skill levels, career options, etc.)

### 2. Inference Engine (`engine/inference_engine.py`)
- **`WorkingMemory`** — Stores student facts + derived conclusions during a session
- **`InferenceEngine`** — Implements **Forward Chaining**:
  - Iterates all rules against working memory
  - Fires matching rules and asserts new conclusions
  - Repeats until fixpoint (no new rules can fire)
  - Generates full reasoning trace
- **`ProjectMatcher`** — Scores every project topic against inference results
- **`ExpertSystem`** — Main facade combining inference + matching

### 3. Explanation Facility
- Every recommendation shows which rules fired
- Each rule explains WHY it applied in plain language
- Full inference trace is viewable step-by-step

### 4. Web Interface (Flask + HTML/CSS/JS)
- **Homepage** — System overview and architecture diagram
- **Consult** — 5-step guided student profile form
- **Results** — Ranked recommendations with scores, tabs for Explanation, Trace, and Profile
- **Knowledge Base** — Browse all rules and project categories
- **About** — System architecture and team

---

## 📐 Rule Format

Rules follow the standard Expert System IF-THEN format:

```python
{
    "id": "R008",
    "name": "Python Strength → AI/ML or Data Science",
    "conditions": [
        {"attribute": "skills", "operator": "contains", "value": "python"},
        {"attribute": "skill_level_python", "operator": ">=", "value": 3}
    ],
    "conclusion": {"boost_categories": ["AI_ML", "DATA_SCIENCE", "EXPERT_SYSTEM"]},
    "weight": 0.85,
    "explanation": "Your Python proficiency makes you well-suited for AI/ML and Data Science tracks.",
    "type": "skill_match"
}
```

**Supported operators:** `>=`, `<=`, `>`, `<`, `==`, `!=`, `contains`, `contains_any`, `in`

---

## 🔌 API Endpoints

| Method | Endpoint         | Description                          |
|--------|-----------------|--------------------------------------|
| GET    | `/`              | Homepage                             |
| GET    | `/consult`       | Consultation form                    |
| GET    | `/results`       | Results page (reads from sessionStorage) |
| GET    | `/knowledge-base`| Browse knowledge base                |
| GET    | `/about`         | About page                           |
| POST   | `/api/consult`   | Run expert system (JSON API)         |
| GET    | `/api/categories`| Get all project categories           |
| GET    | `/api/rules`     | Get all inference rules              |

### `/api/consult` Request Body Example:
```json
{
  "name": "James Wasonga",
  "admission": "CCS/00057/022",
  "gpa": 3.4,
  "weekly_hours": 25,
  "experience_months": 6,
  "group_size": 3,
  "career_goal": "ml_engineer",
  "skills": ["python", "algorithms", "statistics"],
  "skill_levels": {"python": 4},
  "priorities": ["career_alignment", "innovation"]
}
```

---

## 🛠️ Extending the System

### Adding a New Rule
Open `knowledge/knowledge_base.py` and add to the `RULES` list:
```python
{
    "id": "R021",
    "name": "Your Rule Name",
    "description": "What this rule does",
    "conditions": [
        {"attribute": "gpa", "operator": ">=", "value": 3.0}
    ],
    "conclusion": {"some_derived_fact": "some_value"},
    "weight": 0.8,
    "explanation": "Why this rule fired.",
    "type": "eligibility"  # eligibility | time | skill_match | career | risk | group | preference
}
```

### Adding a New Project Topic
Open `knowledge/knowledge_base.py` and add to `PROJECT_TOPICS`:
```python
"XYZ001": {
    "title": "Your Project Title",
    "category": "AI_ML",  # Must match a key in PROJECT_CATEGORIES
    "complexity": "intermediate",  # beginner | intermediate | advanced | expert
    "duration_weeks": 12,
    "skills": ["python", "algorithms"],
    "tools": ["Python", "Flask"],
    "description": "Short project description.",
    "career_alignment": ["ml_engineer"],
    "risk": "medium",    # low | medium | high
    "novelty": "medium", # low | medium | high
}
```

### Adding a New Category
Add to `PROJECT_CATEGORIES` in the knowledge base file.

---

## 📋 Evaluation Notes

The system satisfies all objectives from the project specification:
- ✅ Expert knowledge acquired and formalized from supervisory experience
- ✅ Structured knowledge base with rules, facts, and categories
- ✅ Inference engine with forward chaining (fixpoint iteration)
- ✅ Explanation module showing rules fired and justifications
- ✅ User-friendly multi-step interface
- ✅ Scoring and ranking of project recommendations

---

*© 2026 — Maseno University, Department of Computer Science*
