from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
import time
import unittest
import json


class TestRegisterFunction(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://storecs.vercel.app/')

    def tearDown(self):
        self.driver.quit()

    def login(self, username, password):
        self.driver.find_element(
            By.CSS_SELECTOR, 'div > ul > li:nth-child(4) > a').click()
        self.driver.find_element(By.ID, "email").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(
            By.CSS_SELECTOR, "body > div > div > div > form > div:nth-child(3) > button").click()

    # Happy Cases
    # TC_46
    # def test46(self):
    #     with open("Data/add_product_to_cart_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         username = data["test_cases_add_product"][0]["username"]
    #         password = data["test_cases_add_product"][0]["password"]
    #         quantity = data["test_cases_add_product"][0]["quantity"]
    #         self.login(username, password)
    #         success_message_element_login = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-success"))
    #         )
    #         success_message_login = success_message_element_login.text.strip()

    #         print(success_message_login)
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div:nth-child(3) > div > div:nth-child(2) > div:nth-child(1) > div > div.inner-content > h3 > a").click()

    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").clear()

    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").send_keys(quantity)

    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > button").click()

    #         success_message_element = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-success"))
    #         )
    #         success_message = success_message_element.text.strip()
    #         # self.driver.save_screenshot('image/pass/1.jpg')
    #         print(success_message)
    #         self.assertEqual(
    #             success_message, "Đã thêm sản phẩm vào giỏ hàng! x")

    # Negative Cases
    # TC_47
    # def test47(self):
    #     with open("Data/add_product_to_cart_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         username = data["test_cases_add_product"][1]["username"]
    #         password = data["test_cases_add_product"][1]["password"]
    #         quantity = data["test_cases_add_product"][1]["quantity"]
    #         self.login(username, password)
    #         success_message_element_login = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-success"))
    #         )
    #         success_message_login = success_message_element_login.text.strip()

    #         print(success_message_login)
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div:nth-child(3) > div > div:nth-child(2) > div:nth-child(1) > div > div.inner-content > h3 > a").click()

    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").clear()

    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").send_keys(quantity)

    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > button").click()

    #         error_message_element = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-danger"))
    #         )
    #         error_message = error_message_element.text.strip()
    #         # self.driver.save_screenshot('image/pass/1.jpg')
    #         print(error_message)
    #         self.assertEqual(
    #             error_message, "Thêm sản phẩm thất bại x")

    # TC_48
    # def test48(self):
    #     with open("Data/add_product_to_cart_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         username = data["test_cases_add_product"][2]["username"]
    #         password = data["test_cases_add_product"][2]["password"]
    #         quantity = data["test_cases_add_product"][2]["quantity"]
    #         self.login(username, password)
    #         success_message_element_login = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-success"))
    #         )
    #         success_message_login = success_message_element_login.text.strip()

    #         print(success_message_login)
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div:nth-child(3) > div > div:nth-child(2) > div:nth-child(1) > div > div.inner-content > h3 > a").click()

    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").clear()

    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").send_keys(quantity)

    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > button").click()

    #         error_message = self.driver.find_element(
    #             By.CSS_SELECTOR, 'body > div.product-detail > div:nth-child(1) > div > div:nth-child(2) > form > input').get_attribute("validationMessage")
    #         # self.driver.save_screenshot('image/pass/3.jpg')
    #         print(error_message)
    #         self.assertEqual(
    #             error_message, "Value must be greater than or equal to 1.")

    # TC_49
    def test49(self):
        with open("Data/add_product_to_cart_function_data.json", encoding="utf-8") as f:
            data = json.load(f)
            username = data["test_cases_add_product"][3]["username"]
            password = data["test_cases_add_product"][3]["password"]
            quantity = data["test_cases_add_product"][3]["quantity"]
            self.login(username, password)
            success_message_element_login = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "alert-success"))
            )
            success_message_login = success_message_element_login.text.strip()

            print(success_message_login)
            self.driver.find_element(
                By.CSS_SELECTOR, "body > div:nth-child(3) > div > div:nth-child(2) > div:nth-child(1) > div > div.inner-content > h3 > a").click()

            self.driver.find_element(
                By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").clear()

            self.driver.find_element(
                By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").send_keys(quantity)

            self.driver.find_element(
                By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > button").click()

            error_message = self.driver.find_element(
                By.CSS_SELECTOR, 'body > div.product-detail > div:nth-child(1) > div > div:nth-child(2) > form > input').get_attribute("validationMessage")
            # self.driver.save_screenshot('image/pass/3.jpg')

            current_quantity = self.driver.find_element(
                By.CSS_SELECTOR, 'body > div.product-detail > div:nth-child(1) > div > div:nth-child(2) > div.inner-stock > span').text
            print(error_message)
            self.assertEqual(
                error_message, "Value must be less than or equal to " + current_quantity + ".")


if __name__ == "__main__":
    unittest.main()
