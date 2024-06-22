FROM python:3.10-slim

# Set the timezone (for the pi's sake)
ENV TZ=America/New_York

# Set the working directory
WORKDIR /backend

RUN pip install poetry==1.6.1
RUN pip install RPi.GPIO


# Copy the requirements file
COPY  pyproject.toml poetry.lock ./

RUN poetry install


# Want to copy this last so it only changes 
COPY ./app ./app

# Run the application
CMD ["poetry", "run", "python", "app/button/button.py"]