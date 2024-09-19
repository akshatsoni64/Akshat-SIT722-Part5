# Dockerfile for inventory_management microservice
# Use the base image of Python 3.9
FROM python:3.9-slim 

# Set the working directory
WORKDIR /app

# Copy the content of app folder into current working directory
COPY inventory_management/app .

# Install the python libraries in the environment as mentioned in the requirements.txt file
RUN pip3 install -r requirements.txt

# Expose the port 8080 on the host machine
EXPOSE 8082

# Command to run the uvicorn server, deploying the fastapi application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8082"]