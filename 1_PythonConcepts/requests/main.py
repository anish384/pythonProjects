# website: https://httpbin.org/

import requests

payload = {
    "name": "Mike",
    "age": 21
}

response = requests.post("https://httpbin.org/post", data=payload)

# print(response.status_code)
print(response.url)
print(response.text)

