from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains  # Hover
import time
import unittest
import json

# Initialize the WebDriver (example using Chrome)
# driver = webdriver.Chrome()

# # Navigate to the webpage
# driver.get("https://storecs.vercel.app/")

# # Locate the main menu item
# main_menu_item = driver.find_element(
#     By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li.sub-menu > a")

# # Initialize ActionChains
# actions = ActionChains(driver)

# # Hover over the main menu item
# actions.move_to_element(main_menu_item).perform()

# # Wait for the sub-menu to be displayed (implicit wait can be used, or WebDriverWait)
# driver.implicitly_wait(10)

# # Locate the sub-menu item
# sub_menu_item = driver.find_element(
#     By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li.sub-menu > ul > li:nth-child(1) > a")

# Click the sub-menu item
# actions.move_to_element(sub_menu_item).click().perform()

# Perform any further actions if needed

# Close the WebDriver
# driver.quit()


class TestRegisterFunction(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://storecs.vercel.app/')

    def tearDown(self):
        self.driver.quit()

    # Happy Cases
    # TC_44
    def test44(self):
        main_menu_item = self.driver.find_element(
            By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li.sub-menu > a")
        actions = ActionChains(self.driver)
        actions.move_to_element(main_menu_item).perform()
        self.driver.implicitly_wait(10)
        sub_menu_item = self.driver.find_element(
            By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li.sub-menu > ul > li:nth-child(1) > a")
        actions.move_to_element(sub_menu_item).click().perform()
        time.sleep(5)

        product_items = self.driver.find_elements(
            By.CLASS_NAME, 'product-item')

        # In thông tin về từng sản phẩm tương ứng với filter khách chọn
        for product in product_items:
            title = product.find_element(By.CLASS_NAME, 'inner-title').text
            price_new = product.find_element(
                By.CLASS_NAME, 'inner-price-new').text
            price_old = product.find_element(
                By.CLASS_NAME, 'inner-price-old').text
            discount = product.find_element(
                By.CLASS_NAME, 'inner-discount').text
            print(
                f"Title: {title}, New Price: {price_new}, Old Price: {price_old}, Discount: {discount}")

    # TC_45
    def test45(self):
        main_menu_item = self.driver.find_element(
            By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li.sub-menu > a")
        actions = ActionChains(self.driver)
        actions.move_to_element(main_menu_item).perform()
        self.driver.implicitly_wait(10)
        sub_menu_item = self.driver.find_element(
            By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li.sub-menu > ul > li:nth-child(2) > a")
        actions.move_to_element(sub_menu_item).click().perform()
        time.sleep(5)

        product_items = self.driver.find_elements(
            By.CLASS_NAME, 'product-item')

        # In thông tin về từng sản phẩm tương ứng với filter khách chọn
        for product in product_items:
            title = product.find_element(By.CLASS_NAME, 'inner-title').text
            price_new = product.find_element(
                By.CLASS_NAME, 'inner-price-new').text
            price_old = product.find_element(
                By.CLASS_NAME, 'inner-price-old').text
            discount = product.find_element(
                By.CLASS_NAME, 'inner-discount').text
            print(
                f"Title: {title}, New Price: {price_new}, Old Price: {price_old}, Discount: {discount}")


if __name__ == "__main__":
    unittest.main()
