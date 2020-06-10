import os
import sys

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def setup(url):
    global driver, orig_url
    orig_url = url

    delay = float(os.getenv("USECASE_REPLAY_DELAY", "0"))
    options = webdriver.ChromeOptions()
    if delay:
        options.add_argument("--start-maximized")
    else:
        options.add_argument("headless")

    d = options.to_capabilities()
    d['loggingPrefs'] = {"browser": "ALL"}

    driver = webdriver.Chrome(desired_capabilities=d)
    driver.get(url)


def print_html_page(page_name):
    html = driver.page_source
    with open(f"{page_name}.html", "w", encoding="utf-8") as f:
        f.write(html)


def wait_until(condition):
    try:
        return WebDriverWait(driver, 30).until(condition)
    except Exception as e:
        sys.stderr.write(f"Timed out {repr(driver)}\n")
        driver.quit()
        raise


def select_garden_size(size):
    garden_selector = Select(driver.find_element_by_id("select-garden-size"))
    garden_selector.select_by_visible_text(size)


def submit_garden_quizz():
    submit_button = driver.find_element_by_id("submit-garden-quizz")
    submit_button.click()


def select_flowers(flowers):
    for flower in flowers:
        checkbox_selector = driver.find_element_by_id(f"checkbox_{flower}")
        checkbox_selector.click()


def close():
    driver.quit()
