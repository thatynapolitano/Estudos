import requests
import csv 

api_key = "7355bc8e306b4feb8390955f3aad5108"

url = f'https://newsapi.org/v2/everything?q=bitcoin&language=en&sortBy=popularity&apiKey={api_key}'

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data['articles']
        status = data['status']
        totalResults = data['totalResults']

        with open('news.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['ID','Name', 'Author', 'Title', 'Description', 'URL', 'urlToImage', 'Status', 'TotalResults']) 

            for article in articles:
                id = article.get('id', '') 
                name = article.get('source', {}).get('name', '')
                author = article.get('author', '')
                title = article.get('title', '')
                description = article.get('description', '')
                url = article.get('url', '')
                urlToImage = article.get('urlToImage', '')

                writer.writerow([id,name,author,title,description,url,urlToImage, status, totalResults])  

    else:
        print('Falha ao obter dados:', response.status_code)
except:
    print('Erro')



# try:
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         articles = data['articles']

#         for article in articles:
#             print(article['title'])
#     else:
#         print('Falha ao obter dados:', response.status_code)
# except Exception:
#     print('Erro:', Exception)

