# Use an official Python Alpine image for maximum compactness
FROM python:3.13-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install runtime dependencies required for Pillow
RUN apk add --no-cache jpeg-dev zlib-dev

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install build dependencies temporarily, install Python packages without cache, then remove build dependencies
RUN apk add --no-cache --virtual .build-deps \
    build-base \
    linux-headers \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps

# Copy the current directory contents into the container
COPY . /app/

# Expose port 8000 for the Django server
EXPOSE 8000

# Define the command to run the application
CMD ["sh", "-c", "python manage.py migrate && python populate_variants.py && python manage.py runserver 0.0.0.0:8000"]
