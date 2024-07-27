import requests
from bs4 import BeautifulSoup

# URL du site web d'offres d'emploi

def main():
    url = 'https://www.emploitogo.info/'

    # Envoyer une requête HTTP pour obtenir la page web
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Exemple de scraping des données d'un site
    jobs = []
    for job_element in soup.find_all('h3', class_='entry-title'):
        title = job_element.find('a')['title']
        # location = job_element.find('span', class_='location').text.strip()
        # description = job_element.find('div', class_='description').text.strip()
        
        # job = {
        #     'title': title,
        #     'location': location,
        #     'description': description
        # }
        # jobs.append(job)
        print(title)
    # Afficher les offres d'emploi récupérées
    # for job in jobs:
    #     print(f"Title: {job['title']}")
    #     print(f"Location: {job['location']}")
    #     print(f"Description: {job['description']}\n")


if __name__ == "__main__":
    main()