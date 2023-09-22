from django.shortcuts import render
import requests

def index(request):
    url = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=d77f259c77d04d49ab955da521cb1afe'
    crypto_news = requests.get(url).json()
    articles = crypto_news.get('articles', [])  # Use .get() to handle missing 'articles' key

    # Initialize empty lists
    title = []
    desc = []
    img = []

    for article in articles:
        title.append(article.get('title', ''))
        desc.append(article.get('description', ''))
        img.append(article.get('urlToImage', ''))

    mylist = list(zip(title, desc, img))  # Convert zip to list

    context = {'mylist': mylist}
    return render(request, 'index.html', context)

