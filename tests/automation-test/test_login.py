from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import unittest
import time
import json


class TestLoginFunction(unittest.TestCase):
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
    # TC_01
    def test1(self):
        with open("Data/login_function_data.json", encoding="utf-8") as f:
            data = json.load(f)
            username = data["test_cases_login"][0]["username"]
            password = data["test_cases_login"][0]["password"]
            self.login(username, password)
            # time.sleep(5)
            # a = self.driver.switch_to().alert()
            # success_message = self.driver.switch_to.alert.text
            # success_message = self.driver.find_element(
            #     By.CLASS_NAME, "alert-success").text
            # time.sleep(5)
            success_message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "alert-success"))
            )
            success_message = success_message_element.text.strip()
            self.driver.save_screenshot('image/pass/1.jpg')
            print(success_message)
            self.assertEqual(success_message, "Đăng nhập thành công! x")

    # Negative Cases
    # TC_02
    def test2(self):
        with open("Data/login_function_data.json", encoding="utf-8") as f:
            data = json.load(f)
            username = data["test_cases_login"][1]["username"]
            password = data["test_cases_login"][1]["password"]
            self.login(username, password)
            # time.sleep(3)
            error_message = self.driver.find_element(
                By.ID, 'email').get_attribute("validationMessage")
            print(error_message)
            self.driver.save_screenshot('image/pass/2.jpg')
            self.assertEqual(error_message, "Please fill out this field.")

    # TC_03
    def test3(self):
        with open("Data/login_function_data.json", encoding="utf-8") as f:
            data = json.load(f)
            username = data["test_cases_login"][2]["username"]
            password = data["test_cases_login"][2]["password"]
            self.login(username, password)
            error_message = self.driver.find_element(
                By.ID, 'email').get_attribute("validationMessage")
            self.driver.save_screenshot('image/pass/3.jpg')
            print(error_message)
            self.assertEqual(error_message, "Please fill out this field.")

    # TC_04
    def test4(self):
        with open("Data/login_function_data.json", encoding="utf-8") as f:
            data = json.load(f)
            username = data["test_cases_login"][3]["username"]
            password = data["test_cases_login"][3]["password"]
            self.login(username, password)

            error_message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "alert-danger"))
            )
            error_message = error_message_element.text.strip()
            self.driver.save_screenshot('image/pass/4.jpg')
            print(error_message)
            self.assertEqual(error_message, "Mật khẩu không được để trống x")

    # TC_05
    def test5(self):
        with open("Data/login_function_data.json", encoding="utf-8") as f:
            data = json.load(f)
            username = data["test_cases_login"][4]["username"]
            password = data["test_cases_login"][4]["password"]
            self.login(username, password)
            error_message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "alert-danger"))
            )
            error_message = error_message_element.text.strip()
            self.driver.save_screenshot('image/pass/5.jpg')
            print(error_message)
            self.assertEqual(error_message, "Sai mật khẩu! x")

    # TC_06
    def test6(self):
        with open("Data/login_function_data.json", encoding="utf-8") as f:
            data = json.load(f)
            username = data["test_cases_login"][5]["username"]
            password = data["test_cases_login"][5]["password"]
            self.login(username, password)
            error_message = self.driver.find_element(
                By.ID, 'email').get_attribute("validationMessage")
            self.driver.save_screenshot('image/pass/6.jpg')
            print(error_message)
            self.assertEqual(
                error_message, "Please include an '@' in the email address. '"+username+"' is missing an '@'.")

    # TC_07
    def test7(self):
        with open("Data/login_function_data.json", encoding="utf-8") as f:
            data = json.load(f)
            username = data["test_cases_login"][6]["username"]
            password = data["test_cases_login"][6]["password"]
            self.login(username, password)
            error_message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "alert-danger"))
            )
            error_message = error_message_element.text.strip()
            self.driver.save_screenshot('image/pass/7.jpg')
            print(error_message)
            self.assertEqual(error_message, "Email không tồn tại! x")

    # TC_08
    def test8(self):
        with open("Data/login_function_data.json", encoding="utf-8") as f:
            data = json.load(f)
            username = data["test_cases_login"][7]["username"]
            password = data["test_cases_login"][7]["password"]
            self.login(username, password)
            error_message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "alert-danger"))
            )
            error_message = error_message_element.text.strip()
            self.driver.save_screenshot('image/pass/8.jpg')
            print(error_message)
            self.assertEqual(error_message, "Email không tồn tại! x")


if __name__ == "__main__":
    unittest.main()
