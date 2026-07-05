# Django Monthly Challenges Example

A simple yet powerful Django project designed to help developers practice and showcase their skills through monthly coding challenges. This platform is perfect for learners, hobbyists, and professionals looking to improve their Python and web development abilities.

## Table of Contents
1. [Features](#features)
2. [How It Works](#how-it-works)
3. [Technology Stack](#technology-stack)
4. [Requirements](#requirements)
5. [Installation](#installation)
6. [Configuration](#configuration)
7. [Quick Start](#quick-start)
8. [Usage](#usage)
9. [Project Structure](#project-structure)
10. [Development](#development)
11. [Limitations](#limitations)
12. [License](#license)

## Features
### Challenge Management
- **Admin Interface**: Easily create, edit, and delete coding challenges.
- **User Authentication**: Secure user accounts for tracking progress and achievements.

### Responsive Design
- **Mobile-Friendly**: The platform is designed to be accessible on various devices.

### Customizable Challenges
- **Multiple Difficulty Levels**: Choose from easy, medium, and hard challenges.
- **Custom Challenge Creation**: Users can create their own challenges for the community.

## How It Works
The Django Monthly Challenges Example follows a straightforward architecture:

1. **User Authentication**: Users log in using their credentials or social media accounts.
2. **Challenge Selection**: Users browse through available challenges based on difficulty and category.
3. **Submission**: Users submit their solutions, which are automatically checked for correctness.
4. **Feedback**: Users receive feedback on their submissions, including hints and explanations.

## Technology Stack
| Technology | Purpose |
|------------|---------|
| Django     | Web framework for building robust web applications. |
| Python     | Programming language used for backend development. |
| PostgreSQL | Database management system for storing user data and challenges. |
| Bootstrap  | Frontend framework for responsive design. |

## Requirements
- **Python**: 3.8 or higher
- **Django**: 3.2 or higher
- **PostgreSQL**: 10 or higher

## Installation
To install the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/PartORG/Django_Monthly_Challanges_Example.git
   cd Django_Monthly_Challanges_Example
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Configuration
The project uses environment variables for configuration. You can set these in a `.env` file:

```plaintext
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
DATABASE_URL=postgres://user:password@localhost/dbname
```

## Quick Start
To get started quickly, follow these steps:

1. Clone the repository and navigate to the project directory.
2. Set up a virtual environment and install dependencies.
3. Apply migrations and create a superuser.
4. Run the development server.

## Usage
Here are some example commands and usage scenarios:

- **Creating a new challenge**:
  ```bash
  python manage.py createsuperuser
  # Follow prompts to create an admin user
  ```

- **Running the development server**:
  ```bash
  python manage.py runserver
  # Access the platform at http://127.0.0.1:8000/
  ```

## Project Structure
```
Django_Monthly_Challanges_Example/
├── challenges/
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── static/
│   │   └── challenges/
│   │       ├── challenge.css
│   │       ├── includes/
│   │       │   ├── header.css
│   │       │   └── header.html
│   │       └── index.css
│   ├── templates/
│   │   └── challenges/
│   │       ├── challenge.html
│   │       ├── includes/
│   │       │   └── header.html
│   │       └── index.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── monthly_challenges/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
```

## Development
The project follows a standard Django development workflow:

1. **Feature Branches**: Create feature branches for new features.
2. **Code Reviews**: Submit pull requests for code reviews.
3. **Merging**: Merge approved changes into the main branch.

## Limitations
- **Single Database**: The platform currently supports only one database instance.
- **Basic Authentication**: Basic authentication is used for simplicity; consider using OAuth for production environments.

## License
This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more details.