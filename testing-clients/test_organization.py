import requests
import time

# try to make requests 60 requests in a minute
token = '29815c6015558e80c6c4965f4d0b19e0f7a29d5e'
#token = '76b403de09e2de17680b45da8532ef80e91e8d20'
#token = 'faljd21423'
start = time.time()

headers = {'content-type': 'application/json', 'Authorization': 'Token ' + token}
while time.time() - start <= 100:
    response = requests.get('http://127.0.0.1:8000/api/v1/organization/', headers=headers)
    print(response)
    print(response.json())
    time.sleep(1)
