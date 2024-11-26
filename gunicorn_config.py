# gunicorn_config.py
workers = 4  # Adjust based on your app's needs (you can start with 4 and increase if necessary)
timeout = 120  # Set the timeout to 120 seconds to handle longer requests
bind = "0.0.0.0:8000"  # Bind to all IP addresses and port 8000, or the port Render expects
