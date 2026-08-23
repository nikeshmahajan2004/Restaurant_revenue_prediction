# base image
FROM python:3.12.3-slim

# Working directory
WORKDIR /app

# Copy
COPY . /app

# run
RUN pip install -r requirements.txt

# Port
EXPOSE 5000

# Command
CMD ["python","app.py"]