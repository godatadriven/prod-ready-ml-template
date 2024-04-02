import requests

test_file = {"input" : open("../data/test.csv", "rb")}

r = requests.post("http://127.0.0.1:8000/predict", files=test_file)

print(r.text)
