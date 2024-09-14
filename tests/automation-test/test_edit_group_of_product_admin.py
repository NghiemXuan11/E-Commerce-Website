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
        with open("Data/edit_group_of_product_function_data.json", encoding="utf-8") as f:
            data = json.load(f)
            username = data["test_cases_edit_group_of_product"][5]["username"]
            password = data["test_cases_edit_group_of_product"][5]["password"]
            title = data["test_cases_edit_group_of_product"][5]["title"]
            description = data["test_cases_edit_group_of_product"][5]["description"]
            location = data["test_cases_edit_group_of_product"][5]["location"]
            self.login(username, password)

            success_message = self.driver.find_element(
                By.CSS_SELECTOR, "body > header > div > div > div.col-3 > div > a").text
            # self.driver.save_screenshot('image/pass/1.jpg')
            # print(success_message)
            # self.assertEqual(success_message, "ADMIN")

            # Chọn danh mục sản phẩm
            self.driver.find_element(
                By.CSS_SELECTOR, "body > div > div.sider > div > ul > li:nth-child(2) > a").click()
            time.sleep(5)
            # Chọn thêm mới danh mục
            self.driver.find_element(
                By.XPATH, "/html/body/div/div[2]/div/div[2]/div/div[2]/a").click()

            # Điền nội dung tiêu đề
            self.driver.find_element(By.ID, "title").send_keys(title)

            # Chọn danh mục
            select_element = self.driver.find_element(By.ID, "parent_id")
            select = Select(select_element)
            select.select_by_index(0)  # Danh mục cha ở vị trí 0 (mặc định)
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

            # Chọn vị trí
            self.driver.find_element(
                By.CSS_SELECTOR, "#position").send_keys(location)

            # Chọn trạng thái Hoạt động/Không hoạt động
            # Hoạt động
            self.driver.find_element(
                By.XPATH, '//*[@id="statusActive"]').click()
            # Không hoạt động
            # self.driver.find_element(
            #     By.XPATH, '//*[@id="statusInActive"]').click()

            # Chọn tạo mới
            self.driver.find_element(
                By.XPATH, '/html/body/div[1]/div[2]/form/div[8]/button').click()
            time.sleep(5)

            # Chọn vào sửa
            self.driver.find_element(
                By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[3]/td[6]/a").click()
            time.sleep(3)

            # Sửa tiêu đề
            self.driver.find_element(
                By.ID, "title").clear()  # Xóa tiêu đề cũ
            self.driver.find_element(
                By.ID, "title").send_keys("Danh mục Apple")
            # Sửa vị trí
            self.driver.find_element(
                By.CSS_SELECTOR, "#position").clear()  # Xóa vị trí cũ
            self.driver.find_element(
                By.CSS_SELECTOR, "#position").send_keys("4")
            # Điền mô tả vào thẻ iframe (Sửa nội dung)
            self.driver.switch_to.frame("desc_ifr")
            body = self.driver.find_element(By.ID, "tinymce")
            body.clear()  # Clear any existing content
            body.send_keys("Đây là nội dung sửa")
            self.driver.switch_to.default_content()
            time.sleep(3)

            # Upload ảnh mới
            file_input = self.driver.find_element(By.ID, 'thumbnail')
            file_path = "D:/Project-managerTest/tests/automation-test/image_for_testing/cat.jpg"
            file_input.send_keys(file_path)
            time.sleep(3)

            # Sửa trạng thái
            self.driver.find_element(
                By.XPATH, '//*[@id="statusActive"]').click()

            # Chọn button cập nhật
            self.driver.find_element(
                By.XPATH, '/html/body/div[1]/div[2]/form/div[8]/button').click()
            time.sleep(5)

            # Vào lại danh mục sản phẩm chọn xem đã sửa chưa
            self.driver.find_element(
                By.XPATH, '/html/body/div[1]/div[1]/div/ul/li[2]/a').click()
            self.driver.save_screenshot('image/fail/TC_89.jpg')
            time.sleep(4)
            # Chọn vào sửa lại để xem
            # self.driver.find_element(
            #     By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[3]/td[6]/a").click()
            # time.sleep(3)


if __name__ == "__main__":
    unittest.main()
