FROM python:3.11-alpine
WORKDIR /Users/user/Desktop/RoomBooking/
COPY requirements.txt requirements.txt
COPY . /app

RUN pip install pipenv
RUN pipenv install -r requirements
RUN pipenv shell
COPY . .
CMD ["python", "manage.py", "runserver 0.0.0.0:8000"]
