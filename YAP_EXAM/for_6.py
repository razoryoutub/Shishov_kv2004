import requests
spisok_valut = [
	'https://www.google.com/search?q=usd&rlz=1C1CHZN_ruRU956RU956&oq=USD&aqs=chrome.0.69i59j0i433l2j0l5j0i433j0.890j0j7&sourceid=chrome&ie=UTF-8',
	'https://www.google.com/search?q=EUR&newwindow=1&rlz=1C1CHZN_ruRU956RU956&sxsrf=ALeKk01fPgA-IlQt-dGn-obDbD9IXrKjEA%3A1624476746569&ei=SozTYMiOIuTnrgT_p4zoBg&oq=EUR&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBwgAELEDEEMyBwgAELEDEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEM6AggAOgUIABCxA0oECEEYAFCT9m1Y8PxtYOv_bWgAcAJ4AIABVYgBsQKSAQE0mAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=gws-wiz&ved=0ahUKEwjI27K7v67xAhXks4sKHf8TA20Q4dUDCBE&uact=5',
	'https://www.google.com/search?q=GBP&newwindow=1&rlz=1C1CHZN_ruRU956RU956&sxsrf=ALeKk03e7B_vZSY3kqz9FfpFbWxf5UUPYQ%3A1624478805359&ei=VZTTYNqMFbDrrgTp3YDYCA&oq=GBP&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgAEEMyBwgAEIcCEBQyAggAMgIIADIFCAAQsQMyAggAMgIIADIGCC4QChABMgIIADoHCAAQRxCwA0oECEEYAFDGNFjGNGCCN2gBcAJ4AIABUYgBiAGSAQEymAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=gws-wiz&ved=0ahUKEwiai42Rx67xAhWwtYsKHekuAIsQ4dUDCBE&uact=5',
	'https://www.google.com/search?q=AUD&newwindow=1&rlz=1C1CHZN_ruRU956RU956&sxsrf=ALeKk01AzqRHe_P3rG2gRjM6ODUp5pBQoQ%3A1624478813425&ei=XZTTYPy0GceMrwSHoZHQCw&oq=AUD&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyCwguELEDEMcBEKMCMgQIABBDMgQIABBDMgQIABBDMgUIABCxAzIFCAAQsQMyBQgAELEDMgUIABCxAzIFCAAQsQM6AggAOgcIABCxAxBDOgQILhBDOg0ILhCxAxDHARCjAhBDSgQIQRgAUKnzDliz9Q5ghvwOaABwAngAgAFfiAGsApIBATSYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=gws-wiz&ved=0ahUKEwi81_mUx67xAhVHxosKHYdQBLoQ4dUDCBE&uact=5',
	'https://www.google.com/search?q=JPY&newwindow=1&rlz=1C1CHZN_ruRU956RU956&sxsrf=ALeKk00Mpz2T3OBButFXRmfZi_y1O0HxNA%3A1624479059562&ei=U5XTYM7oIezHrgS65ruQDQ&oq=JPY&gs_lcp=Cgdnd3Mtd2l6EAMyCQgjECcQRhCCAjIHCAAQhwIQFDICCAAyAggAMgIIADICCAAyAggAMgIIADIGCAAQChABMgIIADoECCMQJzoFCAAQsQM6CAguEMcBEKMCOgUILhCxAzoLCC4QsQMQxwEQowI6CAguEMcBEK8BSgQIQRgAUKihAVjsqAFg8a4BaABwAngAgAFViAGyApIBATSYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=gws-wiz&ved=0ahUKEwiO3qiKyK7xAhXso4sKHTrzDtIQ4dUDCBE&uact=5',
]

for link in spisok_valut:
	r = requests.get(link)
	answer = str(r.content).split()[list((str(r.content).split())).index('iBp4i') + 4]
	print(answer[8:])
