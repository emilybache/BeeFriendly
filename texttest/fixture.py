import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def run_selenium():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8080/")

    print_html_page(driver, "start_page")

    dropdown = driver.find_element(By.CSS_SELECTOR, "select")
    dropdown.find_element(By.XPATH, "//option[. = 'Balcony']").click()
    driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .btn").click()

    print_html_page(driver, "end_page")

    driver.quit()


def print_html_page(driver, page_name):
    html = driver.page_source
    with open(f"{page_name}.html", "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    run_selenium()