import requests
from bs4 import BeautifulSoup

def code_guardian(query):
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('div', class_='tF2Cxc')
    
    answers = []
    for result in results:
        answer = result.find('div', class_='BNeawe vvjwJb')
        if answer:
            answer = answer.text
            answers.append(answer)
    
    return answers
