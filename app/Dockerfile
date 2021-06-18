FROM python:3.8-alpine

RUN mkdir /images
RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt

CMD ["python", "main.py"]