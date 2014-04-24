import multiprocessing
#from os import environ

workers = multiprocessing.cpu_count() * 2 + 1
#max_requests = environ.get('GUNICORN_MAX_REQUESTS', 0)
worker_class = 'gevent'
loglevel = 'debug'
timeout = 20
