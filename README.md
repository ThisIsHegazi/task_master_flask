# Task Master Flask

## Overview
Task Master Flask is a web application built using Flask, designed to help users manage their tasks efficiently. It offers features such as CRUD operations for tasks, user authentication, and an intuitive user interface.

## Features
- User Authentication: Register, login, and manage account settings.
- Task Management: Create, read, update, and delete tasks.
- Due Dates: Set and manage due dates for tasks.
- User-friendly Interface: Easy-to-navigate UI for managing tasks.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ThisIsHegazi/task_master_flask.git
   cd task_master_flask
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Set up the environment variables:
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   ```
2. Run the application:
   ```bash
   flask run
   ```
3. Access the application at `http://127.0.0.1:5000/`.

## Contributing
Contributions are welcome! Please follow the standard process for contributing to open-source projects:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-XYZ`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-XYZ`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Flask framework for being lightweight and easy to use.
- All contributors who have helped improve this project.