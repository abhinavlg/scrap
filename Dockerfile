# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Install dependencies for Playwright
RUN apt-get update && apt-get install -y \
    libgdk-pixbuf2.0-0 \
    libavif.so.15 \
    libgstgl-1.0.so.0 \
    libgstcodecparsers-1.0.so.0 \
    libenchant-2.so.2 \
    libsecret-1.so.0 \
    libmanette-0.2.so.0 \
    libGLESv2.so.2 \
    && rm -rf /var/lib/apt/lists/*

# Set up a working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN python -m playwright install

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose the port the app runs on
EXPOSE 8080

# Run the app
CMD ["python", "app.py"]
