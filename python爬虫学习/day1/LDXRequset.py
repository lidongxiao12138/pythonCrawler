import requests
import datetime

class LDXRequset():
    def get(url, header, data):
        response = requests.get(url=url, headers=header, data=data).text
        return response

    def post(url, header, data):
        response = requests.post(url=url, headers=header, data=data).text
        return response

    def nowTime():
        now = datetime.datetime.now()
        timestamp = now.timestamp()
        return timestamp
    
    
