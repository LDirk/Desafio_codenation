import requests
import json 
import hashlib 


#Resumo crypto 
with open("answer.json","r") as f:
	data = json.load(f)
	encoding = f.encoding 

resumo = hashlib.sha1(data["decifrado"].encode(encoding)).hexdigest()
print(resumo)

#Escrevendo no json 
with open("answer.json","r+") as f:
	data = json.load(f)
	data["resumo_criptografico"] = resumo
	f.seek(0) #remove remaining part
	json.dump(data, f, indent = 4)

#Enviando ? 
POST = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=2ae5e3690db0365ecd95002ff8bd8b8905303e96"
answer = {'answer': open("answer.json", 'rb')}
submit = requests.post(POST, files = answer)
print(submit.text)




"""
with open("answer.json","r") as f:
	data_json = json.load(f)

resposta = requests.post("https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=2ae5e3690db0365ecd95002ff8bd8b8905303e96", data = data_json)
"""