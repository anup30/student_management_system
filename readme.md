# Student Management System

A Django-based web application for managing students and courses with a clean, responsive UI using Bootstrap 5.

## Features

- User Registration and Authentication
- Student Management (Create, Read, Update, Delete)
- Course Management (Create, Read, Update, Delete)
- Bootstrap 5 UI with responsive design
- Form validation and error handling
- Success/error messages using Django's message framework

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd student-management-system
```

### 2. Create and Activate Virtual Environment

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install django django-crispy-forms crispy-bootstrap5
```

### 4. Run Migrations

```bash
python manage.py makemigrations core
python manage.py migrate
```

### 5. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser to access the application.

## Project Structure

- **student_management_system/**: Main project folder
- **core/**: Main application with models, views, forms, and templates
  - **models.py**: Defines the Student and Course models
  - **views.py**: Contains class-based views for CRUD operations
  - **forms.py**: Contains forms for Student and Course models
  - **templates/**: HTML templates using Bootstrap 5
- **accounts/**: Authentication-related functionality
  - User registration and login

## Usage

1. Register as a new user or log in
2. Add courses using the "Add Course" button in the navigation bar
3. Add students with course enrollment selection
4. View, edit, and delete student and course records as needed

## Technology Stack

- **Backend**: Django 4+
- **Frontend**: Bootstrap 5
- **Database**: SQLite (default Django database)
- **Forms**: Django forms with Crispy Forms + Bootstrap 5