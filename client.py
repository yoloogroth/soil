import requests
body = {
    "lat":64,
    "lon":1,
    "elevation":3,
    "slope1":120,
    "slope2":150
    }
response = requests.post(url = 'http://127.0.0.1:8000/score',
              json = body)
print (response.json())
# output: {'score': 0.866490130600765ÇÇ
