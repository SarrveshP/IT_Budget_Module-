# 💼 IT Budget Management System

This is a lightweight web application developed using **Python + Flask** for managing IT budget allocations and expenditures. It allows Admins and Division Heads to enter and track budgets and transactions across various IT categories and divisions.

---

## 🚀 Features

- 🎯 **Budget Master Form**: Define yearly budget by category.
- 🧾 **Transaction Form**: Record actual spending by division.
- 📊 **Live Table Views**: Displays budget and transaction entries.
- ⛔ **Validation Ready**: Setup to include over-utilization checks.
- ⚙️ **Extensible**: Easily add KPIs, reports, authentication, or dashboards.

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (SQLAlchemy ORM)
- **Forms**: Flask-WTF (WTForms)

---

## 📁 Folder Structure
```
IT_Budget_App/
├── app.py # Main application entry point
├── forms.py # WTForm classes for Budget and Transaction
├── models.py # SQLAlchemy DB models
├── templates/ # HTML templates
│ ├── budget_form.html # Budget Master entry and display
│ └── transaction_form.html # Transaction entry and display
├── static/ # Bootstrap and custom styles (optional)
├── instance/ # SQLite DB created here (default)
└── README.md # Project documentation
```


---

## 📌 How to Run

1. 🔃 **Clone the repository**
   ```bash
   git clone https://github.com/your-username/IT-Budget-App.git
   cd IT-Budget-App
🐍 Create a virtual environment

Bash Code :
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
📦 Install dependencies

Bash Code :
pip install -r requirements.txt
🔧 Initialize the database


Py : from app import db
db.create_all()
▶️ Run the app


🌐 Open in browser
Visit: http://127.0.0.1:5000/budget
