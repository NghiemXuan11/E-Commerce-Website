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

    def test184(self):
        with open("Data/add_new_role_group_admin_function_data.json", encoding="utf-8") as f:
            data = json.load(f)
            username = data["test_cases_add_new_role_group"][0]["username"]
            password = data["test_cases_add_new_role_group"][0]["password"]
            title = data["test_cases_add_new_role_group"][0]["title"]
            description = data["test_cases_add_new_role_group"][0]["description"]

            self.login(username, password)
            # Vào chức năng nhóm quyền
            self.driver.find_element(
                By.XPATH, "/html/body/div/div[1]/div/ul/li[6]/a").click()
            time.sleep(3)
            # Vào thêm mới
            self.driver.find_element(
                By.XPATH, "/html/body/div/div[2]/div/div[2]/div/div[2]/a").click()
            # Điền thông tin thêm mới
