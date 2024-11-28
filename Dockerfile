# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port your application will run on
EXPOSE 8000

# Set the entry point for your application (adjust if you use Gunicorn, etc.)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]