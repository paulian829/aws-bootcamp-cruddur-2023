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
