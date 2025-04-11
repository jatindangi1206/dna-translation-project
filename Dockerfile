FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]

# Instructions to build and deploy the Docker image to GitHub Pages
# Build the Docker image
# docker build -t dna-translation .

# Run the Docker container
# docker run -p 8080:8080 dna-translation

# Deploy to GitHub Pages
# ghp-import -n -p -f build
