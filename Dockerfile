# Containerized environment for reproducibility
FROM python:3.11-slim

# Install system dependencies (git is needed by DVC/Git hooks)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory in container
WORKDIR /app

# Copy dependency files
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy all project files to container
COPY . .

# Expose Jupyter port
EXPOSE 8888

# Default command to run bash
CMD ["bash"]
