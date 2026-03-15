# CMDB (Django)

A simple **Computer Management System** built using **Django**.

This application allows users to search IT assets, report issues, communicate with administrators, and assign engineers to resolve problems.

Repository:
https://github.com/Misrabharat/cmdb_manoj

---

# Features

• User Login System
• Asset Search
• Asset Detail Page
• Chat / Comment System
• Admin Assignment to Engineers
• Status Tracking (Open / In Progress / Resolved)
• Django Admin Panel for Asset Management

---

# Technology Stack

Backend: Django 6.0
Database: SQLite
Frontend: Bootstrap 5
Language: Python 3.11+

Libraries Used:

* Django
* pandas
* openpyxl
* numpy

---

# Project Structure

```
cmdb_manoj/
│
├── assets/                 # Django app
├── config/                 # Django project settings
├── templates/              # HTML templates
├── assets.xlsx             # Sample asset data
├── import_excel.py         # Excel import script
├── manage.py
├── requirements.txt
└── README.md
```

---

# System Requirements

Python 3.11 or higher

Download Python:
https://www.python.org/downloads/

---

# Installation Steps

### 1. Clone the repository

```
git clone https://github.com/Misrabharat/cmdb_manoj.git
```

### 2. Navigate to project folder

```
cd cmdb_manoj
```

### 3. Create virtual environment

Windows:

```
python -m venv venv
```

### 4. Activate virtual environment

Windows:

```
venv\Scripts\activate
```

### 5. Install dependencies

```
pip install -r requirements.txt
```

### 6. Run database migrations

```
python manage.py migrate
```

### 7. Create admin user

```
python manage.py createsuperuser
```

### 8. Run the application

```
python manage.py runserver
```

### 9. Open the application

```
http://127.0.0.1:8000
```

---

# Import Asset Data (Optional)

To import assets from Excel:

```
python import_excel.py
```

This will load asset records into the database.

---

# Application Workflow

User => Search Asset
User => Raise Issue / Comment
Admin => Review Issue
Admin => Assign Engineer
Engineer => Resolve Issue
Admin => Update Status (Resolved)

---

# Admin Panel

Access Admin Panel:

```
http://127.0.0.1:8000/admin
```

Admin capabilities:

• Manage assets
• Assign engineers
• View chat history
• Update issue status

---

# Future Improvements

• Email notifications
• Dashboard analytics
• Role based permissions
• Ticket number generation
• File attachments for issues
• Docker deployment

---

# Author

Bharat Mishra

GitHub:
https://github.com/Misrabharat

---

# License

This project is for **educational and demonstration purposes**.
