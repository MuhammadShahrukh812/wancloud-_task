FROM python:3.8.0-buster
WORKDIR /flaskProject
ADD . /flaskProject
EXPOSE 8000
COPY . /requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt