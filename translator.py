import requests

class Translator:


    def __init__(self):

        self.url = "https://rapid-translate-multi-traduction.p.rapidapi.com/t"
	
	file = open("API_KEY.txt")
	
        self.headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": file.read(),
            "X-RapidAPI-Host": "rapid-translate-multi-traduction.p.rapidapi.com"
        }

    def translate(self, string):
        

        payload = {
            "from": "ml",
            "to": "en",
            "e": "",
            "q": string
        }

        response = requests.request("POST", self.url, json=payload, headers=self.headers)

        return response.text

# obj = Translator()
# print(obj.translate('മലയാളത്തിൽ ടൈപ്പ്)'))
