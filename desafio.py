import requests
import json 

request = requests.get("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=2ae5e3690db0365ecd95002ff8bd8b8905303e96")
jaison_3 = request.json()
jaison_2 = json.dumps(jaison_3)
jaison_1 = json.loads(jaison_2)

with open('answer.json','w') as f:
	json.dump(jaison_1, f)









