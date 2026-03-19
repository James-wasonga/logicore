"""
LogiCore Expert System - Flask Application
Main web server and API routes
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from engine.inference_engine import ExpertSystem
from knowledge.knowledge_base import FACTS, PROJECT_CATEGORIES

app = Flask(__name__)
app.secret_key = "logicore_expert_system_2026_maseno"
CORS(app)

expert_system = ExpertSystem()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/consult")
def consult():
    return render_template("consult.html",
                           skills=FACTS["skill_options"],
                           careers=FACTS["career_options"],
                           priorities=FACTS["priority_options"])


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/knowledge-base")
def knowledge_base_view():
    return render_template("knowledge_base.html",
                           categories=PROJECT_CATEGORIES)


@app.route("/api/consult", methods=["POST"])
def api_consult():
    try:
        data = request.get_json()

        # Build student profile
        student_data = {
            "name": data.get("name", "Student"),
            "admission": data.get("admission", ""),
            "gpa": float(data.get("gpa", 2.5)),
            "weekly_hours": int(data.get("weekly_hours", 20)),
            "experience_months": int(data.get("experience_months", 0)),
            "group_size": int(data.get("group_size", 1)),
            "career_goal": data.get("career_goal", ""),
            "skills": data.get("skills", []),
            "skill_levels": data.get("skill_levels", {}),
            "priorities": data.get("priorities", []),
            "interests": data.get("interests", []),
        }

        # Run expert system
        result = expert_system.consult(student_data)

        return jsonify({"success": True, "result": result})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/categories")
def api_categories():
    return jsonify(PROJECT_CATEGORIES)


@app.route("/api/rules")
def api_rules():
    from knowledge.knowledge_base import RULES
    return jsonify(RULES)


@app.route("/results")
def results():
    return render_template("results.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0" port=int(os.environ.get("PORT", 5000)))
