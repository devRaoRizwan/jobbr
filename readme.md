# Jobbr - Job Board Application

A Django REST Framework project built for learning purposes. This is a simple job board platform that demonstrates API development, authentication, and role-based permissions.

## 🚀 Features

### For Employers
- **Post Jobs**: Create detailed job listings with salary, location, job type, and deadlines
- **Manage Applications**: View, review, and update application statuses
- **Dashboard Control**: Full CRUD operations on job postings

### For Job Seekers
- **Browse Jobs**: Search and filter jobs by type, location, salary, and keywords
- **Apply Easily**: Submit applications with resume uploads and cover letters
- **Bookmark Jobs**: Save interesting opportunities for later

### Core Features
- **JWT Authentication**: Secure token-based authentication system
- **Role-Based Access**: Separate permissions for employers and job seekers
- **File Uploads**: Resume storage with Django's media handling
- **Advanced Filtering**: Filter by job type, location, salary period, and search functionality
- **API Documentation**: Interactive Swagger UI documentation
- **Pagination**: Efficient data handling with page-based pagination

## 🛠️ Technology Stack

- **Backend**: Django 4.x + Django REST Framework
- **Authentication**: JWT (JSON Web Tokens) via djangorestframework-simplejwt
- **Database**: SQLite (development) / PostgreSQL (production recommended)
- **API Documentation**: drf-spectacular (Swagger/OpenAPI)
- **Filtering**: django-filter for advanced query capabilities
- **Environment Management**: python-dotenv for configuration

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd jobbr
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the `backend/` directory:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ```

5. **Database Setup**
   ```bash
   python manage.py migrate
   ```

6. **Create Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## 📚 API Documentation

Access the interactive API documentation at:
- **Swagger UI**: `http://127.0.0.1:8000/api/docs/`
- **OpenAPI Schema**: `http://127.0.0.1:8000/api/schema/`

## 🔐 Authentication

The API uses JWT (JSON Web Token) authentication. To access protected endpoints:

1. **Register** a new user account
2. **Login** to obtain access and refresh tokens
3. **Include** the access token in the Authorization header:
   ```
   Authorization: Bearer <your-access-token>
   ```

### User Roles

- **Employer**: Can post jobs and manage applications
- **Job Seeker**: Can browse jobs, apply, and bookmark

## 🌐 API Endpoints

### Authentication (`/api/auth/`)
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login (obtain JWT tokens)
- `POST /api/auth/token/refresh/` - Refresh access token
- `GET /api/auth/me/` - Get current user information

### Jobs (`/api/jobs/`)
- `GET /api/jobs/` - List all open jobs (public)
- `POST /api/jobs/` - Create new job (employers only)
- `GET /api/jobs/{id}/` - Get job details (public)
- `PUT /api/jobs/{id}/` - Update job (employer owner only)
- `DELETE /api/jobs/{id}/` - Delete job (employer owner only)

### Applications (`/api/jobs/`)
- `GET /api/jobs/{job_id}/apply/` - List applications for a job (employer only)
- `POST /api/jobs/{job_id}/apply/` - Apply to a job (job seekers only)
- `PUT /api/jobs/applications/{application_id}/` - Update application status (employer only)

### Bookmarks (`/api/jobs/`)
- `POST /api/jobs/{job_id}/bookmark/` - Toggle bookmark for a job (authenticated users)

## 🔍 Filtering and Search

The jobs endpoint supports extensive filtering:

### Query Parameters
- `job_type`: Filter by job type (`full_time`, `part_time`, `contract`)
- `location`: Filter by location (case-insensitive partial match)
- `salary_period`: Filter by salary period (`hour`, `month`, `year`)
- `search`: Search in title and description
- `ordering`: Order by `salary`, `created_at`, `deadline` (prefix with `-` for descending)

### Examples
```bash
# Search for Python jobs in New York
GET /api/jobs/?search=python&location=new york

# Filter full-time jobs ordered by salary (descending)
GET /api/jobs/?job_type=full_time&ordering=-salary

# Monthly paid jobs
GET /api/jobs/?salary_period=month
```

## 📄 Data Models

### User
- `username`: String (unique)
- `email`: String (unique)
- `role`: Choice (`employer` or `jobseeker`)
- `password`: String (write-only)

### Job
- `title`: String (max 250 chars)
- `description`: Text
- `employer_user`: Foreign Key to User
- `location`: String
- `salary`: Decimal (10 digits, 2 decimal places)
- `salary_period`: Choice (`hour`, `month`, `year`)
- `currency`: String (3 chars, e.g., "USD")
- `job_type`: Choice (`full_time`, `part_time`, `contract`)
- `deadline`: Date (optional)
- `is_closed`: Boolean
- `created_at`: DateTime (auto)
- `updated_at`: DateTime (auto)

### Application
- `job`: Foreign Key to Job
- `applicant`: Foreign Key to User
- `upload_resume`: File (stored in `media/resume/`)
- `cover_letter`: Text (optional)
- `status`: Choice (`applied`, `seen`, `rejected`, `interviewed`)
- `submitted_at`: DateTime (auto)

### Bookmark
- `job`: Foreign Key to Job
- `user`: Foreign Key to User
- `created_at`: DateTime (auto)

## 🗂️ Project Structure

```
jobbr/
├── backend/
│   ├── core/                 # Django project settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   ├── accounts/             # User management app
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── migrations/
│   ├── job/                  # Job board functionality
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── permissions.py
│   │   ├── urls.py
│   │   ├── migrations/
│   │   └── resume/           # Resume upload directory
│   ├── db.sqlite3            # SQLite database
│   ├── manage.py
│   └── requirements.txt
├── media/                    # User-uploaded files (created at runtime)
└── readme.md
```

## 🔒 Security Features

- **JWT Authentication**: Stateless token-based auth
- **Role-based Permissions**: Granular access control
- **Input Validation**: Comprehensive serializer validation
- **CSRF Protection**: Django's built-in CSRF middleware
- **SQL Injection Prevention**: Django ORM protection
- **File Upload Security**: Secure file handling

## 🚀 Deployment

### Environment Variables for Production
```env
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@host:port/database
```

### Recommended Production Setup
1. Use PostgreSQL database
2. Configure proper ALLOWED_HOSTS
3. Set DEBUG=False
4. Use a production WSGI server
5. Set up proper static/media file serving
6. Configure HTTPS
7. Set up proper logging

---

**Created by Rao Rizwan**

**Built with ❤️ using Django REST Framework**