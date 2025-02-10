# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy all files to container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start the bot
CMD ["python", "main.py"]
