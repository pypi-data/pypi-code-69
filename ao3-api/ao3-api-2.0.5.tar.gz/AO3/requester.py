import time

import requests


CUSTOM_USERAGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"


class Requester:
    """Requester object"""
    
    def __init__(self, rqtw=-1, timew=400):
        """Limits the request rate to prevent HTTP 429 (rate limiting) responses

        Args:
            rqm (int, optional): Maximum requests per time window (-1 -> no limit). Defaults to -1.
            timew (int, optional): Time window (seconds). Defaults to 400.
        """
        
        self._requests = []
        self._rqtw = rqtw
        self._timew = timew
        self.total = 0
        
    def setRQTW(self, value):
        self._rqtw = value
        
    def setTimeW(self, value):
        self._timew = value

    def request(self, *args, **kwargs):
        """Requests a web page once enough time has passed since the last request
        
        Args:
            session(requests.Session, optional): Session object to request with

        Returns:
            requests.Response: Response object
        """
        
        # We've made a bunch of requests, time to rate limit?
        if self._rqtw != -1 and len(self._requests) >= self._rqtw:
            t = time.time()
            # Reduce list to only requests made within the current time window
            while len(self._requests):
                if t-self._requests[0] >= self._timew:
                    self._requests.pop(0) # Older than window, forget about it
                else:
                    break # Inside window, the rest of them must be too
            # Have we used up all available requests within our window?
            if len(self._requests) >= self._rqtw: # Yes
                # Wait until the oldest request exits the window, giving us a slot for the new one
                time.sleep(self._requests[0] + self._timew - t)
                # Now outside window, drop it
                self._requests.pop(0)
                    
        if "headers" not in kwargs:
            kwargs["headers"] = {"User-Agent": CUSTOM_USERAGENT}
        else:
            kwargs["headers"]["User-Agent"] = CUSTOM_USERAGENT           
        if "session" in kwargs:
            sess = kwargs["session"]
            del kwargs["session"]
            req = sess.request(*args, **kwargs)
        else:
            req = requests.request(*args, **kwargs)
        if self._rqtw != -1:
            self._requests.append(time.time())
        self.total += 1
        return req

requester = Requester()