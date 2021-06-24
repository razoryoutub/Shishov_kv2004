import requests
spisok_valut = [
	'https://www.google.com/search?q=USD',
	'https://www.google.com/search?q=EUR',
	'https://www.google.com/search?q=GBP',
	'https://www.google.com/search?q=AUD',
	'https://www.google.com/search?q=JPY',
]

for link in spisok_valut:
	r = requests.get(link)
	answer = str(r.content).split()[list((str(r.content).split())).index('iBp4i') + 4]
	print(answer[8:].replace(',', '.'))
