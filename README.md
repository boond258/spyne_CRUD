# Discussion Forum Project
This project is a web application built using Flask, which allows users to register, log in, create discussions, and interact with each other through posts and comments. It also integrates with an external API for user authentication.

## Features
User Registration and Login
Create, Update, Delete Discussions
Comment and Like Posts
Follow Other Users
Search Users and Posts
API Integration for User Authentication
Setup Instructions
Prerequisites
Ensure you have the following installed:

Python 3.6+
Flask
Flask-Login
Flask-SQLAlchemy
Flask-WTF
requests
Installation
## Clone the repository:
```bash
sh
Copy code
git clone https://github.com/yourusername/discussion-forum.git
cd discussion-forum
```

# Create and activate a virtual environment:
```bash
sh
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

# Install the required packages:
```bash
sh
Copy code
pip install -r requirements.txt
```
# Set up the database:
```bash
sh
Copy code
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
Configuration
Create a .env file in the project root with the 
```

# Following content:
```bash
env
Copy code
SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=sqlite:///site.db
RAPIDAPI_KEY=your_rapidapi_key
API_KEY=your_api_key
```

# Running the Application
(Run the Flask application)
```bash
sh
Copy code
flask run
Open your web browser and navigate to http://127.0.0.1:5000.
```


# Project Structure
```bash
discussion-forum/
│
├── app/
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   └── static/
│       └── style.css
│
├── migrations/
│
├── .env
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

# API Endpoints
(User Registration)

#### URL: /api/register
#### Method: POST
#### Payload:json
```bash
{
  "name": "John Doe",
  "email": "john@example.com",
  "mobile_no": "1234567890",
  "password": "securepassword"
}
```
### Response:

```bash
{
  "message": "User created successfully"
}
```

## User Login
#### URL: /api/login
#### Method: POST
#### Payload:json
```bash
{
  "email": "john@example.com",
  "password": "securepassword"
}
```
## Response:
```bash
{
  "token": "some_generated_token"
}
```

## Forms

### RegistrationForm
#### Fields:
#### name
#### email
#### mobile_no
#### password
#### confirm_password
#### LoginForm
#### Fields:
#### email
#### password
#### remember
#### Templates
#### home.html
```bash
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <div class="container">
        <h2>Welcome to the Discussion Forum</h2>
        {% if current_user.is_authenticated %}
            <p>Hello, {{ current_user.name }}!</p>
            <a href="{{ url_for('logout') }}">Logout</a>
        {% else %}
            <a href="{{ url_for('login') }}">Login</a> |
            <a href="{{ url_for('register') }}">Register</a>
        {% endif %}
    </div>
</body>
</html>
register.html
html
Copy code
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
</head>
<body>
    <div class="container">
        <h2>Register</h2>
        <form method="POST">
            {{ form.hidden_tag() }}
            <div>{{ form.name.label }} {{ form.name() }}</div>
            <div>{{ form.email.label }} {{ form.email() }}</div>
            <div>{{ form.mobile_no.label }} {{ form.mobile_no() }}</div>
            <div>{{ form.password.label }} {{ form.password() }}</div>
            <div>{{ form.confirm_password.label }} {{ form.confirm_password() }}</div>
            <div>{{ form.submit() }}</div>
        </form>
    </div>
</body>
</html>
```

## login.html
```bash
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <div class="container">
        <h2>Login</h2>
        <form method="POST">
            {{ form.hidden_tag() }}
            <div>{{ form.email.label }} {{ form.email() }}</div>
            <div>{{ form.password.label }} {{ form.password() }}</div>
            <div>{{ form.remember() }} {{ form.remember.label }}</div>
            <div>{{ form.submit() }}</div>
        </form>
    </div>
</body>
</html>
```