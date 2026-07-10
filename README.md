# 📋 Project Task Manager

A simple web-based Project Task Manager built using Flask and MySQL. The application allows users to register, log in securely, and manage their personal tasks with complete CRUD (Create, Read, Update, Delete) functionality.

## 🚀 Features

- User Registration & Login
- Secure Password Hashing
- Session-based Authentication
- Create Tasks
- View Tasks
- Edit Tasks
- Delete Tasks
- Dashboard with Task Statistics
- Responsive User Interface
- MySQL Database Integration

## 🛠 Tech Stack

- Frontend
  - HTML5
  - CSS3
  - JavaScript

- Backend
  - Python
  - Flask

- Database
  - MySQL (Railway)

- Deployment
  - Render

## 📂 Project Structure

```
task_manager/
│
├── app.py
├── config.py
├── requirements.txt
├── Procfile
├── README.md
├── .env
│
├── static/
│   └── style.css
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── add_task.html
│   └── edit_task.html
│
└── screenshots/
```

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/task-manager.git
cd task-manager
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file in the project root.

```
SECRET_KEY=your_secret_key

MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=task_manager
```

For deployment, replace these values with your Railway MySQL credentials.

## Run the Application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

## Database Schema

### Users Table

- id
- name
- email
- password
- created_at

### Tasks Table

- id
- user_id
- title
- description
- priority
- status
- due_date
- created_at

## Deployment

- Database hosted on Railway MySQL
- Application deployed on Render

## Future Improvements

- Search Tasks
- Task Filtering
- Email Notifications
- Task Categories
- Due Date Reminders
- File Attachments
