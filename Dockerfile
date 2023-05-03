FROM python:3.12.0a7-bullseye

COPY . .

RUN apt update && apt install -y python3-pip && pip3 install -r requirements.txt

ENTRYPOINT ["app.py"]