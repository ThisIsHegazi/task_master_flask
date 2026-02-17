# TaskMaster ✅

A clean, lightweight task management web app built with **Flask** and **SQLite**. Add, update, and delete tasks with a simple and intuitive interface.

## 🚀 Features

- ➕ Add new tasks instantly
- ✏️ Edit existing tasks
- 🗑️ Delete completed or unwanted tasks
- 📅 Tasks are timestamped and sorted by creation date
- 💾 Persistent storage with SQLite

---

## 🛠️ Tech Stack

| Layer     | Technology          |
|-----------|---------------------|
| Backend   | Python, Flask       |
| Database  | SQLite, SQLAlchemy  |
| Frontend  | HTML, CSS           |

---

## 📁 Project Structure

```
taskmaster/
├── app.py              # Main Flask application
├── instance/
│   └── tasks.db        # SQLite database (auto-generated)
├── templates/
│   ├── home.html       # Main task list page
│   └── update.html     # Task update page
└── static/
    └── css/            # Stylesheets
```

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/](https://github.com/ThisIsHegazi/task_master_flask.git
   cd task_master_flask

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask flask-sqlalchemy
   ```

4. **Initialize the database**
   ```bash
   python
   >>> from app import app, db
   >>> with app.app_context():
   ...     db.create_all()
   >>> exit()
   ```

5. **Run the app**
   ```bash
   python app.py
   ```

6. Open your browser and visit `http://127.0.0.1:5000`

---

## 🔗 Routes

| Route                    | Method     | Description          |
|--------------------------|------------|----------------------|
| `/` or `/home`           | GET, POST  | View and add tasks   |
| `/delete/<task_id>`      | GET        | Delete a task        |
| `/update/<task_id>`      | GET, POST  | Update a task        |
