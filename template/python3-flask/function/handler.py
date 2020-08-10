import time


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    time.sleep(0.01)
    print("hello world")
    return req
