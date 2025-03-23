FROM python:3.8

# Copy the application files into the Docker container
COPY . /app

# Copy the model file into the container (adjust the path as necessary)
COPY artifacts/best_model.pkl /app/artifacts/best_model.pkl

# Set the working directory
WORKDIR /app

# Install the dependencies
RUN pip install -r requirements.txt

# Expose the necessary port
EXPOSE 5000

# Start the Flask application (use gunicorn in production)
CMD ["python", "app.py"]
