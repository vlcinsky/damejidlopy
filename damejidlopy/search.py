import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait


def createdriver():
    """Creates driver """
    print("Getting everything ready...")
    print()
    options = Options()
    # options.headless = True
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(options=options)
    driver.get("https://damejidlo.cz")
    return driver


def search(customer):
    """Searches every restaurant in the area and prints info about it
    Arguments:
        customer(Customer): Customer object with info about customer
    Return:
        restau(list): List of clickable links ID
        driver: Driver of the website"""
    num = 1
    restau = []
    driver = createdriver()
    textbox = driver.find_element_by_class_name("NewAddress__input")
    textbox.send_keys(customer.address)
    textbox.send_keys(Keys.ENTER)
    try:
        WebDriverWait(driver, 5).until(
            lambda x: x.find_element_by_class_name("Restaurant-list")
        )
    except selenium.common.exceptions.TimeoutException:
        print("No restaurants are opened at this address")
        return
    page = BeautifulSoup(driver.page_source, "lxml")
    restaurace = page.find("div", class_="Restaurant-list")

    def find_info(iterator, plus: bool):
        nonlocal num
        """Finds info about restaurant and prints it
        Arguments:
            iterator(bs4.element.Tag): Code of one restaurant box,
            plus(bool): If the restaurant is in Dáme Jídlo +
        """
        price = iterator.find(
            "span", class_="RestaurantDeliveryInfo__price"
        ).text.strip()
        tiime = iterator.find(
            "span", class_="RestaurantDeliveryInfo__time"
        ).text.strip()
        try:
            count = iterator.find(
                "span", class_="RestaurantRating__rating-count"
            ).text.strip()
            if count == "Nehodnocena":
                rating = "?"
            else:
                rating = iterator.find(
                    "span", class_="RestaurantRating__info"
                ).text.strip()
        except AttributeError:
            rating = "Not specified"
            count = "Not specified"
        if plus:
            print("Dáme jídlo +")
        print(f"{num}. {iterator.find('h2', 'Restaurant__title').text.strip()}")
        print(iterator.find("div", class_="Restaurant__ingredients").text.strip())
        print(f"Shipping: {price} do {tiime}")
        print(iterator.find("div", class_="RestaurantDeliveryInfo__order").text.strip())
        print(f"Rating: {rating}, {count}")
        print("-" * 20)
        num += 1
        restau.append(iterator.get_attribute_list("data-id")[0])

    for restaurant in restaurace.find_all("a", class_="Restaurant Restaurant-box"):
        find_info(restaurant, False)

    for restaurant in restaurace.find_all(
        "a", class_="Restaurant Restaurant-box Restaurant--djPlus"
    ):
        find_info(restaurant, True)

    return restau, driver
