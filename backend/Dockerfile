# Use official Python image
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install dependencies
RUN pip install flask mysql-connector-python

# Expose port 5000 for Flask
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]

