# CMDB Asset Management System (Django)

A simple **Configuration Management Database (CMDB)** and **IT Asset Support System** built using **Django**.

This application allows users to search assets, raise issues, communicate with administrators, and assign engineers to resolve problems.

---

# Features

• User Login
• Asset Search
• Asset Details View
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
asset_management/
│
├── assets/                # Django app
├── config/                # Django project settings
├── templates/             # HTML templates
├── assets.xlsx            # Sample asset data
├── import_excel.py        # Script to import Excel data
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

1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/cmdb-asset-management.git
```

2. Navigate to the project folder

```
cd cmdb-asset-management
```

3. Create virtual environment

Windows:

```
python -m venv venv
```

4. Activate virtual environment

Windows:

```
venv\Scripts\activate
```

5. Install required packages

```
pip install -r requirements.txt
```

6. Run database migrations

```
python manage.py migrate
```

7. Create admin user

```
python manage.py createsuperuser
```

8. Start the server

```
python manage.py runserver
```

9. Open the application

```
http://127.0.0.1:8000
```

---

# Import Asset Data (Optional)

To import asset data from Excel:

```
python import_excel.py
```

This will load asset information into the database.

---

# Application Workflow

User → Search Asset
User → Raise Issue / Comment
Admin → Review Issue
Admin → Assign Engineer
Engineer → Resolve Issue
Admin → Mark Status Resolved

---

# Admin Panel

Access Django Admin Panel:

```
http://127.0.0.1:8000/admin
```

Admin can:

• Manage assets
• Assign engineers
• View chat history
• Update issue status

---

# Screens

Main features include:

• Asset Search Dashboard
• Asset Details Page
• Comment / Chat System
• Admin Assignment System
• Status Tracking

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

Developed as a Proof of Concept CMDB / IT Support System using Django.

---

# License

This project is for educational and demonstration purposes.

