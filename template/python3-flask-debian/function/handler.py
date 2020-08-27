import time
import logging


def get_duration(start):
    """
    Example:
    start = time.time()
    # time.sleep(15)
    start = start - 5
    print(get_duration(start))
    start = start - 10
    print(get_duration(start))
    start = start - 46
    print(get_duration(start))
    start = start - (60*60*1 + 15)
    print(get_duration(start))
    start = start - (60*60*2 + 15)
    print(get_duration(start))
    """
    seconds = time.time() - start
    minutes = seconds // 60
    hours = minutes // 60
    # print('hours: {}'.format(hours))
    if hours > 1:
        return str("%d hours %d min. %d sec." % (hours, minutes % 60, seconds % 60))
    if hours > 0:
        return str("%d hour %d min. %d sec." % (hours, minutes % 60, seconds % 60))
    if minutes > 0:
        return str("%d min. %d sec." % (minutes, seconds % 60))
    return str("%d sec." % (seconds))


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    logging.debug("Start Query %s", req)
    start = time.time()
    logging.info('run..........')

    # password: str = ""
    # with open("/var/openfaas/secrets/secret-name") as f:
    #     password = f.read()

    # TODO: remove next line
    time.sleep(10)  # Sleeping for ten second

    logging.debug(
        "Query completed. Total time taken %s", get_duration(start)
    )

    return req
