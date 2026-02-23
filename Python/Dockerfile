FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt --target=/app/libs 

COPY . .

FROM gcr.io/distroless/python3-debian12

WORKDIR /app

COPY --from=builder /app/libs /app/libs

COPY --from=builder /app /app 

ENV PYTHONPATH=/app/libs

CMD ["app.py"]
