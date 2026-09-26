FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir "boto3>=1.35,<2"

COPY agent.py .

USER 10001

CMD ["python", "-u", "agent.py"]

