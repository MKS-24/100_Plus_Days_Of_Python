import logging

logging.basicConfig(level=logging.INFO)

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b

# log_function_call(my_function)(2,2)
my_function(4.2,3)



#  Ye Function ko edit kerke print kerte hai