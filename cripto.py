import json
criptografia = []
linguagem_normal = []


for i in range(ord('a'), ord('z')+1):
	criptografia.append(chr(i))

criptografia.append(".")
criptografia.append(" ")


print(criptografia)
print()
"""
for i in range(ord('e'),ord('z')+1):
	linguagem_normal.append(chr(i))

for i in range(ord("a"),ord('d')+1):
	linguagem_normal.append(chr(i))

linguagem_normal.append(".")	
linguagem_normal.append(" ")	


print(linguagem_normal)
print() 

"""

for i in range(ord("w"),ord('z')+1):
	linguagem_normal.append(chr(i))
for i in range(ord("a"),ord("v")+1):
	linguagem_normal.append(chr(i))
linguagem_normal.append(".")	
linguagem_normal.append(" ")	



with open('answer.json','r') as f:
	data = json.load(f)


#Pegando o codigo cifrado
cifrado = []
for letra in data['cifrado']:
	cifrado.append(letra)

print(cifrado)

#Decifrando

decifrado = []

for elemento1 in cifrado:
	for elemento2 in criptografia:
		if elemento1 == elemento2:
			for i in range(0,len(criptografia),1):
				if elemento1 == criptografia[i]:
					decifrado.append(linguagem_normal[i])
print()

print(decifrado)
print()

#Transformar decifrado em uma "palavra" para escrever 
decifrado_str = '!'

for elemento in decifrado:
	decifrado_str = decifrado_str + elemento

decifrado_str = decifrado_str.strip('!')
print(decifrado_str)

#Escrevendo a decifrado_str no answer.json:

with open("answer.json","r+") as f:
	data = json.load(f)
	data["decifrado"] = decifrado_str
	f.seek(0) #remove remaining part
	json.dump(data, f, indent = 4)






