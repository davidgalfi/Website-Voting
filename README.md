# Website-Voting

This project aims to develop a web application where users can log in with their credentials to participate in voting sessions initiated by an admin user. Users can also register if they don't have an account. The admin has additional privileges like managing users, starting and ending votes, and declaring winners.

## Features

- User Authentication:
  - Users can log in with their credentials or register if new.
  - Admin users are pre-registered with special privileges.

- Voting:
  - Logged-in users can participate in ongoing votes.
  - Admin users can start and manage voting sessions.

- User Profile Management:
  - Users can edit or delete their profiles.
  - Admin can manage user profiles except their own. 
 
## Project Structure

| - admin:
|       | - static: -- Contains static files like CSS and images.
|       | - templates: -- Contains HTML templates for different pages.
|       |        | - admin_base.html
|       |        | - admin_home.html
|       |        | - admin_users.html
|       |        | - admin_newvoting.html
|       | - __init__.py
|       | - admin.py -- It's a Blueprint for admin-related routes and logic.
| - user:
|       | - static: -- Contains static files like CSS and images.
|       | - templates: -- Contains HTML templates for different pages.
|       |        | - user_base.html
|       |        | - user_home.html
|       | - __init__.py
|       | - user.py -- It's a Blueprint for user-related routes and logic.
| - login:
|       | - static: -- Contains static files like CSS and images.
|       | - templates: -- Contains HTML templates for different pages.
|       |        | - login_register_base.html
|       |        | - login.html
|       |        | - register.html
|       | - __init__.py
|       | - login.py -- It's a Blueprint for login-related routes and logic
|       | - register.py -- It's a Blueprint for register-related routes and logic
| - model.py -- Defines SQLAlchemy data models.
| - main.py -- The main Flask application file containing routes and logic.

## Roadmap

1. **Project Setup and Modules Installation**
   - Create the project structure.
   - Install required modules.

2. **Flask Setup**
   - Initialize basic Flask app in `main.py`.
   - Set up main routes.

3. **Website Creation**
   - Create base HTML templates with extensions.
   - Design HTML templates using Bootstrap.

4. **Route Implementation**
   - Implement routes for base templates.
   - Implement login and logout routes.

5. **Database Setup**
   - Define user and admin tables in `models.py`.
   - Define voting table in `models.py`.
   - Integrate database with the main app.

6. **Authentication Implementation**
   - Complete the login functionality.
   - Implement user registration.

7. **Data Management**
   - Implement user profile deletion.
   - Implement admin's ability to delete users.
   - Allow admin to manage votes.

8. **Vote Management**
   - Enable the creation and closure of voting sessions.

## Technologies Used

- Python
- Flask framework
- SQLAlchemy for database management
- Bootstrap for front-end design

## How to Run

1. Clone the repository: `git clone https://github.com/your-username/your-repo.git`
2. Install required dependencies: `pip install -r requirements.txt`
3. Run the application: `python main.py`

Feel free to contribute, report issues, or suggest improvements!

## License

This project is licensed under the MIT License

