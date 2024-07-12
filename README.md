# Todo Django App

## Overview

# Todo Django Backend API

This project implements a Todo App backend using Python and Django, exposing CRUD (Create, Read, Update, Delete) functionalities via APIs. It includes user authentication with different roles (admin and user) and implements access control based on these roles.

## Features

- **Authentication:**
  - User authentication using JWT (JSON Web Token).
  - Two user roles: "admin" and "user".
  - Only authenticated users can access the APIs.

- **CRUD Functionality:**
  - **Create:** Create a new Todo.
  - **Read:** Retrieve all Todos or details of a specific Todo.
  - **Update:** Update details of a Todo (accessible by admin only).
  - **Delete:** Delete a Todo (accessible by admin only).

- **Access Control:**
  - Users with the "admin" role can update and delete any Todo.
  - Users with any other role can create, retrieve, and update their own Todos.

- **Task Expiration:**
  - Todos have an expiration feature implemented using JWT expiry time (e.g., 5 minutes).
  - Expiry time is included in the JWT payload for secure handling.

## API Endpoints

- **Admin Interface:** `/admin/`
  - Django admin interface for managing users and Todos.

- **Swagger Documentation:** `/swagger/`
  - Interactive API documentation using Swagger UI.

- **API Routes:**
  - `/api/`: Includes all Todo related endpoints.
  - `/register/`: Register a new user.
  - `/login/`: Obtain JWT tokens for authentication.
  - `/token/refresh/`: Refresh JWT access tokens.
  - `/todos/`: List all Todos and create new Todos.
  - `/todos/<int:pk>/`: Retrieve, update, or delete a specific Todo.
  - `/logout/`: Endpoint to invalidate JWT tokens and log out.

## Technologies Used

- **Django:** Backend framework for web development.
- **Django REST Framework (DRF):** Toolkit for building Web APIs in Django.
- **SQLite3:** Default database used for simplicity and ease of setup.
- **JWT:** Used for secure user authentication and session management.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/todo-django.git
   cd todo-django
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

4. Run the development server:
   ```bash
   python manage.py runserver 80
   ```

5. Access the APIs:
   - Open `http://localhost:80/swagger/` in your browser to view and interact with the API endpoints using Swagger UI.
   - Use the admin interface at `http://localhost:80/admin/` to manage users and Todos.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or issues, please create a new issue or pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with love and Django.

```
Username: masterplan
Email address: isakajames@medikea.co.tz
Password: hDF98&@bRTaE4
```
