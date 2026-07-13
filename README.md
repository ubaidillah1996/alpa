# 🚀 ALPA — AI Personal Learning Assistant

**Version: v0.4.0**

ALPA (AI Personal Learning Assistant) is a Python-based productivity system designed to track learning activities, manage ideas and projects, and provide intelligent insights based on personal learning data.

The goal of ALPA is to transform raw learning records into meaningful analysis and actionable recommendations.

---

## ✨ Features

### 📚 Learning Activity Tracker

* Record daily learning activities
* Track category, duration, notes, and rating
* Store learning history using SQLite database
* Validate user input before saving data

---

### 💡 Idea Vault

Manage and organize ideas with:

* Title
* Description
* Priority
* Status

---

### 🚀 Project Tracker

Track ongoing projects with:

* Project name
* Description
* Status
* Progress percentage
* Next action

---

# 🧠 Intelligence Layer (v0.4.0)

ALPA now includes an intelligence system that analyzes learning behavior.

## Daily Analysis

Provides:

* Today's learning sessions
* Total learning time
* Activity summary

Example:

```
Today's Sessions: 3
Today's Learning Time: 180 minutes
```

---

## Weekly Performance Analysis

Analyzes recent learning patterns:

* 7-day activity tracking
* Weekly average learning time
* Performance comparison

Example:

```
7-Day Sessions: 4
Weekly Average: 34.3 minutes
Status: Above Average 🚀
```

---

## Insight Generator

Converts data into meaningful observations.

Example:

```
Strong learning momentum today.
```

---

## Recommendation Engine

Uses project data to suggest the next focus area.

Example:

```
Focus on: Dota 2 Match Analyzer

Next Action:
Complete CRUD
```

---

# 🏗️ Project Architecture

```
AI-Learning-Assistant

│
├── main.py
│
├── database.py
│
├── models
│   ├── activity.py
│   ├── idea.py
│   └── project.py
│
├── menus
│   ├── activity_menu.py
│   ├── idea_menu.py
│   └── project_menu.py
│
├── services
│   ├── analyzer.py
│   └── intelligence.py
│
└── learning.db
```

---

# 🛠️ Technologies Used

* Python
* SQLite
* Pandas
* Git & GitHub

---

# ▶️ How To Run

Clone repository:

```bash
git clone https://github.com/ubaidillah1996/alpa.git
```

Navigate into project:

```bash
cd alpa
```

Run application:

```bash
python main.py
```

---

# 📌 Development Roadmap

## Completed

✅ Activity Tracker
✅ Idea Management
✅ Project Tracker
✅ Database Integration
✅ Input Validation
✅ Learning Analytics
✅ Intelligence Layer v0.4.0

---

## Future Improvements

### v0.5 — Smart Decision Layer

Planned features:

* Productivity scoring
* Project priority ranking
* Learning streak tracking
* Smarter recommendations
* Improved decision support

---

# 👨‍💻 Author

Built as a continuous learning project while exploring:

* Python development
* Software architecture
* Data analysis
* AI-assisted programming

---

⭐ ALPA is continuously evolving from a simple tracker into a personal AI learning companion.

## Version History

### v0.8
- Added project progress history tracking
- Added project analytics
- Track progress changes over time
- Calculate project growth rate
