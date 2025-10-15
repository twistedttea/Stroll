# Use the official Python runtime image
FROM python:3.13

# Create the app directory
RUN mkdir /app

# Set the working directory inside the container
WORKDIR /app

# Set environment variables
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Install system dependencies (gcc, mysql-client for MySQL database connection, curl for Node.js)
RUN apt update && apt install -y \
    gcc \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Copy the Django project and install dependencies
# COPY requirements.prod.txt  /app/
COPY requirements.txt  /app/

# run this command to install all dependencies
# RUN pip install --no-cache-dir -r requirements.prod.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project to the container
COPY app/ /app/

# Expose the Django port
EXPOSE 8000

# Start the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "djangoproject.wsgi:application"]
