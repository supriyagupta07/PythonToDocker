**My first Dockerized app :D**
Welcome to my mini Flask web app that's fully Dockerized and deployed online!  
This was my first project where I explored how to containerise a Python web app and deploy it. 

**What it does**
This is a simple Python Flask web application that:
* Displays a customised HTML welcome message.
* It is containerised using **Docker**.
* Helps beginners learn the end-to-end workflow of local development → Docker → live deployment.

Before I start, it's important to know, I did it on Windows in Command Prompt.

**What is each file doing?**
_app.py_: It’s the core of what my Docker container is running "Hello, Supriya!" message (or any other logic) lives here.

_requirements.txt_: This file lists all the Python libraries your app depends on. For your project, the main one is Flask.
When Docker is building the image, it uses this file to install Flask inside the container environment, ensuring your app has everything it needs to run.

_Dockerfile _: Without this file, Docker wouldn’t know how to package your app. It’s what transforms your local Python app into a portable Docker container.

Steps it follows: 
* Uses Python as the base image.
* Copies your app and dependencies into the container.
* Installs the dependencies from requirements.txt.
* Runs your Flask app on container start.

_test-web-app.sh_ (Optional): There are two commands in this file. This is for Unix-based terminals (like Bash). If you are using Windows then you will have to manually run these commands. It automates the process of building and running your Docker container.

**ERRORS**
This project was a real hands-on ride! Some issues I ran into and resolved:
* Docker Daemon not running — resolved by starting Docker Desktop app on laptop manually.
* Dockerfile: no such file or directory — fixed by making sure I'm in the correct directory before building.
* Render deployment errors — solved by matching Docker paths and ensuring the repo structure was clean.
Every time I updated app.py, I had to rebuild the image & rerun the container — learned about efficient container use!

Please feel free to reach out if you have any questions. Happy learning :D
