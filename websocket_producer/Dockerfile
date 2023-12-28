# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip install websocket-client

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 8765 available to the world outside this container
EXPOSE 8765

# Run websocket_producer.py when the container launches
CMD ["python", "app.py"]
