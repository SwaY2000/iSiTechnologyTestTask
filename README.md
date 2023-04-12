# BackEnd iSi Technology test task
(Simple chat)
We need to provide an application with 2 models:
● Thread (fields - participants, created, updated)
● Message (fields - sender, text, thread, created, is_read)
Thread can’t have more than 2 participants.

1. Implement REST endpoints for:
● creation (if a thread with particular users exists - just return it.);
● removing a thread;
● retrieving the list of threads for any user;
● creation of a message and retrieving message list for the thread;
● marking the message as read;
● retrieving a number of unread messages for the user.
2. Customize Django admin.
3. Provide pagination(LimitOffsetPagination) where it is needed.
4. Validation in URLs is required, comments are welcome.
5. Add a README.md file with a description of how to run the test task.
6. Create a dump of a database to load test data.
7. Give access to the project in the GIT repository. (Public Access)

## Requirements
- Djangо
- Django Rest Framework
- python-dotenv
- Simple JWT
- database – SQLite

## .gitignore
.gitignore is a file used to specify which files and directories should be ignored by Git when tracking changes in your project. This file is usually located at the root of your project directory.

It's important to include files and directories in your .gitignore that should not be tracked by Git, such as generated files, temporary files, log files, or any sensitive information like API keys or database credentials.

Here are some common files and directories that should be added to your .gitignore:

### venv
The venv directory is a virtual environment that is used to isolate dependencies for your project. This directory should be excluded from version control, as it can be large and contain many files that are not necessary for other developers.

### .idea
The .idea directory is created by PyCharm and contains configuration files for the IDE. This directory should also be excluded from version control, as it is not necessary for other developers.

### pycache
The __pycache__ directory contains compiled bytecode files for your Python code. These files should not be tracked by Git, as they are generated automatically and can be recompiled if necessary.

### .env
The .env file is used to store environment variables for your project, such as database credentials, API keys, or other sensitive information. This file should not be tracked by Git, as it can contain confidential information that should not be shared with other developers.

## Managing environment variables
Create a .env file in the root of the project and add the following variables:
.env/

And in the .env file include the following environment settings:
## Environment Variables
SECRET_KEY_DJANGO_SETTINGS -  it's secret key for Django, which  a string used to encrypt data in the application.

DEBUG - it's boolean variable, for debugging project.
**_Don't run with debug turned on in production!_**

## Running the Django Project
1. Open a terminal or command prompt.
2. Navigate to the root directory of the project.
3. Run the Django development server by running the following command:
   **_python manage.py runserver_**