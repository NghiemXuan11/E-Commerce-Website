from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import unittest
import time
import json


class TestRegisterFunction(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://storecs.vercel.app/')

    def tearDown(self):
        self.driver.quit()

    def login(self, name, username, password):
        self.driver.find_element(
            By.CSS_SELECTOR, 'body > header > div > div > div.col-4 > div > ul > li:nth-child(5) > a').click()
        self.driver.find_element(By.ID, "fullName").send_keys(name)
        self.driver.find_element(By.ID, "email").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)

        self.driver.find_element(
            By.CSS_SELECTOR, "body > div > div > div > form > div:nth-child(4) > button").click()

    # Happy Cases
    # TC_9
    # def test9(self):
    #     with open("Data/register_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         name = data["test_cases_Register"][0]["name"]
    #         username = data["test_cases_Register"][0]["username"]
    #         password = data["test_cases_Register"][0]["password"]
    #         self.login(name, username, password)

    #         success_message_element = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-success"))
    #         )
    #         success_message = success_message_element.text.strip()
    #         self.driver.save_screenshot('image/fail/TC_09.jpg')
    #         print(success_message)
    #         self.assertEqual(success_message, "Đăng ký thành công! x")

    # Negative Cases
    # TC_10
    # def test10(self):
    #     with open("Data/register_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         name = data["test_cases_Register"][1]["name"]
    #         username = data["test_cases_Register"][1]["username"]
    #         password = data["test_cases_Register"][1]["password"]
    #         self.login(name, username, password)
    #         error_message_element = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-danger"))
    #         )
    #         error_message = error_message_element.text.strip()
    #         # self.driver.save_screenshot('10.jpg')
    #         print(error_message)
    #         self.assertEqual(error_message, "Họ tên không hợp lệ x")

    # # TC_11
    # def test11(self):
    #     with open("Data/register_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         name = data["test_cases_Register"][2]["name"]
    #         username = data["test_cases_Register"][2]["username"]
    #         password = data["test_cases_Register"][2]["password"]
    #         self.login(name, username, password)
    #         error_message = self.driver.find_element(
    #             By.ID, 'fullName').get_attribute("validationMessage")
    #         # self.driver.save_screenshot('image/pass/3.jpg')
    #         print(error_message)
    #         self.assertEqual(error_message, "Please fill out this field.")

    # # TC_12
    # def test12(self):
    #     with open("Data/register_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         name = data["test_cases_Register"][3]["name"]
    #         username = data["test_cases_Register"][3]["username"]
    #         password = data["test_cases_Register"][3]["password"]
    #         self.login(name, username, password)

    #         error_message_element = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-danger"))
    #         )
    #         error_message = error_message_element.text.strip()
    #         # self.driver.save_screenshot('image/pass/4.jpg')
    #         print(error_message)
    #         self.assertEqual(error_message, "Họ tên không hợp lệ x")

    # # TC_13
    # def test13(self):
    #     with open("Data/register_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         name = data["test_cases_Register"][4]["name"]
    #         username = data["test_cases_Register"][4]["username"]
    #         password = data["test_cases_Register"][4]["password"]
    #         self.login(name, username, password)

    #         error_message = self.driver.find_element(
    #             By.ID, 'email').get_attribute("validationMessage")
    #         # self.driver.save_screenshot('image/pass/3.jpg')
    #         print(error_message)
    #         self.assertEqual(error_message, "Please fill out this field.")

    # # TC_14
    # def test14(self):
    #     with open("Data/register_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         name = data["test_cases_Register"][5]["name"]
    #         username = data["test_cases_Register"][5]["username"]
    #         password = data["test_cases_Register"][5]["password"]
    #         self.login(name, username, password)

    #         error_message = self.driver.find_element(
    #             By.ID, 'email').get_attribute("validationMessage")
    #         # self.driver.save_screenshot('image/pass/6.jpg')
    #         print(error_message)
    #         self.assertEqual(
    #             error_message, "Please include an '@' in the email address. '"+username+"' is missing an '@'.")

    # # TC_15
    # def test15(self):
    #     with open("Data/register_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         name = data["test_cases_Register"][6]["name"]
    #         username = data["test_cases_Register"][6]["username"]
    #         password = data["test_cases_Register"][6]["password"]
    #         self.login(name, username, password)

    #         error_message = self.driver.find_element(
    #             By.ID, 'password').get_attribute("validationMessage")
    #         # self.driver.save_screenshot('image/pass/6.jpg')
    #         print(error_message)
    #         self.assertEqual(
    #             error_message, "Please fill out this field.")

    # # TC_16
    # def test16(self):
    #     with open("Data/register_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         name = data["test_cases_Register"][7]["name"]
    #         username = data["test_cases_Register"][7]["username"]
    #         password = data["test_cases_Register"][7]["password"]
    #         self.login(name, username, password)

    #         error_message_element = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-danger"))
    #         )
    #         error_message = error_message_element.text.strip()
    #         # self.driver.save_screenshot('image/pass/4.jpg')
    #         print(error_message)
    #         self.assertEqual(
    #             error_message, "Độ dài mật khẩu tối thiểu phải 8 ký tự x")

    # # TC_17
    # def test17(self):
    #     with open("Data/register_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         name = data["test_cases_Register"][8]["name"]
    #         username = data["test_cases_Register"][8]["username"]
    #         password = data["test_cases_Register"][8]["password"]
    #         self.login(name, username, password)

    #         error_message_element = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-danger"))
    #         )
    #         error_message = error_message_element.text.strip()
    #         self.driver.save_screenshot('image/fail/TC_17.jpg')
    #         print(error_message)
    #         self.assertEqual(
    #             error_message, "Mật khẩu phải có ít nhất 1 ký tự viết hoa x")

    # # TC_18
    # def test18(self):
    #     with open("Data/register_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         name = data["test_cases_Register"][9]["name"]
    #         username = data["test_cases_Register"][9]["username"]
    #         password = data["test_cases_Register"][9]["password"]
    #         self.login(name, username, password)

    #         error_message_element = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-danger"))
    #         )
    #         error_message = error_message_element.text.strip()
    #         self.driver.save_screenshot('image/fail/TC_18.jpg')
    #         print(error_message)
    #         self.assertEqual(
    #             error_message, "Mật khẩu phải có ít nhất 1 ký tự viết thường x")

    # # TC_19
    # def test19(self):
    #     with open("Data/register_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         name = data["test_cases_Register"][10]["name"]
    #         username = data["test_cases_Register"][10]["username"]
    #         password = data["test_cases_Register"][10]["password"]
    #         self.login(name, username, password)

    #         error_message_element = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-danger"))
    #         )
    #         error_message = error_message_element.text.strip()
    #         self.driver.save_screenshot('image/fail/TC_19.jpg')
    #         print(error_message)
    #         self.assertEqual(
    #             error_message, "Mật khẩu phải có ít nhất 2 chữ số x")

    # # TC_20
    def test20(self):
        with open("Data/register_function_data.json", encoding="utf-8") as f:
            data = json.load(f)
            name = data["test_cases_Register"][11]["name"]
            username = data["test_cases_Register"][11]["username"]
            password = data["test_cases_Register"][11]["password"]
            self.login(name, username, password)

            error_message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "alert-danger"))
            )
            error_message = error_message_element.text.strip()
            self.driver.save_screenshot('image/fail/TC_20.jpg')
            print(error_message)
            self.assertEqual(
                error_message, "Độ dài mật khẩu không quá 100 ký tự x")

    # # TC_21
    # def test21(self):
    #     with open("Data/register_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         name = data["test_cases_Register"][12]["name"]
    #         username = data["test_cases_Register"][12]["username"]
    #         password = data["test_cases_Register"][12]["password"]
    #         self.login(name, username, password)

    #         error_message = self.driver.find_element(
    #             By.ID, 'fullName').get_attribute("validationMessage")
    #         # self.driver.save_screenshot('image/pass/3.jpg')
    #         print(error_message)
    #         self.assertEqual(error_message, "Please fill out this field.")

    # # TC_22
    # def test22(self):
    #     with open("Data/register_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         name = data["test_cases_Register"][13]["name"]
    #         username = data["test_cases_Register"][13]["username"]
    #         password = data["test_cases_Register"][13]["password"]
    #         self.login(name, username, password)

    #         error_message_element = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-danger"))
    #         )
    #         error_message = error_message_element.text.strip()
    #         # self.driver.save_screenshot('image/pass/4.jpg')
    #         print(error_message)
    #         self.assertEqual(error_message, "Email đã tồn tại! x")


if __name__ == "__main__":
    unittest.main()
