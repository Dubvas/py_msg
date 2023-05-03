FROM python:3.12.0a7-bullseye

COPY . .

RUN apt update && apt install python3-pip && pip3 install requirements.txt

ENTRYPOINT ["app.py"]