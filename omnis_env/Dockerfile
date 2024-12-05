# Base image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Expose port for any web services (if applicable)
EXPOSE 8000

# Command to run your application
CMD ["python", "scripts/main.py"]
