from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import unittest
import time
import json
import imaplib
import email
import regex  # thư viện trích chuỗi
import ezgmail  # thư viện đọc mail
from email.header import decode_header
from selenium import webdriver


class TestForgotPasswordFunction(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://storecs.vercel.app/')

    def tearDown(self):
        self.driver.quit()

    def login(self, username):
        self.driver.find_element(
            By.CSS_SELECTOR, 'div > ul > li:nth-child(4) > a').click()
        self.driver.find_element(
            By.CSS_SELECTOR, "body > div > div > div > a").click()
        self.driver.find_element(By.ID, "email").send_keys(username)
        self.driver.find_element(
            By.CSS_SELECTOR, 'body > div > div > div > form > div:nth-child(2) > button').click()

    # Happy Cases
    # TC_23
    def test23(self):
        with open("Data/forgot_password_function_data.json", encoding="utf-8") as f:
            data = json.load(f)
            email = data["test_cases_Forgot_Password"][0]["email"]
            password = data["test_cases_Forgot_Password"][0]["password"]
            self.login(email)
            time.sleep(5)
            # Lấy OTP
            unreadThreads = ezgmail.unread()
            a = str(unreadThreads[0])
            otpmatch = regex.search(r'\b\d{8}\b', a)
            otp = otpmatch.group(0)
            # print(a)
            # print(otp)
            time.sleep(6)
            # Điền OTP và đổi mật khẩu
            self.driver.find_element(By.ID, "otp").send_keys(otp)
            self.driver.find_element(
                By.CSS_SELECTOR, "body > div > div > div > form > div:nth-child(3) > button").click()
            self.driver.find_element(By.ID, "password").send_keys(password)
            self.driver.find_element(
                By.ID, "confirmPassword").send_keys(password)
            self.driver.find_element(
                By.CSS_SELECTOR, "body > div.container.my-5 > div > div > form > div:nth-child(3) > button").click()

            success_message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "alert-success"))
            )
            success_message = success_message_element.text.strip()
            # self.driver.save_screenshot('123lmss.png')
            print(success_message)
            self.assertEqual(success_message, "Đổi mật khẩu thành công! x")

    # Negative Cases
    # TC_24
    # def test24(self):
    #     with open("Data/forgot_password_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         email = data["test_cases_Forgot_Password"][1]["email"]
    #         self.login(email)
    #         error_message = self.driver.find_element(
    #             By.ID, 'email').get_attribute("validationMessage")
    #         # self.driver.save_screenshot('123lmss.png')
    #         print(error_message)
    #         self.assertEqual(
    #             error_message, "Please include an '@' in the email address. '"+email+"' is missing an '@'.")

    # TC_25
    # def test25(self):
    #     with open("Data/forgot_password_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         email = data["test_cases_Forgot_Password"][2]["email"]
    #         self.login(email)
    #         error_message = self.driver.find_element(
    #             By.ID, 'email').get_attribute("validationMessage")
    #         # self.driver.save_screenshot('123lmss.png')
    #         print(error_message)
    #         self.assertEqual(
    #             error_message, "Please fill out this field.")

    # TC_26
    # def test26(self):
    #     with open("Data/forgot_password_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         email = data["test_cases_Forgot_Password"][3]["email"]
    #         self.login(email)
    #         error_message_element = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-danger"))
    #         )
    #         error_message = error_message_element.text.strip()
    #         # self.driver.save_screenshot('123lmss.png')
    #         print(error_message)
    #         self.assertEqual(error_message, "Email không tồn tại! x")

    # TC_27
    # def test27(self):
    #     with open("Data/forgot_password_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         email = data["test_cases_Forgot_Password"][4]["email"]
    #         password = data["test_cases_Forgot_Password"][4]["password"]
    #         self.login(email)
    #         time.sleep(5)
    #         # Lấy OTP
    #         unreadThreads = ezgmail.unread()
    #         a = str(unreadThreads[0])
    #         otpmatch = regex.search(r'\b\d{8}\b', a)
    #         otp = otpmatch.group(0)
    #         # print(a)
    #         # print(otp)
    #         time.sleep(6)
    #         # Điền OTP và đổi mật khẩu
    #         self.driver.find_element(By.ID, "otp").send_keys(otp)
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div > div > form > div:nth-child(3) > button").click()
    #         self.driver.find_element(By.ID, "password").send_keys(password)
    #         self.driver.find_element(
    #             By.ID, "confirmPassword").send_keys(password)
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div.container.my-5 > div > div > form > div:nth-child(3) > button").click()

    #         error_message = self.driver.find_element(
    #             By.ID, 'password').get_attribute("validationMessage")
    #         # self.driver.save_screenshot('image/pass/6.jpg')
    #         print(error_message)
    #         self.assertEqual(
    #             error_message, "Please fill out this field.")

    # TC_28
    # def test28(self):
    #     with open("Data/forgot_password_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         email = data["test_cases_Forgot_Password"][5]["email"]
    #         password = data["test_cases_Forgot_Password"][5]["password"]
    #         self.login(email)
    #         time.sleep(5)
    #         # Lấy OTP
    #         unreadThreads = ezgmail.unread()
    #         a = str(unreadThreads[0])
    #         otpmatch = regex.search(r'\b\d{8}\b', a)
    #         otp = otpmatch.group(0)
    #         # print(a)
    #         # print(otp)
    #         time.sleep(6)
    #         # Điền OTP và đổi mật khẩu
    #         self.driver.find_element(By.ID, "otp").send_keys(otp)
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div > div > form > div:nth-child(3) > button").click()
    #         self.driver.find_element(
    #             By.ID, "confirmPassword").send_keys(password)
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div.container.my-5 > div > div > form > div:nth-child(3) > button").click()

    #         error_message = self.driver.find_element(
    #             By.ID, 'password').get_attribute("validationMessage")
    #         # self.driver.save_screenshot('image/pass/6.jpg')
    #         print(error_message)
    #         self.assertEqual(
    #             error_message, "Please fill out this field.")

    # TC_29
    # def test29(self):
    #     with open("Data/forgot_password_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         email = data["test_cases_Forgot_Password"][6]["email"]
    #         password = data["test_cases_Forgot_Password"][6]["password"]
    #         self.login(email)
    #         time.sleep(5)
    #         # Lấy OTP
    #         unreadThreads = ezgmail.unread()
    #         a = str(unreadThreads[0])
    #         otpmatch = regex.search(r'\b\d{8}\b', a)
    #         otp = otpmatch.group(0)
    #         # print(a)
    #         # print(otp)
    #         time.sleep(6)
    #         # Điền OTP và đổi mật khẩu
    #         self.driver.find_element(By.ID, "otp").send_keys(otp)
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div > div > form > div:nth-child(3) > button").click()
    #         self.driver.find_element(
    #             By.ID, "password").send_keys(password)
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div.container.my-5 > div > div > form > div:nth-child(3) > button").click()

    #         error_message = self.driver.find_element(
    #             By.ID, 'confirmPassword').get_attribute("validationMessage")
    #         # self.driver.save_screenshot('image/pass/6.jpg')
    #         print(error_message)
    #         self.assertEqual(
    #             error_message, "Please fill out this field.")

    # TC_30
    # def test30(self):
    #     with open("Data/forgot_password_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         email = data["test_cases_Forgot_Password"][7]["email"]
    #         password = data["test_cases_Forgot_Password"][7]["password"]
    #         confirmPassword = data["test_cases_Forgot_Password"][7]["confirmpassword"]
    #         self.login(email)
    #         time.sleep(5)
    #         # Lấy OTP
    #         unreadThreads = ezgmail.unread()
    #         a = str(unreadThreads[0])
    #         otpmatch = regex.search(r'\b\d{8}\b', a)
    #         otp = otpmatch.group(0)
    #         # print(a)
    #         # print(otp)
    #         time.sleep(6)
    #         # Điền OTP và đổi mật khẩu
    #         self.driver.find_element(By.ID, "otp").send_keys(otp)
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div > div > form > div:nth-child(3) > button").click()
    #         self.driver.find_element(
    #             By.ID, "password").send_keys(password)
    #         self.driver.find_element(
    #             By.ID, "confirmPassword").send_keys(confirmPassword)
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div.container.my-5 > div > div > form > div:nth-child(3) > button").click()

    #         error_message_element = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-danger"))
    #         )
    #         error_message = error_message_element.text.strip()
    #         # self.driver.save_screenshot('image/pass/4.jpg')
    #         print(error_message)
    #         self.assertEqual(
    #             error_message, "Xác nhận mật khẩu không khớp với mật khẩu trên! x")

    # TC_31
    # def test31(self):
    #     with open("Data/forgot_password_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         email = data["test_cases_Forgot_Password"][8]["email"]
    #         password = data["test_cases_Forgot_Password"][8]["password"]
    #         confirmPassword = data["test_cases_Forgot_Password"][8]["confirmpassword"]
    #         self.login(email)
    #         time.sleep(5)
    #         # Lấy OTP
    #         unreadThreads = ezgmail.unread()
    #         a = str(unreadThreads[0])
    #         otpmatch = regex.search(r'\b\d{8}\b', a)
    #         otp = otpmatch.group(0)
    #         # print(a)
    #         # print(otp)
    #         time.sleep(6)
    #         # Điền OTP và đổi mật khẩu
    #         self.driver.find_element(By.ID, "otp").send_keys(otp)
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div > div > form > div:nth-child(3) > button").click()
    #         self.driver.find_element(
    #             By.ID, "password").send_keys(password)
    #         self.driver.find_element(
    #             By.ID, "confirmPassword").send_keys(confirmPassword)
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div.container.my-5 > div > div > form > div:nth-child(3) > button").click()

    #         error_message_element = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-danger"))
    #         )
    #         error_message = error_message_element.text.strip()
    #         # self.driver.save_screenshot('image/pass/4.jpg')
    #         print(error_message)
    #         self.assertEqual(
    #             error_message, "password: Độ dài mật khẩu tối thiểu phải 8 ký tự x")

    # # TC_32
    # def test32(self):
    #     with open("Data/forgot_password_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         email = data["test_cases_Forgot_Password"][9]["email"]
    #         password = data["test_cases_Forgot_Password"][9]["password"]
    #         confirmPassword = data["test_cases_Forgot_Password"][9]["confirmpassword"]
    #         self.login(email)
    #         time.sleep(5)
    #         # Lấy OTP
    #         unreadThreads = ezgmail.unread()
    #         a = str(unreadThreads[0])
    #         otpmatch = regex.search(r'\b\d{8}\b', a)
    #         otp = otpmatch.group(0)
    #         # print(a)
    #         # print(otp)
    #         time.sleep(6)
    #         # Điền OTP và đổi mật khẩu
    #         self.driver.find_element(By.ID, "otp").send_keys(otp)
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div > div > form > div:nth-child(3) > button").click()
    #         self.driver.find_element(
    #             By.ID, "password").send_keys(password)
    #         self.driver.find_element(
    #             By.ID, "confirmPassword").send_keys(confirmPassword)
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div.container.my-5 > div > div > form > div:nth-child(3) > button").click()

    #         error_message_element = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-danger"))
    #         )
    #         error_message = error_message_element.text.strip()
    #         # self.driver.save_screenshot('image/pass/4.jpg')
    #         print(error_message)
    #         self.assertEqual(
    #             error_message, "password: Phải có ít nhất 1 chữ viết hoa x")

    # TC_33
    # def test33(self):
    #     with open("Data/forgot_password_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         email = data["test_cases_Forgot_Password"][10]["email"]
    #         password = data["test_cases_Forgot_Password"][10]["password"]
    #         confirmPassword = data["test_cases_Forgot_Password"][10]["confirmpassword"]
    #         self.login(email)
    #         time.sleep(5)
    #         # Lấy OTP
    #         unreadThreads = ezgmail.unread()
    #         a = str(unreadThreads[0])
    #         otpmatch = regex.search(r'\b\d{8}\b', a)
    #         otp = otpmatch.group(0)
    #         # print(a)
    #         # print(otp)
    #         time.sleep(6)
    #         # Điền OTP và đổi mật khẩu
    #         self.driver.find_element(By.ID, "otp").send_keys(otp)
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div > div > form > div:nth-child(3) > button").click()
    #         self.driver.find_element(
    #             By.ID, "password").send_keys(password)
    #         self.driver.find_element(
    #             By.ID, "confirmPassword").send_keys(confirmPassword)
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div.container.my-5 > div > div > form > div:nth-child(3) > button").click()

    #         error_message_element = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-danger"))
    #         )
    #         error_message = error_message_element.text.strip()
    #         # self.driver.save_screenshot('image/pass/4.jpg')
    #         print(error_message)
    #         self.assertEqual(
    #             error_message, "password: Phải có ít nhất 1 chữ viết thường x")

    # TC_34
    # def test34(self):
    #     with open("Data/forgot_password_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         email = data["test_cases_Forgot_Password"][11]["email"]
    #         password = data["test_cases_Forgot_Password"][11]["password"]
    #         confirmPassword = data["test_cases_Forgot_Password"][11]["confirmpassword"]
    #         self.login(email)
    #         time.sleep(5)
    #         # Lấy OTP
    #         unreadThreads = ezgmail.unread()
    #         a = str(unreadThreads[0])
    #         otpmatch = regex.search(r'\b\d{8}\b', a)
    #         otp = otpmatch.group(0)
    #         # print(a)
    #         # print(otp)
    #         time.sleep(6)
    #         # Điền OTP và đổi mật khẩu
    #         self.driver.find_element(By.ID, "otp").send_keys(otp)
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div > div > form > div:nth-child(3) > button").click()
    #         self.driver.find_element(
    #             By.ID, "password").send_keys(password)
    #         self.driver.find_element(
    #             By.ID, "confirmPassword").send_keys(confirmPassword)
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div.container.my-5 > div > div > form > div:nth-child(3) > button").click()

    #         error_message_element = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-danger"))
    #         )
    #         error_message = error_message_element.text.strip()
    #         # self.driver.save_screenshot('image/pass/4.jpg')
    #         print(error_message)
    #         self.assertEqual(
    #             error_message, "password: Phải có ít nhất 2 chữ số x")

    # TC_35
    # def test35(self):
    #     with open("Data/forgot_password_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         email = data["test_cases_Forgot_Password"][12]["email"]
    #         password = data["test_cases_Forgot_Password"][12]["password"]
    #         confirmPassword = data["test_cases_Forgot_Password"][12]["confirmpassword"]
    #         self.login(email)
    #         time.sleep(5)
    #         # Lấy OTP
    #         unreadThreads = ezgmail.unread()
    #         a = str(unreadThreads[0])
    #         otpmatch = regex.search(r'\b\d{8}\b', a)
    #         otp = otpmatch.group(0)
    #         # print(a)
    #         # print(otp)
    #         time.sleep(6)
    #         # Điền OTP và đổi mật khẩu
    #         self.driver.find_element(By.ID, "otp").send_keys(otp)
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div > div > form > div:nth-child(3) > button").click()
    #         self.driver.find_element(
    #             By.ID, "password").send_keys(password)
    #         self.driver.find_element(
    #             By.ID, "confirmPassword").send_keys(confirmPassword)
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div.container.my-5 > div > div > form > div:nth-child(3) > button").click()

    #         error_message_element = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-success"))
    #         )
    #         error_message = error_message_element.text.strip()
    #         self.driver.save_screenshot('image/fail/TC_35.jpg')
    #         print(error_message)
    #         self.assertEqual(
    #             error_message, "password: Độ dài mật khẩu không quá 100 ký tự x")


if __name__ == "__main__":
    unittest.main()
