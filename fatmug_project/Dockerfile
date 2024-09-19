# Dockerfile

# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . /app/

# Run migrations and collect static files
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn fatmug_project.wsgi:application --bind 0.0.0.0:8000"]
