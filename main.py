from Product import Product
from bs4 import BeautifulSoup
from selenium import webdriver


def start():

    try:

        driver = webdriver.Chrome("./chromedriver")
        driver.get("https://www.amazon.com.br/")
        driver.find_element_by_xpath("//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers']").click()
        driver.find_element_by_link_text('Ver mais Mais Vendidos em Games e Consoles').click()
        data = driver.find_elements_by_class_name('a-link-normal')
        links = []

        for value in data[:10]:
            links.append(value.get_attribute('href'))

        all_products = []

        for link in links:
            driver.get(link)
            html = driver.find_element_by_tag_name('body')
            html = html.get_attribute('innerHTML')

            soup = BeautifulSoup(html, 'html.parser')
            product_name = soup.find_all("span", {"class": 'a-size-large product-title-word-break'})[0].get_text()
            product_price = soup.find_all("span", {"class": 'a-size-medium a-color-price priceBlockBuyingPriceString'})[0].get_text()

            product_name = product_name.strip()
            product_price = product_price.strip()

            product = Product(product_name, product_price)
            all_products.append(product)

        with open("products.txt", mode='w') as file:
            for product in all_products:
                file.write("%s\n" % product)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    start()
