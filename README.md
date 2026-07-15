# ALPA - AI Learning Progress Assistant

ALPA (AI Learning Progress Assistant) is a personal learning and project management assistant built to help track learning progress, manage projects, organize goals, and generate insights based on daily activities.

The main purpose of ALPA is to help learners stay consistent, understand their progress, and decide what to focus on next.

---

# 🚀 ALPA v1.0

ALPA v1.0 is a CLI-based productivity system built with Python and SQLite.

The system combines:

- Learning activity tracking
- Project management
- Goal tracking
- Progress analytics
- Smart project recommendation
- Personal dashboard overview

---

# ✨ Features

## 1. Learning Activity Tracker

Track daily learning activities:

- Activity name
- Category
- Duration
- Notes
- Self-rating

Example:

Activity:
Learn FastAPI

Category:
Programming

Duration:
60 minutes

## 2. Activity Report & Insight Engine

Generate learning reports based on recorded activities.

Provides:

- Total learning sessions
- Total learning time
- Most active learning category
- Activity breakdown
- Learning recommendations

Example output:

========== LEARNING REPORT ==========

Total Learning Sessions: 5
Total Learning Time: 300 minutes
Most Active Category: Programming

====================================

# 3. Project Tracker

Manage personal and development projects.

Features:

- Create projects
- View projects
- Update progress
- Track next action
- Set priority

Project information:

- Name
- Description
- Status
- Progress percentage
- Next action
- Priority level



# 4. Project Analytics

Analyze project development progress.

Tracks:

- Total progress gain
- Number of updates
- Average growth

Example:

========== PROJECT ANALYTICS ==========

Total Progress Gain: +30%
Total Updates: 2
Average Growth: 15%

=======================================

# 5. Project History Tracking

Every project progress update is recorded.

Example:

Project ID: 11

Progress:
60% -> 80%

Changed At:
2026-07-13

# 6. Smart Project Recommendation Engine

ALPA analyzes active projects and recommends the most important project to focus on.

The decision is based on:

- Project priority
- Current progress
- Defined next action
- Project status

Example:

========== SMART RECOMMENDATION ==========

Project:
Priority Test

Decision Score:
185

Why selected:
✓ High priority project
✓ Has defined next action

Next Action:
Important Task

==========================================

# 7. Goal Management

Track important personal goals.

Features:

- Create goals
- View goals
- Manage status
- Set deadlines

Example:

Goal:
Join Gamuda AI Academy

Deadline:
31/7/2026

Status:
Active

# 8. Goal & Project Relationship

Connect goals with related projects.

Example:

Goal:
Join Gamuda AI Academy

Related Project:
Portfolio Preparation
AI Learning Assistant
Dota 2 Analyzer


This helps understand which projects contribute towards bigger goals.

---

# 9. ALPA Dashboard

A central overview of current progress.

Dashboard displays:

- Total goals
- Total projects
- Active projects
- Learning sessions
- Learning time
- Main learning focus
- Recommended project

Example:

========== ALPA DASHBOARD ==========

Goals: 1
Projects: 11
Active Projects: 7
Learning Sessions: 5
Learning Time: 300 minutes
Main Focus: Programming
Recommended Project: Priority Test

====================================

# 🛠️ Technology Stack

Built with:

- Python
- SQLite
- Pandas
- Matplotlib

Python concepts applied:

- Object-Oriented Programming
- Modular architecture
- Database CRUD operations
- Data analysis
- Error handling
- Function abstraction

# 📂 Project Structure

AI-Learning-Assistant

│
├── main.py
├── database.py
├── learning.db
│
├── models
│ ├── activity.py
│ ├── project.py
│ └── goal.py
│
├── services
│ ├── analyzer.py
│ ├── insight.py
│ ├── decision_engine.py
│ └── dashboard.py
│
└── README.md


---

# 🎯 Future Improvements

Planned improvements:

- AI-powered learning recommendations
- Web dashboard interface
- Better visualization
- Learning statistics
- Export reports
- Cloud database support

---

# 👨‍💻 Author

Built by Ubaidillah Abdullah

A personal project developed to improve learning consistency, project management, and software development skills.

---

# 📌 Version

Current Version:

ALPA v1.0

Status: Ready for daily personal use!
