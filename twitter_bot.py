import requests
import bs4
import os
from twikit import Client
from dotenv import load_dotenv, find_dotenv

def main():
    load_dotenv(find_dotenv())

    #Grab the number 1 top ranked word
    url = "https://dictionary.goo.ne.jp/jn/"
    res = requests.get(url)
    res.raise_for_status()
    word_soup = bs4.BeautifulSoup(res.text, 'html.parser')
    jp_select = word_soup.select("#search-rank-main-0 > div:nth-child(1) > ol:nth-child(1) > li:nth-child(1) > a:nth-child(1) > ul:nth-child(1) > li:nth-child(2)")
    word = jp_select[0].string



    #Fetch definition

    url = f'https://dictionary.goo.ne.jp/word/{word}/'
    res = requests.get(url)
    res.raise_for_status()
    wordSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    jp_text = wordSoup.select('.text')

    definition = ''

    for element in jp_text:
        definition += element.text

    USERNAME = os.environ['USERNAMEV']
    EMAIL = os.environ['EMAILV']
    PASSWORD = os.environ['PASSWORDV']

    # Initialize client
    client = Client('en-US')

    # Login to the service with provided user credentials
    """
    client.login(
        auth_info_1=USERNAME ,
        auth_info_2=EMAIL,
        password=PASSWORD
    )
    """

    #client.save_cookies('cookies.json')
    client.load_cookies("/home/vboxuser/repos/twitterbot/cookies.json")

    client.create_tweet(
        text=f"今日の日本語 「{word}」\n - {definition}"
    )

if __name__ == "__main__":
    main()
