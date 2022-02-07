import requests


poison_data = {"id": "3403", "holdthedoor":"submit"}


for i in range(0, 1024):
    requests.post("http://158.69.76.135/level0.php", data=poison_data)
    print(i + 1)
    
