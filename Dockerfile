FROM python:3.12.0a7-bullseye

COPY . .

ENTRYPOINT ["app.py"]