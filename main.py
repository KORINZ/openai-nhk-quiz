import openai
import chardet
import requests
import random
from bs4 import BeautifulSoup
from datetime import datetime
from openai_key import api_key

openai.api_key = api_key


def get_random_news_url(news_list_url="https://www3.nhk.or.jp/news/easy/top-list.json") -> str:
    """Get a random news url from NHK Easy News."""
    response = requests.get(news_list_url)
    data = response.json()[0:4]
    news_id = data[random.randint(0, 3)]["news_id"]
    news_url = "https://www3.nhk.or.jp/news/easy/" + news_id + "/" + news_id + ".html"
    return news_url


def get_news_article(url: str) -> str:
    """Get the content of the news."""
    response = requests.get(url)
    response.encoding = chardet.detect(response.content)["encoding"]
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find(
        "h1", class_="article-main__title").text.strip()  # type: ignore

    date = soup.find(id="js-article-date").text.split(' ')[0]  # type: ignore
    # Assume the news is from the current year
    date = f"{datetime.now().year}年{date[1:]}"

    content = soup.find(
        id="js-article-body").text.replace("\n", "")  # type: ignore
    return "Title: " + title + "\n" + "Date: " + date + "\n" + "Content: " + content


def main() -> None:
    """Generate a quiz based on a random news article with chatGPT api."""
    news_url = get_random_news_url()
    news_content = get_news_article(news_url)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
                "content": "You are a helpful assistant who creates a multiple-choice reading comprehension quiz for JLPT N2 level students based on a given news article prompted by the user. (2 questions in Japanese, 3 choices each)"},
            {"role": "user", "content": news_content},
            # {"role": "user", "content": "Also provide the answer to the question and 3 important vocabularies in the news article."},
        ],
        temperature=0,
    )

    quiz = response['choices'][0]['message']['content']  # type: ignore
    print(news_url, end="\n\n")
    print(news_content, end="\n\n")
    print(quiz)


if __name__ == "__main__":
    main()
