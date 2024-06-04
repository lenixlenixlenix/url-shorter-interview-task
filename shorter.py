import random
import string
import re

import redis

class Shortener: 

    db = redis.Redis()
    db = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)
    domain_name: str = "http://127.0.0.1:5000"

    def __init__(self) -> None:
        pass
    # implemented 
    def generate_short_code(self):
        short = ""
        for i in range(5):
            short += (random.choice(
                string.ascii_lowercase + string.digits)
            )
        return short
    
    def get_url_from_code(self, code: str) -> str:
        try:  
            result: str = str(self.db.get(code))
        except KeyError:
            result = "No valid short url"
        return result
    
    def put_code_from_url(self, url: str) -> str:
        regex_url = "((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"
        if re.match(regex_url, url):
            code_url = self.generate_short_code()
            self.db.set(code_url, url)
            message = f"{self.domain_name}/{code_url}"
        else:
            message = "Not correct url"
        return message

        

    
