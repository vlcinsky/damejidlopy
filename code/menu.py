from selenium import webdriver
import selenium
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup


def menu(searched, restaurant):
    cislo = 1
    _id, driver = searched
    button = driver.find_element_by_xpath(f"//a[@data-id='{_id[restaurant - 1]}']")
    driver.execute_script("arguments[0].click();", button)
    try:
        WebDriverWait(driver, 5).until(
            lambda x: x.find_element_by_class_name("RestaurantDetailMenuCategory")
        )
    except selenium.common.exceptions.TimeoutException:
        print("Webpage couldn't load")
    page = BeautifulSoup(driver.page_source, "lxml")
    for menicko in page.find_all("div", class_="RestaurantDetailMenuCategory"):
        textik = menicko.find("h2", class_="RestaurantDetailMenuCategory__title")
        title = [
            slovo
            for slovo in textik.text.split()
            if slovo not in textik.find(
                "div", class_="RestaurantDetailMenuCategory__packing"
            ).text.split()
        ]
        title = " ".join(title)
        print(title)
        print("-" * 20)
        for jidlo in menicko.find_all(class_="RestaurantDetailMenuCategory__list"):
            for mensijidlo in jidlo.find_all(class_="Menu-list__item-text"):
                text = mensijidlo.find("a", class_="basketAdd").text.strip().split()
                if text[0][0].isnumeric():
                    text.pop(0)
                text = " ".join(text)
                print(f"""{text}
                """)
            print("-" * 20)
