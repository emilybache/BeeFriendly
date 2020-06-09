import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


def run_selenium():
    delay = float(os.getenv("USECASE_REPLAY_DELAY", "0"))
    options = webdriver.ChromeOptions()
    if delay:
        options.add_argument("--start-maximized")
    else:
        options.add_argument("headless")

    d = options.to_capabilities()
    d['loggingPrefs'] = {"browser": "ALL"}

    driver = webdriver.Chrome(desired_capabilities=d)
    driver.get("http://localhost:8080/")

    print_html_page(driver, "start_page")

    do_use_case(driver)

    print_html_page(driver, "end_page")

    driver.quit()


def do_use_case(driver):
    garden_selector = Select(driver.find_element_by_id("select-garden-size"))
    garden_selector.select_by_visible_text("Balcony")
    submit_button = driver.find_element_by_id("submit-garden-quizz")
    submit_button.click()


def print_html_page(driver, page_name):
    html = driver.page_source
    with open(f"{page_name}.html", "w", encoding="utf-8") as f:
        f.write(html)


def wait_until(condition, driver):
    try:
        return WebDriverWait(driver, 30).until(condition)
    except Exception as e:
        sys.stderr.write(f"Timed out {repr(driver)}\n")
        driver.quit()
        raise


if __name__ == "__main__":
    run_selenium()