import multiprocessing

bind = "0.0.0.0:8180"
workers = multiprocessing.cpu_count() * 2 + 1
threads = multiprocessing.cpu_count() * 2
accesslog = "/logs/access.log"
errorlog = "/logs/error.log"
