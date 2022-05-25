from django.shortcuts import render
from django.views import View
from django.http import Http404
import json
import datetime
import random
from django.shortcuts import redirect


# Create your views here.

def get_links(old_links):
    new_links = old_links
    return new_links


def redirect_m(request):
    return redirect('/news/')


class MainPageView(View):
    def get(self, request, *args, **kwargs):
        search_info = request.GET.get('q')
        with open("C:\\Users\\User\\PycharmProjects\\HyperNews Portal\\HyperNews Portal\\task\\hypernews\\news.json",
                  "r") as json_file:
            news = json.load(json_file)
        links = [i['link'] for i in news]
        if search_info is None or search_info == "":
            new_news = news
        else:
            new_news = []
            for i in news:
                if search_info in i['title']:
                    new_news.append(i)
        return render(request, 'news/index.html', {'news': new_news, 'links': links})


class ArticlePageView(View):
    def get(self, request, number_of_link, *args, **kwargs):
        with open("C:\\Users\\User\\PycharmProjects\\HyperNews Portal\\HyperNews Portal\\task\\hypernews\\news.json",
                  "r") as json_file:
            news = json.load(json_file)
        links = [i['link'] for i in news]

        if int(number_of_link) not in links:
            raise Http404
        article = None
        for art in news:
            if art['link'] == int(number_of_link):
                article = art
        return render(request, 'news/article.html', {'article': article})


class CreateArticle(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'news/create_article.html')

    def post(self, request, *args, **kwargs):
        with open("C:\\Users\\User\\PycharmProjects\\HyperNews Portal\\HyperNews Portal\\task\\hypernews\\news.json",
                  "r") as json_file:
            news = json.load(json_file)
        links = [i['link'] for i in news]

        title = request.POST.get('title')
        text = request.POST.get('text')
        date_and_time = datetime.datetime.now()
        created = str(date_and_time.replace(microsecond=0))
        while True:
            new_link = random.randrange(0, 101)
            if new_link in links:
                continue
            else:
                break
        link = new_link
        new_article = {"created": created, "text": text, "title": title, "link": link}
        news.append(new_article)
        with open("C:\\Users\\User\\PycharmProjects\\HyperNews Portal\\HyperNews Portal\\task\\hypernews\\news.json",
                  "w") as json_new_file:
            json.dump(news, json_new_file)
        return redirect('/news/')
