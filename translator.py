import requests

class Translator:


    def __init__(self):

        self.url = "https://rapid-translate-multi-traduction.p.rapidapi.com/t"

        self.headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "e305f608a8msha9fd8fddbcfc877p12bfb1jsnb78ed1c9306a",
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