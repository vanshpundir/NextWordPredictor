# Use the official Python image as a base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install required packages from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the Flask app will run on (if your app runs on a different port, modify this)
EXPOSE 5000

# Set the environment variable for Flask (you can change the value to your Flask app's main Python file)
ENV FLASK_APP=app.py

# Command to run the Flask app when the container starts
CMD ["python", "app.py"]
