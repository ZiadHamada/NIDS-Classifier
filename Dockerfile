# Multi-stage build for production
FROM python:3.10 as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.10
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . /app/

ENV PATH=/root/.local/bin:$PATH
ENV PYTHONPATH=/app

CMD ["python", "app.py"]