# Week 1 — App Containerization

## Backend Flask
Created Dockerfile for backend flask
```
# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable to tell Flask to listen on port 8080
ENV FLASK_RUN_PORT=4567
ENV FLASK_ENV='development'

# Expose port 8080 for the Flask app to listen on
EXPOSE 4567

# Define the command to run the Flask app when the container starts
CMD ["flask", "run", "--host=0.0.0.0"]

```
To run the Dockerfile for backend

```
docker build -t crudder-back-end .
docker run -p 4567:4567 crudder-back-end
```

Test the API endpoint using INSOMNIA or POSTMAN
hit endpoint `localhost:4567`


Created .ENV file
```
FRONTEND_URL="*"
BACKEND_URL="*"
``` 

Created Config.py for the ENV global variables
```
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()


FRONTEND = os.getenv('FRONTEND_URL')
BACKEND = os.getenv('BACKEND_URL')


```


## Frontend React JS
Created Dockerfile for frontend react JS

```
# Use an official Node runtime as the base image
FROM node:14-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code to the container
COPY . .

# Build the React app
RUN npm run build

# Expose the port that the app will run on
EXPOSE 3000

# Start the app
CMD [ "npm", "start" ]

```

To run the frontend
```
docker build -t crudder-frontend .
docker run -p 3000:3000 crudder-frontend
```



## Docker-compose.yml
Created docker compose file for orchestrating the backend and frontend

```
version: '3'
services:
  crudder-frontend:
    build:
      context: ./frontend-react-js
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    volumes:
      - ./frontend-react-js:/app
      - /app/node_modules
    environment:
      - REACT_APP_BACKEND_URL=http://localhost:4567
    depends_on:
      - crudder-backend
  crudder-backend:
    build:
      context: ./backend-flask
      dockerfile: Dockerfile
    ports:
      - "4567:4567"
    volumes:
      - ./backend-flask:/app
    environment:
      - FLASK_APP=app.py
      - FLASK_ENV=development
      - FRONTEND_URL=*
      - BACEND_URL=*
```

To execute the command
```
docker-compose build
docker-compose up

```