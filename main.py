from Product import Product
from bs4 import BeautifulSoup
from selenium import webdriver

def start():

    try:
        chrome = webdriver.Chrome("./chromedriver")
        chrome.get("https://www.amazon.com.br/")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    start()