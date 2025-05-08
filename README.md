# Flask To-Do List App

This project is a simple To-Do List application built using Python and Flask. The app allows users to add and delete tasks through a web interface.

## Features

* **Add Tasks:** Enter a task and click the "Add Task" button to add it to the list.
* **Delete Tasks:** Click the "Delete" link next to a task to remove it from the list.
* **Web Interface:** Simple and user-friendly interface built with HTML and Flask.

## Prerequisites

* Python 3.x
* Flask library

## Installation

Clone the repository and install Flask:

```bash
git clone https://github.com/tallaladnan/flask-todo-list.git
cd flask-todo-list
pip install flask
```

## Running the App

To start the Flask server:

```bash
python app.py
```

Visit the app at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Usage

1. Open the app in your browser.
2. Enter a new task and click "Add Task".
3. To delete a task, click the "Delete" link next to it.

## How It Works

1. **Adding a Task:** Uses a POST request to add a task to the list.
2. **Deleting a Task:** Uses the task's index to remove it via a GET request.
3. **Rendering the List:** Uses Flask's Jinja2 template engine to dynamically display tasks.

## Future Improvements

* Add task completion functionality.
* Use a database to store tasks persistently.
* Improve UI with CSS and JavaScript.
