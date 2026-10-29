FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY cryptor.py .

RUN useradd -u 1001 saturn_cryptor_user
USER saturn_cryptor_user

CMD ["python", "cryptor.py"]