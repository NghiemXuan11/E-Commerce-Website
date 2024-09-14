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

    # Happy Cases
    # TC_83
    def test83(self):
        with open("Data/edit_prodcuct_detail_function_admin_data.json", encoding="utf-8") as f:
            data = json.load(f)
            username = data["test_cases_edit_detail_product"][0]["username"]
            password = data["test_cases_edit_detail_product"][0]["password"]
            title = data["test_cases_edit_detail_product"][0]["title"]
            description = data["test_cases_edit_detail_product"][0]["description"]
            self.login(username, password)

            success_message = self.driver.find_element(
                By.CSS_SELECTOR, "body > header > div > div > div.col-3 > div > a").text
            # self.driver.save_screenshot('image/pass/1.jpg')
            # print(success_message)
            # self.assertEqual(success_message, "ADMIN")

            # Chọn danh sách sản phẩm
            self.driver.find_element(
                By.XPATH, "/html/body/div/div[1]/div/ul/li[3]/a").click()
            time.sleep(5)
            # Chọn sửa danh mục
            self.driver.find_element(
                By.XPATH, "/html/body/div/div[2]/div[2]/div[4]/table/tbody/tr[1]/td[10]/a[2]").click()

            # Sửa nội dung tiêu đề
            self.driver.find_element(By.ID, "title").clear()
            self.driver.find_element(By.ID, "title").send_keys("T134")

            # Chọn danh mục
            select_element = self.driver.find_element(
                By.ID, "product_category_id")
            select = Select(select_element)
            select.select_by_index(1)  # Danh mục Apple ở vị trí 1 (mặc định)
            time.sleep(2)

            # Điền mô tả vào thẻ iframe
            self.driver.switch_to.frame("desc_ifr")
            body = self.driver.find_element(By.ID, "tinymce")
            body.clear()  # Clear any existing content
            body.send_keys(description)
            self.driver.switch_to.default_content()
            time.sleep(3)

            # Upload ảnh
            file_input = self.driver.find_element(By.ID, 'thumbnail')
            file_path = "D:/Project-managerTest/tests/automation-test/image_for_testing/dog.jpg"
            file_input.send_keys(file_path)
            time.sleep(3)

            # Chọn trạng thái Hoạt động/Không hoạt động
            # Hoạt động
            self.driver.find_element(
                By.XPATH, '//*[@id="statusActive"]').click()
            # Không hoạt động
            # self.driver.find_element(
            #     By.XPATH, '//*[@id="statusInActive"]').click()

            # Chọn cập nhật
            self.driver.find_element(
                By.XPATH, '/html/body/div[1]/div[2]/form/div[13]/button').click()
            time.sleep(5)

            # Về danh sách sản phẩm xem tiêu đề chỉnh sửa
            self.driver.find_element(
                By.XPATH, "/html/body/div/div[1]/div/ul/li[3]/a").click()
            self.driver.save_screenshot('image/fail/134.jpg')
            time.sleep(5)


if __name__ == "__main__":
    unittest.main()
