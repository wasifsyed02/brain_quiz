import requests
res=requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
res.raise_for_status()
res.json()
question_data = res.json()["results"]

