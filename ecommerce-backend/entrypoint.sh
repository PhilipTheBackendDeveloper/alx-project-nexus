#!/bin/bash

set -e

echo "================================================"
echo "🚀 Starting E-Commerce API Deployment"
echo "================================================"

# Wait for database to be ready
echo " Waiting for database to be ready..."
sleep 5

# Additional database check
echo " Checking database connection..."
python << END
import sys
import time
import psycopg2
import os

max_retries = 30
retry_count = 0

while retry_count < max_retries:
    try:
        conn = psycopg2.connect(os.environ.get('DATABASE_URL'))
        conn.close()
        print(" Database connection successful!")
        sys.exit(0)
    except psycopg2.OperationalError as e:
        retry_count += 1
        print(f" Attempt {retry_count}/{max_retries}: Database not ready yet...")
        time.sleep(2)

print(" Could not connect to database after maximum retries")
sys.exit(1)
END

# Run database migrations
echo ""
echo "  Running database migrations..."
python manage.py migrate --noinput

# Collect static files
echo ""
echo " Collecting static files..."
python manage.py collectstatic --noinput

# Run production setup (create superuser + load sample data)
echo ""
echo "  Running production setup..."
python manage.py setup_production || echo "  Setup command not found or failed - continuing anyway"

echo ""
echo "================================================"
echo " Deployment Complete!"
echo "================================================"

# Start Gunicorn server
echo ""
echo " Starting Gunicorn server on port ${PORT:-8000}..."
echo ""
exec gunicorn config.wsgi:application \
    --bind 0.0.0.0:${PORT:-8000} \
    --workers 3 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile -