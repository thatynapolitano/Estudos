# %%
import requests,csv 
from datetime import datetime, timedelta 
# %%

# %%
api_key = "7355bc8e306b4feb8390955f3aad5108"

#url = f'https://newsapi.org/v2/everything?q=bitcoin&language=en&sortBy=popularity&apiKey={api_key}'
url = "https://newsapi.org/v2/everything?q=bitcoin&from=2024-01-01&=to=2024-04-02&language=en&sortBy=popularity&apiKey=7355bc8e306b4feb8390955f3aad5108"
# %%

# %%
try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data['articles']
        status = data['status']
        totalResults = data['totalResults']

        with open('news.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['ID','Name', 'Author', 'Title', 'Description', 'URL', 'urlToImage','publishedAt','content', 'Status', 'TotalResults']) 

            for article in articles:
                id = article.get('source', {}).get('id', '') 
                name = article.get('source', {}).get('name', '')
                author = article.get('author', '')
                title = article.get('title', '')
                description = article.get('description', '')
                url = article.get('url', '')
                urlToImage = article.get('urlToImage', '')
                publishedAt = article.get('publishedAt', '')
                content = article.get('content', '')

                writer.writerow([id, name, author, title, description, url, urlToImage, publishedAt, content, status, totalResults])  

    else:
        print('Falha ao obter dados:', response.status_code)
except Exception as e:
    print('Erro:', e)
# %%
    


    noticias_por_data.to_csv('noticias_por_data.csv', index=False)
    noticias_por_fonte_autor.to_csv('noticias_por_fonte_autor.csv', index=False)
    aparicoes_palavras_chave.to_csv('aparicoes_palavras_chave.csv', index=False)