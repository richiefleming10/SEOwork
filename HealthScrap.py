from bs4 import BeautifulSoup
import requests
import openai
openai.api_key = 


def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role":"user","content":prompt}]
    )
    return response.choices[0].message.content.strip()
class Scrape:
    def __init__(self,url):
        self.url = url

    def get_titles(self):
        html = requests.get(self.url).text
        soup = BeautifulSoup(html, features="lxml")
        self.data = []
        for link in soup.find_all("span")[60:87]:
            self.data.append(link.text)
        return self.data

    def get_keywords(self, data):
        three_keys = []
        for i in data: 
            words = chat_with_gpt(f"Find the three most important keywords for SEO in this title: {i}")
            three_keys.append(words)
        return three_keys

link = 'https://www.cnn.com/health/life-but-better/fitness'
scrap = Scrape(link)
data = scrap.get_titles()
# print(data)
keywords = scrap.get_keywords(data)
print(keywords)




