FROM python:3.10-slim

# Set the timezone (for the pi's sake)
ENV TZ=America/New_York

# Install build tools and dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

    
# Install RPi.GPIO
RUN pip install RPi.GPIO

# Set the working directory
WORKDIR /backend

RUN pip install poetry==1.6.1

# Copy the requirements file
COPY  pyproject.toml poetry.lock ./

RUN poetry install


# Want to copy this last so it only changes 
COPY ./app ./app

# Run the application
CMD ["poetry", "run", "python", "app/button/button.py"]