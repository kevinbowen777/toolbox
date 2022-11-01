#!/bin/sh env python
# /home/kbowen/.pyenv/shims/python
# https://realpython.com/python-sleep/

import time

from urllib import error, request


def sleep(timeout, retry=3):
    def the_real_decorator(function):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < retry:
                try:
                    value = function(*args, **kwargs)
                    if value is None:
                        return
                except:
                    print(f"Sleeping for {timeout} seconds")
                    time.sleep(timeout)
                    retries += 1

        return wrapper

    return the_real_decorator


@sleep(3)
def uptime_bot(url):
    try:
        conn = request.urlopen(url)
    except error.HTTPError as e:
        # Email admin / log
        print(f"HTTPError: {e.code} for {url}")
        # Re-raise exception for the decorator
        raise error.HTTPError
    except error.URLError as e:
        # Email admin / log
        print(f"URLError: {e.code} for {url}")
        # Re-raise exception for the decorator
        raise error.URLError
    else:
        # Website is up
        print(f"{url} is up")


if __name__ == "__main__":
    # url = 'http://www.google.com/'
    url = "http://www.google.com/py"
    uptime_bot(url)
