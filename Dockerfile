# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Install dependencies for Playwright and other required libraries
RUN apt-get update && apt-get install -y \
    libx11-dev libxcomposite-dev libxdamage-dev libxrandr-dev \
    libgbm-dev libatspi2.0-dev libgtk-3-dev libnss3-dev \
    libgdk-pixbuf2.0-dev libavcodec-dev libavformat-dev \
    libavutil-dev libenchant-2-2 libsecret-1-dev libappindicator3-dev \
    libasound2-dev libxss1 libxtst6 libnss3 libnss3-tools \
    && rm -rf /var/lib/apt/lists/*

# Set up a working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose the port the app runs on
EXPOSE 8080

# Install Playwright browsers
RUN python -m playwright install

# Run the app
CMD ["python", "app.py"]
