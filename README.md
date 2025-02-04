Time Website

This is a simple full-stack web application that displays the current server time. The backend is built with Flask (Python), and the frontend is developed using React (JavaScript). The application demonstrates communication between a Flask API and a React frontend. Both services are containerized and managed with Docker and Docker Compose.

Features
	•	Flask Backend: Provides an API endpoint that returns the current server time.
	•	React Frontend: Displays a button to fetch and display the current time from the backend.
	•	Dockerized: Both frontend and backend are containerized for easy setup and deployment.

Project Structure

    /dockerproject
      ├── backend
      │    ├── time.py               # Flask app
      │    └── requirements.txt      # Python dependencies
      ├── frontend
      │    ├── src
      │    │    └── App.js           # React app
      │    └── package.json          # JavaScript dependencies
      ├── Dockerfile.backend         # Dockerfile for Flask
      ├── Dockerfile.frontend        # Dockerfile for React
      └── docker-compose.yml         # Docker Compose setup

Build and Deployment Steps

1. Clone the Repository

        git clone https://github.com/Recepkrky/timewebsite.git
        cd timewebsite

2. Build and Run with Docker Compose

Ensure you have Docker and Docker Compose installed on your machine.
	1.	Build and start the containers:

    docker-compose up --build

2.	Access the application:
•	Frontend (React): http://localhost:3000
•	Backend (Flask API): http://localhost:5001/time

3. Stopping the Application

To stop the containers:

    docker-compose down

Usage
	1.	Open the React app in your browser: http://localhost:3000
	2.	Click the “Get Time” button.
	3.	The current server time from the Flask backend will be displayed.

Contributing

Feel free to fork the project, make enhancements, and submit pull requests.

