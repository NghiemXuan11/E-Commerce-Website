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

    def test194(self):
        with open("Data/role_division_functon_admin_data.json", encoding="utf-8") as f:
            data = json.load(f)
            username1 = data["test_cases_role_division"][0]["username1"]
            password1 = data["test_cases_role_division"][0]["password1"]
            username2 = data["test_cases_role_division"][0]["username2"]
            password2 = data["test_cases_role_division"][0]["password2"]
            self.login(username1, password1)
            # Vào danh sách tài khoản để chọn tk phân quyền
            self.driver.find_element(
                By.XPATH, "/html/body/div/div[1]/div/ul/li[8]/a").click()
            time.sleep(3)
            # Chọn sửa
            self.driver.find_element(
                By.XPATH, "/html/body/div/div[2]/div/div[2]/table/tbody/tr[4]/td[7]/a[2]").click()
            time.sleep(3)
            # Đổi quyền
            select_element = self.driver.find_element(By.ID, "role_id")
            select = Select(select_element)
            select.select_by_visible_text("Nhân viên")
            # Kiểm tra lại giá trị đã chọn (có thể bỏ qua nếu không cần)
            selected_option = select.first_selected_option
            print("Selected option:", selected_option.text)
            # Chọn cập nhật
            self.driver.find_element(
                By.CSS_SELECTOR, "body > div > div.main > form > div:nth-child(9) > button").click()
            time.sleep(3)
            # Đăng xuất
            self.driver.find_element(
                By.XPATH, "/html/body/header/div/div/div[2]/div/a[2]").click()
            time.sleep(3)
            # Đăng nhập tk vừa dc sửa quyền
            self.login(username2, password2)
            time.sleep(5)

    def test195(self):
        with open("Data/role_division_functon_admin_data.json", encoding="utf-8") as f:
            data = json.load(f)
            username1 = data["test_cases_role_division"][1]["username1"]
            password1 = data["test_cases_role_division"][1]["password1"]
            username2 = data["test_cases_role_division"][1]["username2"]
            password2 = data["test_cases_role_division"][1]["password2"]
            self.login(username1, password1)
            # Vào danh sách tài khoản để chọn tk phân quyền
            self.driver.find_element(
                By.XPATH, "/html/body/div/div[1]/div/ul/li[8]/a").click()
            time.sleep(3)
            # Chọn sửa
            self.driver.find_element(
                By.XPATH, "/html/body/div/div[2]/div/div[2]/table/tbody/tr[4]/td[7]/a[2]").click()
            time.sleep(3)
            # Đổi quyền
            select_element = self.driver.find_element(By.ID, "role_id")
            select = Select(select_element)
            select.select_by_visible_text("Quản Trị Viên")
            # Kiểm tra lại giá trị đã chọn (có thể bỏ qua nếu không cần)
            selected_option = select.first_selected_option
            print("Selected option:", selected_option.text)
            # Chọn cập nhật
            self.driver.find_element(
                By.CSS_SELECTOR, "body > div > div.main > form > div:nth-child(9) > button").click()
            time.sleep(3)
            # Đăng xuất
            self.driver.find_element(
                By.XPATH, "/html/body/header/div/div/div[2]/div/a[2]").click()
            time.sleep(3)
            # Đăng nhập tk vừa dc sửa quyền
            self.login(username2, password2)
            time.sleep(5)


if __name__ == "__main__":
    unittest.main()
