import requests

data = requests.get("https://opentdb.com/api.php?amount=10&category=15&type=boolean").json()
question_data = data['results']
