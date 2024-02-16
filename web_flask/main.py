#!/usr/bin/python3
"""Flask framework that starts the application"""

from flask import Flask


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def task_display():
    """Print message when called."""
    return 'Hello, Task Manager here!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
