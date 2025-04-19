# Use an official Python base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirement.txt /app/
RUN pip install --upgrade pip && pip install -r requirement.txt

# Copy project files
COPY . /app/

# Collect static files (uncomment if you're using Django's collectstatic)
# RUN python manage.py collectstatic --noinput

# Expose the port
EXPOSE 8000

# Run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
