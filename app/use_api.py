import requests

test_file = {"input": open("../data/test.csv", "rb")}

endpoint = "predict"
# endpoint = "predict_streaming"

r = requests.post(f"http://127.0.0.1:8000/{endpoint}", files=test_file)

print(r.headers)
print(r.text)
