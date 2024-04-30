# TravelBlog - A Django Travel Blog Application
### Developed by Sayed Husain Alawi

## Description
TravelBlog is a Django-based web application designed for travel enthusiasts to share their experiences and reviews 
about different locations worldwide. The application allows users to register and manage their accounts. Registered 
users can add, edit, or delete their posts about cities and countries they have visited. The application employs a 
clean and modern user interface styled using Bootstrap, providing a user-friendly experience.

## Getting Started

### Prerequisites
Ensure you have Python installed on your system. The project is developed using Python 3.12.1. 
You can download it from [python.org](https://www.python.org/downloads/).

### Installation
Follow these steps to set up the project environment:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/bigguysayedhusain/miniproject4Sayed_Alawi.git
   ```

2. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
   - Ensure you see "20 migrations need to be applied."
   - Stop the server with CTRL+C.


4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the server again:**
   ```bash
   python manage.py runserver
   ```
   - Navigate to http://127.0.0.1:8000/travelblog/ to test the functionality of the website.
   - Note that at this point, there are no countries imported yet.
   - Stop the server with CTRL+C.

    
6. **Import countries:**
   ```bash
   python manage.py import_countries
   ```

7. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```
   - Follow the prompts to create an administrator account.


8. **Restart the server:**
   ```bash
   python manage.py runserver
   ```
   - Visit http://127.0.0.1:8000/admin to access the admin panel using your superuser credentials.

## Dependencies
This application uses a SQLite database to store data about users, posts, cities, and countries. 
Python comes with built-in support for SQLite in the `sqlite3` module.

## Authors
- **Sayed Husain Alawi**

## Version History
- 0.1
  - Initial Release

## License
This project is released under the CC0 1.0 Universal (CC0 1.0) Public Domain Dedication. You can copy, modify, distribute, and perform the work, even for commercial purposes, all without asking permission. More details can be found at [creativecommons.org/publicdomain/zero/1.0/](https://creativecommons.org/publicdomain/zero/1.0/).

## Acknowledgments
- [Django Documentation](https://docs.djangoproject.com/en/4.0/).
- [Bootstrap for front-end styling.](https://getbootstrap.com/)
- [OpenAI - ChatGPT.](https://chat.openai.com/)

---