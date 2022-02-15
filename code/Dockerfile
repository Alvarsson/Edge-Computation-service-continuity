# simple dockerfile for python based program.
FROM python:3.8-slim-buster

WORKDIR /src

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV FLASK_APP=main.py
EXPOSE 5000

#CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD ["python3","-m","flask", "run", "--host=0.0.0.0"]