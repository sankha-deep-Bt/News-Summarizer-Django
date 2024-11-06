import os
from dotenv import load_dotenv
from newsapi import NewsApiClient
from django.shortcuts import render
from textblob import TextBlob
# from textblob import download_corpora
from newspaper import Article
from urllib.parse import urlparse, unquote
import validators
import requests
import nltk

load_dotenv() #using dotenv
# # Create your views here.
# def index(request):
#     newsApi = NewsApiClient(api_key=os.getenv('api_key')) 
#     articles = []
#     # download_corpora()
#     # newsApi = NewsApiClient(api_key="Your_Api_key")

#     for page in range(1, 6): 
#         headLines = newsApi.get_top_headlines(page=page, page_size=20) 
#         articles.extend(headLines.get('articles', []))

#     # articles = headLines['articles']
#     desc = []
#     news = []
#     img = []
#     url = []

#     for i in range(len(articles)):
#         if articles[i]['description'] is not None:
#             desc.append(articles[i]['description'])
#             news.append(articles[i]['title'])
#             print(articles[i]['title'])
#             img.append(articles[i]['urlToImage'])
#             url.append(articles[i]['url'])
#     mylist = zip(news, desc, img,url)

#     return render(request, 'main/index.html', context={"mylist": mylist})




def index(request):
    newsApi = NewsApiClient(api_key=os.getenv('api_key'))
    # headLines = newsApi.get_top_headlines()
    # articles = headLines.get('articles', [])
    s = '[Removed]'

    articles = []

    for page in range(1, 6): 
        headLines = newsApi.get_top_headlines(page=page, page_size=20) 
        articles.extend(headLines.get('articles', []))

    # print("Total articles fetched:", len(articles))  # Debugging line

    desc = []
    news = []
    img = []
    url = []

    for article in articles:
        title = article.get('title')
        description = article.get('description')
        image = article.get('urlToImage')
        link = article.get('url')

        # Add debugging output to check each attribute
        # print("Title:", title)
        # print("Description:", description)
        # print("Image:", image)
        # print("URL:", link)

        if all([description, title, link]) and description or title is not s:
            desc.append(description)
            news.append(title)
            img.append(image)
            url.append(link)

    # print("Total valid articles:", len(desc))  # Debugging line

    mylist = zip(news, desc, img, url)
    return render(request, 'main/index.html', context={"mylist": mylist})





def get_website_name(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    if domain.startswith("www."):
        domain = domain[4:]
    return domain

def ArticleDetail(request):
        nltk.download('punkt_tab') 
        url = request.POST.get('url')
        # download_corpora() #run this once
        # print(f"URL parameter: {url}") 
        if not url:
            return render(request, 'main/article.html', {'error': 'URL parameter is missing'})

        url = unquote(url)
        if not validators.url(url):
            return render(request, 'main/article.html', {'error': 'Invalid URL'})

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException:
            return render(request, 'main/article.html', {'error': 'Failed to download the content of the URL'})

        article = Article(url)
        article.download()
        article.parse()
        article.nlp()

        title = article.title
        authors = ', '.join(article.authors)
        if not authors:
            authors = get_website_name(url)
        publish_date = article.publish_date.strftime('%B %d, %Y') if article.publish_date else "N/A"

        article_text = article.text
        sentences = article_text.split('.')
        max_summarized_sentences = 5
        summary = '.'.join(sentences[:max_summarized_sentences])

        top_image = article.top_image

        analysis = TextBlob(article.text)
        polarity = analysis.sentiment.polarity

        if polarity > 0:
            sentiment = 'happy 😊'
        elif polarity < 0:
            sentiment = 'sad 😟'
        else:
            sentiment = 'neutral 😐'

        context = {
            'title': title,
            'authors': authors,
            'publish_date': publish_date,
            'summary': summary,
            'top_image': top_image,
            'sentiment': sentiment,
            'url': url
        }
        return render(request, 'main/article.html', context)



def search_news(request):
    query = request.GET.get('query')
    articles = []

    if query:
        url = f'https://newsapi.org/v2/everything?q={query}&apiKey={os.getenv("api_key")}'
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            raw_articles = data.get('articles', [])
            # Filter out articles with missing essential information
            articles = [
                article for article in raw_articles
                if article.get('title') and article.get('description') and article.get('url') and article.get('urlToImage')
            ]
        else:
            print(f"Error: {data.get('message')}")

    return render(request, 'main/search_results.html', {'articles': articles})