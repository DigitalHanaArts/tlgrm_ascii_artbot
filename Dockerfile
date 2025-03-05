# Use official Python image as a base
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install required Python packages
RUN pip install python-telegram-bot pyfiglet

# Command to run the bot
CMD ["python", "TelegramAsciiBot.py"]
