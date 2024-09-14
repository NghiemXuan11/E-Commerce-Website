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
    # TC_71
    def test71(self):
        with open("Data/add_new_group_of_product_function_data.json", encoding="utf-8") as f:
            data = json.load(f)
            username = data["test_cases_add_new_group_of_product"][0]["username"]
            password = data["test_cases_add_new_group_of_product"][0]["password"]
            title = data["test_cases_add_new_group_of_product"][0]["title"]
            description = data["test_cases_add_new_group_of_product"][0]["description"]
            location = data["test_cases_add_new_group_of_product"][0]["location"]
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
            self.driver.save_screenshot('image/fail/TC_79.jpg')
            # Kiểm tra xem danh mục mới có xuất hiện bên màn hình user hay ko
            self.driver.get('https://storecs.vercel.app/')
            main_menu_item = self.driver.find_element(
                By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li.sub-menu > a")
            actions = ActionChains(self.driver)
            actions.move_to_element(main_menu_item).perform()
            self.driver.implicitly_wait(10)
            time.sleep(5)
            # So sánh kết quả với database (thêm sau)

    # TC_72
    # def test72(self):
    #     with open("Data/add_new_group_of_product_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         username = data["test_cases_add_new_group_of_product"][1]["username"]
    #         password = data["test_cases_add_new_group_of_product"][1]["password"]
    #         title = data["test_cases_add_new_group_of_product"][1]["title"]
    #         description = data["test_cases_add_new_group_of_product"][1]["description"]
    #         location = data["test_cases_add_new_group_of_product"][1]["location"]
    #         self.login(username, password)

    #         success_message = self.driver.find_element(
    #             By.CSS_SELECTOR, "body > header > div > div > div.col-3 > div > a").text
    #         # self.driver.save_screenshot('image/pass/1.jpg')
    #         # print(success_message)
    #         # self.assertEqual(success_message, "ADMIN")

    #         # Chọn danh mục sản phẩm
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div.sider > div > ul > li:nth-child(2) > a").click()
    #         time.sleep(5)
    #         # Chọn thêm mới danh mục
    #         self.driver.find_element(
    #             By.XPATH, "/html/body/div/div[2]/div/div[2]/div/div[2]/a").click()

    #         # Điền nội dung tiêu đề
    #         self.driver.find_element(By.ID, "title").send_keys(title)

    #         # Chọn danh mục
    #         select_element = self.driver.find_element(By.ID, "parent_id")
    #         select = Select(select_element)
    #         select.select_by_index(1)  # Danh mục Apple ở vị trí 1
    #         time.sleep(2)

    #         # Điền mô tả vào thẻ iframe
    #         self.driver.switch_to.frame("desc_ifr")
    #         body = self.driver.find_element(By.ID, "tinymce")
    #         body.clear()  # Clear any existing content
    #         body.send_keys(description)
    #         self.driver.switch_to.default_content()
    #         time.sleep(3)

    #         # Upload ảnh
    #         file_input = self.driver.find_element(By.ID, 'thumbnail')
    #         file_path = "D:/Project-managerTest/tests/automation-test/image_for_testing/dog.jpg"
    #         file_input.send_keys(file_path)
    #         time.sleep(3)

    #         # Chọn vị trí
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "#position").send_keys(location)

    #         # Chọn trạng thái Hoạt động/Không hoạt động
    #         # Hoạt động
    #         self.driver.find_element(
    #             By.XPATH, '//*[@id="statusActive"]').click()
    #         # Không hoạt động
    #         # self.driver.find_element(
    #         #     By.XPATH, '//*[@id="statusInActive"]').click()

    #         # Chọn tạo mới
    #         self.driver.find_element(
    #             By.XPATH, '/html/body/div[1]/div[2]/form/div[8]/button').click()
    #         time.sleep(5)

    #         # Kiểm tra xem danh mục mới có xuất hiện bên màn hình user hay ko
    #         self.driver.get('https://storecs.vercel.app/')
    #         main_menu_item = self.driver.find_element(
    #             By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li.sub-menu > a")
    #         actions = ActionChains(self.driver)
    #         actions.move_to_element(main_menu_item).perform()
    #         self.driver.implicitly_wait(10)
    #         time.sleep(5)

    # # TC_73
    # def test73(self):
    #     with open("Data/add_new_group_of_product_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         username = data["test_cases_add_new_group_of_product"][2]["username"]
    #         password = data["test_cases_add_new_group_of_product"][2]["password"]
    #         title = data["test_cases_add_new_group_of_product"][2]["title"]
    #         description = data["test_cases_add_new_group_of_product"][2]["description"]
    #         location = data["test_cases_add_new_group_of_product"][2]["location"]
    #         self.login(username, password)

    #         success_message = self.driver.find_element(
    #             By.CSS_SELECTOR, "body > header > div > div > div.col-3 > div > a").text
    #         # self.driver.save_screenshot('image/pass/1.jpg')
    #         # print(success_message)
    #         # self.assertEqual(success_message, "ADMIN")

    #         # Chọn danh mục sản phẩm
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div.sider > div > ul > li:nth-child(2) > a").click()
    #         time.sleep(5)
    #         # Chọn thêm mới danh mục
    #         self.driver.find_element(
    #             By.XPATH, "/html/body/div/div[2]/div/div[2]/div/div[2]/a").click()

    #         # Điền nội dung tiêu đề
    #         self.driver.find_element(By.ID, "title").send_keys(title)

    #         # Chọn danh mục
    #         select_element = self.driver.find_element(By.ID, "parent_id")
    #         select = Select(select_element)
    #         select.select_by_index(0)  # Danh mục cha ở vị trí 0 (mặc định)
    #         time.sleep(2)

    #         # Điền mô tả vào thẻ iframe
    #         self.driver.switch_to.frame("desc_ifr")
    #         body = self.driver.find_element(By.ID, "tinymce")
    #         body.clear()  # Clear any existing content
    #         body.send_keys(description)
    #         self.driver.switch_to.default_content()
    #         time.sleep(3)

    #         # Upload ảnh
    #         file_input = self.driver.find_element(By.ID, 'thumbnail')
    #         file_path = "D:/Project-managerTest/tests/automation-test/image_for_testing/dog.jpg"
    #         file_input.send_keys(file_path)
    #         time.sleep(3)

    #         # Chọn vị trí
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "#position").send_keys(location)

    #         # Chọn trạng thái Hoạt động/Không hoạt động
    #         # Hoạt động
    #         self.driver.find_element(
    #             By.XPATH, '//*[@id="statusActive"]').click()
    #         # Không hoạt động
    #         # self.driver.find_element(
    #         #     By.XPATH, '//*[@id="statusInActive"]').click()

    #         # Chọn tạo mới
    #         self.driver.find_element(
    #             By.XPATH, '/html/body/div[1]/div[2]/form/div[8]/button').click()
    #         time.sleep(5)

    #         # Kiểm tra xem danh mục mới có xuất hiện bên màn hình user hay ko
    #         self.driver.get('https://storecs.vercel.app/')
    #         main_menu_item = self.driver.find_element(
    #             By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li.sub-menu > a")
    #         actions = ActionChains(self.driver)
    #         actions.move_to_element(main_menu_item).perform()
    #         self.driver.implicitly_wait(10)
    #         time.sleep(5)
    #         # So sánh kết quả với database (thêm sau)

    # # TC_74
    # def test74(self):
    #     with open("Data/add_new_group_of_product_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         username = data["test_cases_add_new_group_of_product"][3]["username"]
    #         password = data["test_cases_add_new_group_of_product"][3]["password"]
    #         title = data["test_cases_add_new_group_of_product"][3]["title"]
    #         description = data["test_cases_add_new_group_of_product"][3]["description"]
    #         location = data["test_cases_add_new_group_of_product"][3]["location"]
    #         self.login(username, password)

    #         success_message = self.driver.find_element(
    #             By.CSS_SELECTOR, "body > header > div > div > div.col-3 > div > a").text
    #         # self.driver.save_screenshot('image/pass/1.jpg')
    #         # print(success_message)
    #         # self.assertEqual(success_message, "ADMIN")

    #         # Chọn danh mục sản phẩm
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div.sider > div > ul > li:nth-child(2) > a").click()
    #         time.sleep(5)
    #         # Chọn thêm mới danh mục
    #         self.driver.find_element(
    #             By.XPATH, "/html/body/div/div[2]/div/div[2]/div/div[2]/a").click()

    #         # Điền nội dung tiêu đề
    #         self.driver.find_element(By.ID, "title").send_keys(title)

    #         # Chọn danh mục
    #         select_element = self.driver.find_element(By.ID, "parent_id")
    #         select = Select(select_element)
    #         select.select_by_index(0)  # Danh mục cha ở vị trí 0 (mặc định)
    #         time.sleep(2)

    #         # Điền mô tả vào thẻ iframe
    #         self.driver.switch_to.frame("desc_ifr")
    #         body = self.driver.find_element(By.ID, "tinymce")
    #         body.clear()  # Clear any existing content
    #         body.send_keys(description)
    #         self.driver.switch_to.default_content()
    #         time.sleep(3)

    #         # Upload ảnh
    #         # file_input = self.driver.find_element(By.ID, 'thumbnail')
    #         # file_path = "D:/Project-managerTest/tests/automation-test/image_for_testing/dog.jpg"
    #         # file_input.send_keys(file_path)
    #         # time.sleep(3)

    #         # Chọn vị trí
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "#position").send_keys(location)

    #         # Chọn trạng thái Hoạt động/Không hoạt động
    #         # Hoạt động
    #         self.driver.find_element(
    #             By.XPATH, '//*[@id="statusActive"]').click()
    #         # Không hoạt động
    #         # self.driver.find_element(
    #         #     By.XPATH, '//*[@id="statusInActive"]').click()

    #         # Chọn tạo mới
    #         self.driver.find_element(
    #             By.XPATH, '/html/body/div[1]/div[2]/form/div[8]/button').click()
    #         time.sleep(5)

    #         # Kiểm tra xem danh mục mới có xuất hiện bên màn hình user hay ko
    #         self.driver.get('https://storecs.vercel.app/')
    #         main_menu_item = self.driver.find_element(
    #             By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li.sub-menu > a")
    #         actions = ActionChains(self.driver)
    #         actions.move_to_element(main_menu_item).perform()
    #         self.driver.implicitly_wait(10)
    #         time.sleep(5)
    #         # So sánh kết quả với database (thêm sau)


if __name__ == "__main__":
    unittest.main()
