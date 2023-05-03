FROM python:3.12.0a7-bullseye

COPY . .

RUN pip install requirements.txt

ENTRYPOINT ["app.py"]