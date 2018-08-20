# Docker image for flask service

FROM python:2.7-alpine

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 11000
CMD ["python", "service.py"]
