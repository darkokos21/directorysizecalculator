FROM python:3.9-slim

WORKDIR /app

COPY dir_size.py .

RUN mkdir files

CMD ["python", "dir_size.py"]