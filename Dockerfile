# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the bot script into the container
COPY TelegramAsciiBot.py .

# Install required Python packages
RUN pip install python-telegram-bot pyfiglet

# Command to run the bot
CMD ["python", "TelegramAsciiBot.py"]
