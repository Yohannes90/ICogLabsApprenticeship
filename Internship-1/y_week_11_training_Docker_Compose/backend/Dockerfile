# Use Python image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy everything
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose port 8000 for the Flask app
EXPOSE 8000

# Define environment variable to specify the entry point for Flask
ENV FLASK_APP=app.py

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
