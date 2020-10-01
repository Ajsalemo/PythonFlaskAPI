#!/bin/bash
# Simple migration script to save some keystrokes

# Initialize the database(if needed)
# flask db init

# Run migrations
flask db migrate

# Run upgrades(if any)
flask db upgrade

# Start Flask after migrations
export FLASK_APP=app.py
echo "Flask App is set to $FLASK_APP"
flask run