"""All config default settings can refer to:
https://github.com/benoitc/gunicorn/blob/master/gunicorn/config.py
"""

bind = "0.0.0.0:5000"
workers = 4
worker_class = "gthread"
threads = 1
timeout = 300
graceful_timeout = 30
loglevel = "debug"
max_requests = 10
