import requests
import json

url = "https://www.baidu.com/"
re = requests.get(url)

print(re.text)
