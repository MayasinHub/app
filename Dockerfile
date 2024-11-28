# Use a lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port your application will run on (Render uses $PORT)
EXPOSE 8000

# Command to run your application
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:8000"]
