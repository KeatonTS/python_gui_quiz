import requests

data = requests.get("https://opentdb.com/api.php?amount=10&category=15&type=boolean", timeout=60).json(timeout=60)
question_data = data['results']
