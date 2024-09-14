from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select  # Chọn drop down
from selenium.webdriver.common.action_chains import ActionChains  # hover
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

    # TC_187
    def test187(self):
        with open("Data/edit_group_of_role_function_admin.json", encoding="utf-8") as f:
            data = json.load(f)
            username = data["test_cases_edit_group_of_role"][2]["username"]
            password = data["test_cases_edit_group_of_role"][2]["password"]
            title = data["test_cases_edit_group_of_role"][2]["title"]
            description = data["test_cases_edit_group_of_role"][2]["description"]
            self.login(username, password)

            success_message = self.driver.find_element(
                By.CSS_SELECTOR, "body > header > div > div > div.col-3 > div > a").text
            # self.driver.save_screenshot('image/pass/1.jpg')
            # print(success_message)
            # self.assertEqual(success_message, "ADMIN")

            # Chọn danh sách nhóm quyền
            self.driver.find_element(
                By.XPATH, "/html/body/div/div[1]/div/ul/li[6]/a").click()
            time.sleep(5)
            # Chọn sửa nhóm quyền
            self.driver.find_element(
                By.XPATH, "/html/body/div/div[2]/div/div[2]/table/tbody/tr[3]/td[4]/a").click()

            # Sửa nội dung tiêu đề
            self.driver.find_element(By.ID, "title").clear()
            self.driver.find_element(By.ID, "title").send_keys(title)

            # Sử nội dung mô tả
            self.driver.find_element(By.ID, "desc").clear()
            self.driver.find_element(By.ID, "desc").send_keys(description)

            # Chọn cập nhật
            self.driver.find_element(
                By.CSS_SELECTOR, 'body > div > div.main > form > div:nth-child(3) > button').click()
            self.driver.save_screenshot('image/fail/189.jpg')
            time.sleep(5)


if __name__ == "__main__":
    unittest.main()
