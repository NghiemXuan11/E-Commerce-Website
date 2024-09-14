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
        self.driver.get('https://storecs.vercel.app/admin/auth/login/')

    def tearDown(self):
        self.driver.quit()

    def login(self, username, password):
        self.driver.find_element(By.ID, "email").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(
            By.CSS_SELECTOR, "body > div > div > div > form > div:nth-child(3) > button").click()

    # Happy Cases
    # TC_63
    def test63(self):
        with open("Data/login_admin_function_data.json", encoding="utf-8") as f:
            data = json.load(f)
            username = data["test_cases_login_admin"][0]["username"]
            password = data["test_cases_login_admin"][0]["password"]
            self.login(username, password)

            success_message = self.driver.find_element(
                By.CSS_SELECTOR, "body > header > div > div > div.col-3 > div > a").text
            # self.driver.save_screenshot('image/pass/1.jpg')
            print(success_message)
            self.assertEqual(success_message, "ADMIN")

    # Negative Cases
    # TC_64
    def test64(self):
        with open("Data/login_admin_function_data.json", encoding="utf-8") as f:
            data = json.load(f)
            username = data["test_cases_login_admin"][1]["username"]
            password = data["test_cases_login_admin"][1]["password"]
            self.login(username, password)

            error_message = self.driver.find_element(
                By.ID, 'email').get_attribute("validationMessage")
            # self.driver.save_screenshot('image/pass/3.jpg')
            print(error_message)
            self.assertEqual(error_message, "Please fill out this field.")

    # TC_65
    def test65(self):
        with open("Data/login_admin_function_data.json", encoding="utf-8") as f:
            data = json.load(f)
            username = data["test_cases_login_admin"][2]["username"]
            password = data["test_cases_login_admin"][2]["password"]
            self.login(username, password)

            error_message = self.driver.find_element(
                By.ID, 'email').get_attribute("validationMessage")
            # self.driver.save_screenshot('image/pass/3.jpg')
            print(error_message)
            self.assertEqual(error_message, "Please fill out this field.")

    # TC_66
    def test66(self):
        with open("Data/login_admin_function_data.json", encoding="utf-8") as f:
            data = json.load(f)
            username = data["test_cases_login_admin"][3]["username"]
            password = data["test_cases_login_admin"][3]["password"]
            self.login(username, password)

            error_message = self.driver.find_element(
                By.ID, 'password').get_attribute("validationMessage")
            # self.driver.save_screenshot('image/pass/3.jpg')
            print(error_message)
            self.assertEqual(error_message, "Please fill out this field.")

    # TC_67
    def test67(self):
        with open("Data/login_admin_function_data.json", encoding="utf-8") as f:
            data = json.load(f)
            username = data["test_cases_login_admin"][4]["username"]
            password = data["test_cases_login_admin"][4]["password"]
            self.login(username, password)

            error_message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "alert-danger"))
            )
            error_message = error_message_element.text.strip()
            # self.driver.save_screenshot('image/pass/4.jpg')
            print(error_message)
            self.assertEqual(error_message, "Sai mật khẩu x")

    # TC_68
    def test68(self):
        with open("Data/login_admin_function_data.json", encoding="utf-8") as f:
            data = json.load(f)
            username = data["test_cases_login_admin"][5]["username"]
            password = data["test_cases_login_admin"][5]["password"]
            self.login(username, password)

            error_message = self.driver.find_element(
                By.ID, 'email').get_attribute("validationMessage")
            # self.driver.save_screenshot('image/pass/6.jpg')
            print(error_message)
            self.assertEqual(
                error_message, "Please include an '@' in the email address. '"+username+"' is missing an '@'.")

    # TC_69
    def test69(self):
        with open("Data/login_admin_function_data.json", encoding="utf-8") as f:
            data = json.load(f)
            username = data["test_cases_login_admin"][6]["username"]
            password = data["test_cases_login_admin"][6]["password"]
            self.login(username, password)

            error_message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "alert-danger"))
            )
            error_message = error_message_element.text.strip()
            # self.driver.save_screenshot('image/pass/4.jpg')
            print(error_message)
            self.assertEqual(error_message, "Email không tồn tại x")

    # TC_70
    def test70(self):
        with open("Data/login_admin_function_data.json", encoding="utf-8") as f:
            data = json.load(f)
            username = data["test_cases_login_admin"][7]["username"]
            password = data["test_cases_login_admin"][7]["password"]
            self.login(username, password)

            error_message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "alert-danger"))
            )
            error_message = error_message_element.text.strip()
            # self.driver.save_screenshot('image/pass/4.jpg')
            print(error_message)
            self.assertEqual(error_message, "Email không tồn tại x")


if __name__ == "__main__":
    unittest.main()
