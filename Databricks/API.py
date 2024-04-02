import requests, csv 

api_key = "7355bc8e306b4feb8390955f3aad5108"

url = f'https://newsapi.org/v2/everything?q=bitcoin&language=en&sortBy=popularity&apiKey={api_key}'

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data['articles']

        with open('news.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'URL']) 

            for article in articles:
                title = article['title']
                url = article['url']
                writer.writerow([title, url])  
                
        print('Falha ao obter dados:', response.status_code)
except Exception as e:
    print('Erro:', e)



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

