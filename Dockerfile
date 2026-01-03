FROM python:3.12-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpcap-dev tcpdump ca-certificates \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . /app
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi
CMD ["bash"]
