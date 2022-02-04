import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import math


link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    price = WebDriverWait(browser, 15).until(
        expected_conditions.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), "100")
    )
    browser.find_element(By.XPATH, "//button[@id='book']").click()
    x = browser.find_element(By.XPATH, "//span[@id='input_value']").text
    browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(str(math.log(abs(12*math.sin(int(x))))))

    browser.find_element(By.XPATH, "//button[@id='solve']").click()
    print(browser.switch_to.alert.text)
finally:
    time.sleep(3)
    browser.quit()
