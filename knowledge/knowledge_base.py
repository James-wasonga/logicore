"""
LogiCore Expert System - Knowledge Base
Contains all domain knowledge: facts, rules, and project data
"""

# ─────────────────────────────────────────────
# PROJECT CATEGORIES AND DESCRIPTIONS
# ─────────────────────────────────────────────
PROJECT_CATEGORIES = {
    "AI_ML": {
        "name": "Artificial Intelligence & Machine Learning",
        "icon": "🤖",
        "color": "#6C63FF",
        "description": "Projects involving intelligent systems, neural networks, NLP, computer vision, and predictive models.",
        "skills_required": ["python", "math", "statistics", "algorithms"],
        "career_paths": ["data_scientist", "ml_engineer", "researcher", "ai_developer"],
        "min_gpa": 3.0,
        "complexity_levels": ["intermediate", "advanced", "expert"],
    },
    "WEB_DEV": {
        "name": "Web Development",
        "icon": "🌐",
        "color": "#00C9A7",
        "description": "Full-stack web applications, APIs, progressive web apps, and cloud-hosted platforms.",
        "skills_required": ["html_css", "javascript", "databases"],
        "career_paths": ["web_developer", "full_stack", "frontend", "backend", "devops"],
        "min_gpa": 2.0,
        "complexity_levels": ["beginner", "intermediate", "advanced"],
    },
    "MOBILE": {
        "name": "Mobile Application Development",
        "icon": "📱",
        "color": "#FF6B6B",
        "description": "Android, iOS, or cross-platform mobile applications solving real-world problems.",
        "skills_required": ["java_kotlin", "swift_dart", "ui_design"],
        "career_paths": ["mobile_developer", "app_developer", "full_stack"],
        "min_gpa": 2.3,
        "complexity_levels": ["beginner", "intermediate", "advanced"],
    },
    "BLOCKCHAIN": {
        "name": "Blockchain & Web3",
        "icon": "⛓️",
        "color": "#F7931A",
        "description": "Decentralized applications, smart contracts, cryptocurrency systems, and distributed ledgers.",
        "skills_required": ["cryptography", "solidity", "networking", "python"],
        "career_paths": ["blockchain_dev", "fintech", "security_specialist"],
        "min_gpa": 3.2,
        "complexity_levels": ["advanced", "expert"],
    },
    "DATA_SCIENCE": {
        "name": "Data Science & Analytics",
        "icon": "📊",
        "color": "#4ECDC4",
        "description": "Data pipelines, visualization dashboards, statistical analysis, and business intelligence.",
        "skills_required": ["python", "statistics", "databases", "visualization"],
        "career_paths": ["data_analyst", "data_scientist", "business_analyst"],
        "min_gpa": 2.7,
        "complexity_levels": ["intermediate", "advanced"],
    },
    "CYBERSECURITY": {
        "name": "Cybersecurity",
        "icon": "🔒",
        "color": "#E94560",
        "description": "Security auditing tools, intrusion detection, penetration testing frameworks, and encryption systems.",
        "skills_required": ["networking", "cryptography", "linux", "python"],
        "career_paths": ["security_analyst", "penetration_tester", "soc_analyst"],
        "min_gpa": 3.0,
        "complexity_levels": ["intermediate", "advanced", "expert"],
    },
    "IOT": {
        "name": "Internet of Things (IoT)",
        "icon": "📡",
        "color": "#A8E6CF",
        "description": "Smart devices, sensor networks, home automation, and embedded systems with cloud connectivity.",
        "skills_required": ["c_cpp", "networking", "hardware", "python"],
        "career_paths": ["embedded_engineer", "iot_developer", "systems_engineer"],
        "min_gpa": 2.7,
        "complexity_levels": ["intermediate", "advanced"],
    },
    "CLOUD": {
        "name": "Cloud Computing & DevOps",
        "icon": "☁️",
        "color": "#74B9FF",
        "description": "Cloud infrastructure, container orchestration, CI/CD pipelines, and microservices architecture.",
        "skills_required": ["linux", "networking", "scripting", "databases"],
        "career_paths": ["devops", "cloud_architect", "sre", "systems_admin"],
        "min_gpa": 2.5,
        "complexity_levels": ["intermediate", "advanced"],
    },
    "EXPERT_SYSTEM": {
        "name": "Expert Systems & Knowledge Engineering",
        "icon": "🧠",
        "color": "#FDCB6E",
        "description": "Rule-based systems, decision support tools, ontologies, and intelligent advisory applications.",
        "skills_required": ["python", "logic", "algorithms", "databases"],
        "career_paths": ["ai_developer", "knowledge_engineer", "researcher"],
        "min_gpa": 3.0,
        "complexity_levels": ["intermediate", "advanced"],
    },
    "DATABASE": {
        "name": "Database Systems & Engineering",
        "icon": "🗄️",
        "color": "#B2BEC3",
        "description": "Database design, query optimization, distributed databases, and NoSQL solutions.",
        "skills_required": ["sql", "databases", "algorithms"],
        "career_paths": ["dba", "data_engineer", "backend_developer"],
        "min_gpa": 2.3,
        "complexity_levels": ["beginner", "intermediate", "advanced"],
    },
}

# ─────────────────────────────────────────────
# SPECIFIC PROJECT TOPICS
# ─────────────────────────────────────────────
PROJECT_TOPICS = {
    # AI & ML Topics
    "AI001": {
        "title": "Student Performance Prediction System using Machine Learning",
        "category": "AI_ML",
        "complexity": "intermediate",
        "duration_weeks": 12,
        "skills": ["python", "statistics", "algorithms"],
        "tools": ["Python", "Scikit-learn", "Pandas", "Flask"],
        "description": "Predict student academic performance using classification algorithms based on historical data.",
        "career_alignment": ["data_scientist", "ml_engineer"],
        "risk": "medium",
        "novelty": "medium",
    },
    "AI002": {
        "title": "Real-Time Face Recognition Attendance System",
        "category": "AI_ML",
        "complexity": "advanced",
        "duration_weeks": 14,
        "skills": ["python", "math", "algorithms"],
        "tools": ["Python", "OpenCV", "DeepFace", "Flask"],
        "description": "Automate class attendance using facial recognition with real-time detection.",
        "career_alignment": ["ml_engineer", "ai_developer"],
        "risk": "high",
        "novelty": "high",
    },
    "AI003": {
        "title": "Natural Language Processing Chatbot for University FAQs",
        "category": "AI_ML",
        "complexity": "intermediate",
        "duration_weeks": 10,
        "skills": ["python", "algorithms"],
        "tools": ["Python", "NLTK", "TensorFlow", "Flask"],
        "description": "Build an intelligent chatbot that answers common university questions using NLP.",
        "career_alignment": ["ml_engineer", "ai_developer", "web_developer"],
        "risk": "low",
        "novelty": "medium",
    },
    # Web Dev Topics
    "WEB001": {
        "title": "University Course Registration Portal with Smart Scheduling",
        "category": "WEB_DEV",
        "complexity": "intermediate",
        "duration_weeks": 10,
        "skills": ["html_css", "javascript", "databases"],
        "tools": ["React", "Node.js", "PostgreSQL", "Docker"],
        "description": "A full-stack portal for managing course registration with conflict detection.",
        "career_alignment": ["web_developer", "full_stack", "backend"],
        "risk": "low",
        "novelty": "medium",
    },
    "WEB002": {
        "title": "E-Learning Platform with Video Conferencing Integration",
        "category": "WEB_DEV",
        "complexity": "advanced",
        "duration_weeks": 14,
        "skills": ["html_css", "javascript", "databases", "networking"],
        "tools": ["React", "Node.js", "WebRTC", "MongoDB"],
        "description": "Build a full-featured e-learning platform with live sessions and course management.",
        "career_alignment": ["full_stack", "web_developer"],
        "risk": "high",
        "novelty": "high",
    },
    # Mobile Topics
    "MOB001": {
        "title": "Campus Navigation App with AR Overlays",
        "category": "MOBILE",
        "complexity": "advanced",
        "duration_weeks": 14,
        "skills": ["java_kotlin", "ui_design"],
        "tools": ["Flutter", "Firebase", "Google Maps API", "ARCore"],
        "description": "Help students navigate campus with augmented reality directions.",
        "career_alignment": ["mobile_developer", "app_developer"],
        "risk": "high",
        "novelty": "high",
    },
    "MOB002": {
        "title": "Student Mental Health Tracker and Wellness App",
        "category": "MOBILE",
        "complexity": "intermediate",
        "duration_weeks": 10,
        "skills": ["swift_dart", "ui_design"],
        "tools": ["Flutter", "Firebase", "Dart"],
        "description": "An app for tracking mental health metrics and recommending wellness activities.",
        "career_alignment": ["mobile_developer", "full_stack"],
        "risk": "low",
        "novelty": "high",
    },
    # Blockchain Topics
    "BC001": {
        "title": "Blockchain-Based Academic Certificate Verification",
        "category": "BLOCKCHAIN",
        "complexity": "advanced",
        "duration_weeks": 14,
        "skills": ["cryptography", "solidity", "python"],
        "tools": ["Ethereum", "Solidity", "Web3.js", "IPFS"],
        "description": "Prevent certificate fraud using immutable blockchain-based credential records.",
        "career_alignment": ["blockchain_dev", "security_specialist", "fintech"],
        "risk": "high",
        "novelty": "high",
    },
    # Data Science Topics
    "DS001": {
        "title": "COVID-19 Data Visualization and Trend Analysis Dashboard",
        "category": "DATA_SCIENCE",
        "complexity": "intermediate",
        "duration_weeks": 8,
        "skills": ["python", "statistics", "visualization"],
        "tools": ["Python", "Plotly", "Dash", "Pandas"],
        "description": "Interactive dashboard visualizing COVID-19 trends with predictive modeling.",
        "career_alignment": ["data_analyst", "data_scientist"],
        "risk": "low",
        "novelty": "medium",
    },
    "DS002": {
        "title": "Agricultural Yield Prediction Using Satellite Data",
        "category": "DATA_SCIENCE",
        "complexity": "advanced",
        "duration_weeks": 14,
        "skills": ["python", "statistics", "algorithms", "math"],
        "tools": ["Python", "Google Earth Engine", "TensorFlow", "GeoPandas"],
        "description": "Predict crop yields for Kenyan farmers using satellite imagery and ML.",
        "career_alignment": ["data_scientist", "researcher"],
        "risk": "high",
        "novelty": "high",
    },
    # Cybersecurity
    "SEC001": {
        "title": "Network Intrusion Detection System using Machine Learning",
        "category": "CYBERSECURITY",
        "complexity": "advanced",
        "duration_weeks": 12,
        "skills": ["networking", "python", "algorithms", "linux"],
        "tools": ["Python", "Scapy", "Scikit-learn", "Wireshark"],
        "description": "Detect network intrusions in real-time using anomaly detection algorithms.",
        "career_alignment": ["security_analyst", "penetration_tester"],
        "risk": "high",
        "novelty": "medium",
    },
    # IoT Topics
    "IOT001": {
        "title": "Smart Campus Energy Management System",
        "category": "IOT",
        "complexity": "advanced",
        "duration_weeks": 12,
        "skills": ["c_cpp", "networking", "python", "hardware"],
        "tools": ["Arduino", "Raspberry Pi", "MQTT", "Node-RED"],
        "description": "Monitor and optimize energy usage across campus buildings using IoT sensors.",
        "career_alignment": ["embedded_engineer", "iot_developer"],
        "risk": "high",
        "novelty": "high",
    },
    # Expert System Topics
    "ES001": {
        "title": "Medical Diagnosis Expert System for Common Diseases",
        "category": "EXPERT_SYSTEM",
        "complexity": "intermediate",
        "duration_weeks": 10,
        "skills": ["python", "logic", "algorithms"],
        "tools": ["Python", "Flask", "SQLite", "Prolog"],
        "description": "Rule-based system that diagnoses common diseases from symptoms.",
        "career_alignment": ["ai_developer", "researcher", "knowledge_engineer"],
        "risk": "medium",
        "novelty": "medium",
    },
    # Database Topics
    "DB001": {
        "title": "Hospital Management System with Advanced Reporting",
        "category": "DATABASE",
        "complexity": "intermediate",
        "duration_weeks": 10,
        "skills": ["sql", "databases", "html_css", "javascript"],
        "tools": ["Python", "PostgreSQL", "Flask", "Bootstrap"],
        "description": "Comprehensive hospital management system with patient records and analytics.",
        "career_alignment": ["backend_developer", "dba", "full_stack"],
        "risk": "low",
        "novelty": "low",
    },
    # Cloud Topics
    "CLD001": {
        "title": "Serverless File Sharing Platform with End-to-End Encryption",
        "category": "CLOUD",
        "complexity": "advanced",
        "duration_weeks": 12,
        "skills": ["networking", "scripting", "linux", "cryptography"],
        "tools": ["AWS Lambda", "S3", "Python", "React"],
        "description": "Cloud-native file sharing with zero-knowledge encryption architecture.",
        "career_alignment": ["cloud_architect", "devops", "sre"],
        "risk": "high",
        "novelty": "high",
    },
}

# ─────────────────────────────────────────────
# INFERENCE RULES - The Heart of the Expert System
# ─────────────────────────────────────────────
# Rules follow IF-THEN format
# Each rule has: id, conditions (list of checks), conclusion, weight, explanation

RULES = [
    # ── GPA-Based Complexity Rules ──
    {
        "id": "R001",
        "name": "GPA-Complexity Alignment",
        "description": "Project complexity must match student's academic performance",
        "conditions": [
            {"attribute": "gpa", "operator": ">=", "value": 3.5}
        ],
        "conclusion": {"allow_complexity": ["beginner", "intermediate", "advanced", "expert"]},
        "weight": 1.0,
        "explanation": "Your GPA of {gpa} qualifies you for projects of any complexity level.",
        "type": "eligibility"
    },
    {
        "id": "R002",
        "name": "High GPA Rule",
        "description": "Students with GPA 3.0-3.49 can handle up to advanced",
        "conditions": [
            {"attribute": "gpa", "operator": ">=", "value": 3.0},
            {"attribute": "gpa", "operator": "<", "value": 3.5}
        ],
        "conclusion": {"allow_complexity": ["beginner", "intermediate", "advanced"]},
        "weight": 1.0,
        "explanation": "Your GPA of {gpa} qualifies you for beginner to advanced projects.",
        "type": "eligibility"
    },
    {
        "id": "R003",
        "name": "Average GPA Rule",
        "description": "Students with GPA 2.5-2.99 handle up to intermediate",
        "conditions": [
            {"attribute": "gpa", "operator": ">=", "value": 2.5},
            {"attribute": "gpa", "operator": "<", "value": 3.0}
        ],
        "conclusion": {"allow_complexity": ["beginner", "intermediate"]},
        "weight": 1.0,
        "explanation": "Your GPA of {gpa} is best suited for beginner to intermediate complexity projects.",
        "type": "eligibility"
    },
    {
        "id": "R004",
        "name": "Low GPA Rule",
        "description": "Students with GPA below 2.5 should choose beginner projects",
        "conditions": [
            {"attribute": "gpa", "operator": "<", "value": 2.5}
        ],
        "conclusion": {"allow_complexity": ["beginner"]},
        "weight": 1.0,
        "explanation": "Given your GPA of {gpa}, beginner-level projects are recommended to ensure project success.",
        "type": "eligibility"
    },

    # ── Time Availability Rules ──
    {
        "id": "R005",
        "name": "Full-Time Availability",
        "description": "Students with full time availability can tackle longer projects",
        "conditions": [
            {"attribute": "weekly_hours", "operator": ">=", "value": 30}
        ],
        "conclusion": {"max_duration_weeks": 16, "time_tier": "full"},
        "weight": 0.9,
        "explanation": "With {weekly_hours} hours/week available, you can manage long-duration projects.",
        "type": "time"
    },
    {
        "id": "R006",
        "name": "Part-Time Availability",
        "description": "Students with moderate time should avoid very long projects",
        "conditions": [
            {"attribute": "weekly_hours", "operator": ">=", "value": 15},
            {"attribute": "weekly_hours", "operator": "<", "value": 30}
        ],
        "conclusion": {"max_duration_weeks": 12, "time_tier": "moderate"},
        "weight": 0.9,
        "explanation": "With {weekly_hours} hours/week, projects up to 12 weeks are manageable.",
        "type": "time"
    },
    {
        "id": "R007",
        "name": "Limited Time Rule",
        "description": "Students with very limited time should choose short projects",
        "conditions": [
            {"attribute": "weekly_hours", "operator": "<", "value": 15}
        ],
        "conclusion": {"max_duration_weeks": 10, "time_tier": "limited"},
        "weight": 0.9,
        "explanation": "With only {weekly_hours} hours/week, focus on projects completable within 10 weeks.",
        "type": "time"
    },

    # ── Skill-Category Matching Rules ──
    {
        "id": "R008",
        "name": "Python Strength → AI/ML or Data Science",
        "description": "Strong Python skills align with AI/ML and data science projects",
        "conditions": [
            {"attribute": "skills", "operator": "contains", "value": "python"},
            {"attribute": "skill_level_python", "operator": ">=", "value": 3}
        ],
        "conclusion": {"boost_categories": ["AI_ML", "DATA_SCIENCE", "EXPERT_SYSTEM"]},
        "weight": 0.85,
        "explanation": "Your Python proficiency makes you well-suited for AI/ML and Data Science tracks.",
        "type": "skill_match"
    },
    {
        "id": "R009",
        "name": "Web Skills → Web Development",
        "description": "HTML/CSS/JS skills align with web development projects",
        "conditions": [
            {"attribute": "skills", "operator": "contains", "value": "html_css"},
            {"attribute": "skills", "operator": "contains", "value": "javascript"}
        ],
        "conclusion": {"boost_categories": ["WEB_DEV", "DATABASE"]},
        "weight": 0.85,
        "explanation": "Your web development skills are a strong fit for web and database-driven projects.",
        "type": "skill_match"
    },
    {
        "id": "R010",
        "name": "Networking + Cryptography → Security",
        "description": "Networking and crypto skills align with cybersecurity projects",
        "conditions": [
            {"attribute": "skills", "operator": "contains", "value": "networking"},
            {"attribute": "skills", "operator": "contains", "value": "cryptography"}
        ],
        "conclusion": {"boost_categories": ["CYBERSECURITY", "BLOCKCHAIN", "CLOUD"]},
        "weight": 0.9,
        "explanation": "Your networking and cryptography skills are ideal for security and blockchain projects.",
        "type": "skill_match"
    },
    {
        "id": "R011",
        "name": "Hardware + Embedded → IoT",
        "description": "Hardware and C/C++ skills align with IoT projects",
        "conditions": [
            {"attribute": "skills", "operator": "contains", "value": "hardware"},
            {"attribute": "skills", "operator": "contains", "value": "c_cpp"}
        ],
        "conclusion": {"boost_categories": ["IOT"]},
        "weight": 0.9,
        "explanation": "Your hardware and embedded programming skills make IoT projects a natural choice.",
        "type": "skill_match"
    },
    {
        "id": "R012",
        "name": "Mobile Skills → Mobile Development",
        "description": "Mobile-specific skills align with mobile app projects",
        "conditions": [
            {"attribute": "skills", "operator": "contains_any", "value": ["java_kotlin", "swift_dart"]}
        ],
        "conclusion": {"boost_categories": ["MOBILE"]},
        "weight": 0.85,
        "explanation": "Your mobile development skills are a direct match for mobile application projects.",
        "type": "skill_match"
    },

    # ── Career Alignment Rules ──
    {
        "id": "R013",
        "name": "Career → Category Alignment",
        "description": "Career goals determine which project categories to recommend",
        "conditions": [
            {"attribute": "career_goal", "operator": "in", "value": ["data_scientist", "ml_engineer", "researcher"]}
        ],
        "conclusion": {"preferred_categories": ["AI_ML", "DATA_SCIENCE", "EXPERT_SYSTEM"]},
        "weight": 1.0,
        "explanation": "Your career goal aligns with AI, ML, and data-centric projects.",
        "type": "career"
    },
    {
        "id": "R014",
        "name": "Security Career Alignment",
        "description": "Security career goals align with security/blockchain projects",
        "conditions": [
            {"attribute": "career_goal", "operator": "in", "value": ["security_analyst", "penetration_tester", "soc_analyst"]}
        ],
        "conclusion": {"preferred_categories": ["CYBERSECURITY", "BLOCKCHAIN"]},
        "weight": 1.0,
        "explanation": "Your security career goals align with cybersecurity and blockchain projects.",
        "type": "career"
    },
    {
        "id": "R015",
        "name": "Web/Full-Stack Career Alignment",
        "description": "Web career goals align with web/mobile projects",
        "conditions": [
            {"attribute": "career_goal", "operator": "in", "value": ["web_developer", "full_stack", "frontend", "backend"]}
        ],
        "conclusion": {"preferred_categories": ["WEB_DEV", "MOBILE", "DATABASE"]},
        "weight": 1.0,
        "explanation": "Your web/full-stack career goals are best served by web, mobile, or database projects.",
        "type": "career"
    },
    {
        "id": "R016",
        "name": "DevOps Career Alignment",
        "description": "DevOps career goals align with cloud/IoT projects",
        "conditions": [
            {"attribute": "career_goal", "operator": "in", "value": ["devops", "cloud_architect", "sre", "systems_admin"]}
        ],
        "conclusion": {"preferred_categories": ["CLOUD", "IOT"]},
        "weight": 1.0,
        "explanation": "Cloud and infrastructure projects directly align with your DevOps career path.",
        "type": "career"
    },

    # ── Risk Assessment Rules ──
    {
        "id": "R017",
        "name": "Risk Tolerance - High",
        "description": "Experienced students can accept higher-risk, innovative projects",
        "conditions": [
            {"attribute": "gpa", "operator": ">=", "value": 3.3},
            {"attribute": "weekly_hours", "operator": ">=", "value": 20},
            {"attribute": "experience_months", "operator": ">=", "value": 6}
        ],
        "conclusion": {"allow_risk": ["low", "medium", "high"]},
        "weight": 0.8,
        "explanation": "Your profile supports taking on higher-risk, innovative project ideas.",
        "type": "risk"
    },
    {
        "id": "R018",
        "name": "Risk Tolerance - Low",
        "description": "Students with limited experience should avoid high-risk projects",
        "conditions": [
            {"attribute": "experience_months", "operator": "<", "value": 3}
        ],
        "conclusion": {"allow_risk": ["low", "medium"]},
        "weight": 0.8,
        "explanation": "With limited prior experience, medium and low-risk projects are recommended.",
        "type": "risk"
    },
    {
        "id": "R019",
        "name": "Group Size - Solo Risk Cap",
        "description": "Solo students should avoid expert-level projects",
        "conditions": [
            {"attribute": "group_size", "operator": "==", "value": 1},
            {"attribute": "gpa", "operator": "<", "value": 3.5}
        ],
        "conclusion": {"exclude_complexity": ["expert"]},
        "weight": 0.7,
        "explanation": "Solo projects at expert complexity are very challenging without a GPA above 3.5.",
        "type": "group"
    },
    {
        "id": "R020",
        "name": "Innovation Bonus",
        "description": "Students seeking innovation should get higher novelty projects",
        "conditions": [
            {"attribute": "priority", "operator": "contains", "value": "innovation"}
        ],
        "conclusion": {"prefer_novelty": "high"},
        "weight": 0.75,
        "explanation": "Your interest in innovation is matched to high-novelty, cutting-edge project topics.",
        "type": "preference"
    },
]

# ─────────────────────────────────────────────
# FACTS - Initial World Knowledge
# ─────────────────────────────────────────────
FACTS = {
    "skill_levels": {1: "Beginner", 2: "Elementary", 3: "Intermediate", 4: "Advanced", 5: "Expert"},
    "complexity_order": ["beginner", "intermediate", "advanced", "expert"],
    "career_options": {
        "data_scientist": "Data Scientist",
        "ml_engineer": "Machine Learning Engineer",
        "researcher": "Research Scientist",
        "web_developer": "Web Developer",
        "full_stack": "Full-Stack Developer",
        "frontend": "Frontend Developer",
        "backend": "Backend Developer",
        "mobile_developer": "Mobile App Developer",
        "app_developer": "App Developer",
        "blockchain_dev": "Blockchain Developer",
        "fintech": "FinTech Developer",
        "security_analyst": "Security Analyst",
        "penetration_tester": "Penetration Tester",
        "soc_analyst": "SOC Analyst",
        "data_analyst": "Data Analyst",
        "business_analyst": "Business Analyst",
        "devops": "DevOps Engineer",
        "cloud_architect": "Cloud Architect",
        "sre": "Site Reliability Engineer",
        "systems_admin": "Systems Administrator",
        "embedded_engineer": "Embedded Systems Engineer",
        "iot_developer": "IoT Developer",
        "systems_engineer": "Systems Engineer",
        "dba": "Database Administrator",
        "data_engineer": "Data Engineer",
        "ai_developer": "AI Developer",
        "knowledge_engineer": "Knowledge Engineer",
    },
    "skill_options": {
        "python": "Python Programming",
        "javascript": "JavaScript",
        "java_kotlin": "Java / Kotlin (Android)",
        "swift_dart": "Swift / Dart (Flutter)",
        "c_cpp": "C / C++",
        "html_css": "HTML & CSS",
        "sql": "SQL & Relational Databases",
        "databases": "Database Management",
        "networking": "Computer Networking",
        "cryptography": "Cryptography & Security",
        "algorithms": "Data Structures & Algorithms",
        "math": "Mathematics & Linear Algebra",
        "statistics": "Statistics & Probability",
        "linux": "Linux / Unix Systems",
        "scripting": "Shell / Bash Scripting",
        "hardware": "Hardware & Electronics",
        "ui_design": "UI/UX Design",
        "visualization": "Data Visualization",
        "solidity": "Solidity (Blockchain)",
        "logic": "Formal Logic & Reasoning",
    },
    "priority_options": {
        "career_alignment": "Career Alignment",
        "innovation": "Innovation & Novelty",
        "feasibility": "Feasibility & Low Risk",
        "academic_depth": "Academic Depth",
        "social_impact": "Social Impact",
    }
}
