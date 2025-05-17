class Logger:
    def __init__(self):
        print("Logger Initialized")

    def __del__(self):
        print("Logger Destroyed")

# Example
log = Logger()
del log
