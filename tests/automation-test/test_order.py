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
    # TC_50
    # def test50(self):
    #     with open("Data/order_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         username = data["test_cases_order"][0]["username"]
    #         password = data["test_cases_order"][0]["password"]
    #         quantity = data["test_cases_order"][0]["quantity"]
    #         order_username = data["test_cases_order"][0]["order_username"]
    #         order_phone_number = data["test_cases_order"][0]["order_phone_number"]
    #         order_address = data["test_cases_order"][0]["order_address"]
    #         self.login(username, password)
    #         success_message_element_login = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-success"))
    #         )
    #         success_message_login = success_message_element_login.text.strip()

    #         print(success_message_login)
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div:nth-child(3) > div > div:nth-child(2) > div:nth-child(1) > div > div.inner-content > h3 > a").click()
    #         # Xóa ô nhập số lượng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").clear()
    #         # Nhập số lượng cần mua
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").send_keys(quantity)
    #         # Chon buttong đặt hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > button").click()
    #         # Lấy thông tin số lượng sản phẩm có trong giỏ hàng
    #         # quantity_on_cart = self.driver.find_element(
    #         #     By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(3) > a").text
    #         # print(quantity_on_cart)

    #         # Chọn giỏ hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(3) > a").click()

    #         # Chọn thanh toán
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(2) > div > div > a").click()
    #         # time.sleep(5)
    #         # Điền thông tin nhận hàng
    #         self.driver.find_element(
    #             By.ID, "fullName").send_keys(order_username)
    #         self.driver.find_element(
    #             By.ID, "phone").send_keys(order_phone_number)
    #         self.driver.find_element(By.ID, "address").send_keys(order_address)

    #         # Chọn đặt hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(3) > div > div > form > div:nth-child(4) > button").click()

    #         # Thông báo đặt hàng thành công
    #         success_message = self.driver.find_element(
    #             By.CSS_SELECTOR, 'body > div > div:nth-child(2) > div > div').text
    #         print(success_message)
    #         self.assertEqual(
    #             success_message, "Chúc mừng bạn đã đặt hàng thành công! Chúng tôi sẽ xử lý đơn hàng trong thời gian sớm nhất.")

    #         # Vào tài khoảng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(4) > a").click()
    #         # Tìm xem có tên đơn vừa đặt ko
    #         rows = self.driver.find_elements(
    #             By.XPATH, '//table[@class="table table-hover table-sm"]/tbody/tr')

    #         # Duyệt qua các hàng và tìm đơn hàng có Họ tên như đã nhập ko
    #         for row in rows:
    #             name = row.find_element(By.XPATH, './td[2]/p').text
    #             if name == order_username:
    #                 # Tìm liên kết "Xem" trong hàng này
    #                 # view_link = row.find_element(
    #                 #     By.XPATH, './td[5]/a[@class="btn btn-secondary btn-sm"]').get_attribute('href')
    #                 # print(
    #                 #     f'Link to view order for Nguyễn Trương Xuân Nghiêm: {view_link}')
    #                 view_button = row.find_element(
    #                     By.XPATH, './td[5]/a[@class="btn btn-secondary btn-sm"]')
    #                 view_link = view_button.get_attribute('href')
    #                 self.driver.get(view_link)
    #                 time.sleep(3)
    #                 print(
    #                     f'Navigated to link for {order_username}: {view_link}')

    #                 break
    # # So sánh thông tin đơn hàng với nội dung khách đã nhập trc đó (Thêm sau)

    # # TC_51
    # def test51(self):
    #     with open("Data/order_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         username = data["test_cases_order"][1]["username"]
    #         password = data["test_cases_order"][1]["password"]
    #         quantity = data["test_cases_order"][1]["quantity"]
    #         order_username = data["test_cases_order"][1]["order_username"]
    #         order_phone_number = data["test_cases_order"][1]["order_phone_number"]
    #         order_address = data["test_cases_order"][1]["order_address"]
    #         self.login(username, password)
    #         success_message_element_login = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-success"))
    #         )
    #         success_message_login = success_message_element_login.text.strip()

    #         print(success_message_login)
    #         # Chọn sản phẩm 1 cần mua
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div:nth-child(3) > div > div:nth-child(2) > div:nth-child(1) > div > div.inner-content > h3 > a").click()
    #         # Xóa ô nhập số lượng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").clear()
    #         # Nhập số lượng cần mua
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").send_keys(quantity)
    #         # Chon buttong thêm vào giỏ hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > button").click()

    #         time.sleep(3)
    #         # Về trang chủ để đặt hàng tiếp
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(1) > a").click()
    #         time.sleep(5)
    #         # Chọn sản phẩm 2 cần mua
    #         self.driver.find_element(
    #             By.XPATH, "/html/body/div[1]/div/div[2]/div[4]/div/div[2]/h3/a").click()
    #         time.sleep(5)
    #         # Xóa ô nhập số lượng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").clear()
    #         # Nhập số lượng cần mua
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").send_keys(quantity)
    #         # Chon button thêm vào giỏ hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > button").click()

    #         # Lấy thông tin số lượng sản phẩm có trong giỏ hàng
    #         # quantity_on_cart = self.driver.find_element(
    #         #     By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(3) > a").text
    #         # print(quantity_on_cart)

    #         # Chọn giỏ hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(3) > a").click()

    #         # Chọn thanh toán
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(2) > div > div > a").click()
    #         # time.sleep(5)
    #         # Điền thông tin nhận hàng
    #         self.driver.find_element(
    #             By.ID, "fullName").send_keys(order_username)
    #         self.driver.find_element(
    #             By.ID, "phone").send_keys(order_phone_number)
    #         self.driver.find_element(By.ID, "address").send_keys(order_address)

    #         # Chọn đặt hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(3) > div > div > form > div:nth-child(4) > button").click()

    #         # Thông báo đặt hàng thành công
    #         success_message = self.driver.find_element(
    #             By.CSS_SELECTOR, 'body > div > div:nth-child(2) > div > div').text
    #         print(success_message)
    #         self.assertEqual(
    #             success_message, "Chúc mừng bạn đã đặt hàng thành công! Chúng tôi sẽ xử lý đơn hàng trong thời gian sớm nhất.")

    #         # Vào tài khoảng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(4) > a").click()
    #         # Tìm xem có tên đơn vừa đặt ko
    #         rows = self.driver.find_elements(
    #             By.XPATH, '//table[@class="table table-hover table-sm"]/tbody/tr')

    #         # Duyệt qua các hàng và tìm đơn hàng có Họ tên như đã nhập ko
    #         for row in rows:
    #             name = row.find_element(By.XPATH, './td[2]/p').text
    #             if name == order_username:
    #                 # Tìm liên kết "Xem" trong hàng này
    #                 # view_link = row.find_element(
    #                 #     By.XPATH, './td[5]/a[@class="btn btn-secondary btn-sm"]').get_attribute('href')
    #                 # print(
    #                 #     f'Link to view order for Nguyễn Trương Xuân Nghiêm: {view_link}')
    #                 view_button = row.find_element(
    #                     By.XPATH, './td[5]/a[@class="btn btn-secondary btn-sm"]')
    #                 view_link = view_button.get_attribute('href')
    #                 self.driver.get(view_link)
    #                 time.sleep(3)
    #                 print(
    #                     f'Navigated to link for {order_username}: {view_link}')

    #                 break

    # # Negative Case
    # # TC_52
    # def test52(self):
    #     with open("Data/order_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         username = data["test_cases_order"][2]["username"]
    #         password = data["test_cases_order"][2]["password"]
    #         quantity = data["test_cases_order"][2]["quantity"]
    #         order_username = data["test_cases_order"][2]["order_username"]
    #         order_phone_number = data["test_cases_order"][2]["order_phone_number"]
    #         order_address = data["test_cases_order"][2]["order_address"]
    #         self.login(username, password)
    #         success_message_element_login = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-success"))
    #         )
    #         success_message_login = success_message_element_login.text.strip()

    #         print(success_message_login)
    #         # Chọn sản phẩm 1 cần mua
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div:nth-child(3) > div > div:nth-child(2) > div:nth-child(1) > div > div.inner-content > h3 > a").click()
    #         # Xóa ô nhập số lượng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").clear()
    #         # Nhập số lượng cần mua
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").send_keys(quantity)
    #         # Chon buttong thêm vào giỏ hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > button").click()

    #         # Lấy thông tin số lượng sản phẩm có trong giỏ hàng
    #         # quantity_on_cart = self.driver.find_element(
    #         #     By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(3) > a").text
    #         # print(quantity_on_cart)

    #         # Chọn giỏ hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(3) > a").click()

    #         # Chọn thanh toán
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(2) > div > div > a").click()
    #         # time.sleep(5)
    #         # Điền thông tin nhận hàng
    #         self.driver.find_element(
    #             By.ID, "fullName").send_keys(order_username)
    #         self.driver.find_element(
    #             By.ID, "phone").send_keys(order_phone_number)
    #         self.driver.find_element(By.ID, "address").send_keys(order_address)

    #         # Chọn đặt hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(3) > div > div > form > div:nth-child(4) > button").click()

    #         error_message = self.driver.find_element(
    #             By.ID, 'fullName').get_attribute("validationMessage")
    #         # self.driver.save_screenshot('image/pass/3.jpg')
    #         print(error_message)
    #         self.assertEqual(error_message, "Please fill out this field.")

    # # TC_53
    # def test53(self):
    #     with open("Data/order_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         username = data["test_cases_order"][3]["username"]
    #         password = data["test_cases_order"][3]["password"]
    #         quantity = data["test_cases_order"][3]["quantity"]
    #         order_username = data["test_cases_order"][3]["order_username"]
    #         order_phone_number = data["test_cases_order"][3]["order_phone_number"]
    #         order_address = data["test_cases_order"][3]["order_address"]
    #         self.login(username, password)
    #         success_message_element_login = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-success"))
    #         )
    #         success_message_login = success_message_element_login.text.strip()

    #         print(success_message_login)
    #         # Chọn sản phẩm 1 cần mua
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div:nth-child(3) > div > div:nth-child(2) > div:nth-child(1) > div > div.inner-content > h3 > a").click()
    #         # Xóa ô nhập số lượng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").clear()
    #         # Nhập số lượng cần mua
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").send_keys(quantity)
    #         # Chon buttong thêm vào giỏ hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > button").click()

    #         # Lấy thông tin số lượng sản phẩm có trong giỏ hàng
    #         # quantity_on_cart = self.driver.find_element(
    #         #     By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(3) > a").text
    #         # print(quantity_on_cart)

    #         # Chọn giỏ hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(3) > a").click()

    #         # Chọn thanh toán
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(2) > div > div > a").click()
    #         # time.sleep(5)
    #         # Điền thông tin nhận hàng
    #         self.driver.find_element(
    #             By.ID, "fullName").send_keys(order_username)
    #         self.driver.find_element(
    #             By.ID, "phone").send_keys(order_phone_number)
    #         self.driver.find_element(By.ID, "address").send_keys(order_address)

    #         # Chọn đặt hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(3) > div > div > form > div:nth-child(4) > button").click()

    #         error_message = self.driver.find_element(
    #             By.ID, 'fullName').get_attribute("validationMessage")
    #         # self.driver.save_screenshot('image/pass/3.jpg')
    #         print(error_message)
    #         self.assertEqual(error_message, "Please fill out this field.")

    # TC_54
    # def test54(self):
    #     with open("Data/order_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         username = data["test_cases_order"][4]["username"]
    #         password = data["test_cases_order"][4]["password"]
    #         quantity = data["test_cases_order"][4]["quantity"]
    #         order_username = data["test_cases_order"][4]["order_username"]
    #         order_phone_number = data["test_cases_order"][4]["order_phone_number"]
    #         order_address = data["test_cases_order"][4]["order_address"]
    #         self.login(username, password)
    #         success_message_element_login = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-success"))
    #         )
    #         success_message_login = success_message_element_login.text.strip()

    #         print(success_message_login)
    #         # Chọn sản phẩm 1 cần mua
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div:nth-child(3) > div > div:nth-child(2) > div:nth-child(1) > div > div.inner-content > h3 > a").click()
    #         # Xóa ô nhập số lượng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").clear()
    #         # Nhập số lượng cần mua
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").send_keys(quantity)
    #         # Chon buttong thêm vào giỏ hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > button").click()

    #         # Lấy thông tin số lượng sản phẩm có trong giỏ hàng
    #         # quantity_on_cart = self.driver.find_element(
    #         #     By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(3) > a").text
    #         # print(quantity_on_cart)

    #         # Chọn giỏ hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(3) > a").click()

    #         # Chọn thanh toán
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(2) > div > div > a").click()
    #         # time.sleep(5)
    #         # Điền thông tin nhận hàng
    #         self.driver.find_element(
    #             By.ID, "fullName").send_keys(order_username)
    #         self.driver.find_element(
    #             By.ID, "phone").send_keys(order_phone_number)
    #         self.driver.find_element(By.ID, "address").send_keys(order_address)

    #         # Chọn đặt hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(3) > div > div > form > div:nth-child(4) > button").click()

    #         error_message_element = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-success"))
    #         )
    #         error_message = error_message_element.text.strip()
    #         self.driver.save_screenshot('image/fail/54.jpg')
    #         print(error_message)
    #         self.assertEqual(error_message, "Họ tên không hợp lệ x")

    # TC_55
    # def test55(self):
    #     with open("Data/order_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         username = data["test_cases_order"][5]["username"]
    #         password = data["test_cases_order"][5]["password"]
    #         quantity = data["test_cases_order"][5]["quantity"]
    #         order_username = data["test_cases_order"][5]["order_username"]
    #         order_phone_number = data["test_cases_order"][5]["order_phone_number"]
    #         order_address = data["test_cases_order"][5]["order_address"]
    #         self.login(username, password)
    #         success_message_element_login = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-success"))
    #         )
    #         success_message_login = success_message_element_login.text.strip()

    #         print(success_message_login)
    #         # Chọn sản phẩm 1 cần mua
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div:nth-child(3) > div > div:nth-child(2) > div:nth-child(1) > div > div.inner-content > h3 > a").click()
    #         # Xóa ô nhập số lượng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").clear()
    #         # Nhập số lượng cần mua
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").send_keys(quantity)
    #         # Chon buttong thêm vào giỏ hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > button").click()

    #         # Lấy thông tin số lượng sản phẩm có trong giỏ hàng
    #         # quantity_on_cart = self.driver.find_element(
    #         #     By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(3) > a").text
    #         # print(quantity_on_cart)

    #         # Chọn giỏ hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(3) > a").click()

    #         # Chọn thanh toán
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(2) > div > div > a").click()
    #         # time.sleep(5)
    #         # Điền thông tin nhận hàng
    #         self.driver.find_element(
    #             By.ID, "fullName").send_keys(order_username)
    #         self.driver.find_element(
    #             By.ID, "phone").send_keys(order_phone_number)
    #         self.driver.find_element(By.ID, "address").send_keys(order_address)

    #         # Chọn đặt hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(3) > div > div > form > div:nth-child(4) > button").click()

    #         error_message = self.driver.find_element(
    #             By.ID, 'phone').get_attribute("validationMessage")
    #         # self.driver.save_screenshot('image/pass/3.jpg')
    #         print(error_message)
    #         self.assertEqual(error_message, "Please fill out this field.")

    # TC_56
    def test56(self):
        with open("Data/order_function_data.json", encoding="utf-8") as f:
            data = json.load(f)
            username = data["test_cases_order"][6]["username"]
            password = data["test_cases_order"][6]["password"]
            quantity = data["test_cases_order"][6]["quantity"]
            order_username = data["test_cases_order"][6]["order_username"]
            order_phone_number = data["test_cases_order"][6]["order_phone_number"]
            order_address = data["test_cases_order"][6]["order_address"]
            self.login(username, password)
            success_message_element_login = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "alert-success"))
            )
            success_message_login = success_message_element_login.text.strip()

            print(success_message_login)
            # Chọn sản phẩm 1 cần mua
            self.driver.find_element(
                By.CSS_SELECTOR, "body > div:nth-child(3) > div > div:nth-child(2) > div:nth-child(1) > div > div.inner-content > h3 > a").click()
            # Xóa ô nhập số lượng
            self.driver.find_element(
                By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").clear()
            # Nhập số lượng cần mua
            self.driver.find_element(
                By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").send_keys(quantity)
            # Chon buttong thêm vào giỏ hàng
            self.driver.find_element(
                By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > button").click()

            # Lấy thông tin số lượng sản phẩm có trong giỏ hàng
            # quantity_on_cart = self.driver.find_element(
            #     By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(3) > a").text
            # print(quantity_on_cart)

            # Chọn giỏ hàng
            self.driver.find_element(
                By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(3) > a").click()

            # Chọn thanh toán
            self.driver.find_element(
                By.CSS_SELECTOR, "body > div > div:nth-child(2) > div > div > a").click()
            # time.sleep(5)
            # Điền thông tin nhận hàng
            self.driver.find_element(
                By.ID, "fullName").send_keys(order_username)
            self.driver.find_element(
                By.ID, "phone").send_keys(order_phone_number)
            self.driver.find_element(By.ID, "address").send_keys(order_address)

            # Chọn đặt hàng
            self.driver.find_element(
                By.CSS_SELECTOR, "body > div > div:nth-child(3) > div > div > form > div:nth-child(4) > button").click()

            error_message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "alert-success"))
            )
            error_message = error_message_element.text.strip()
            self.driver.save_screenshot('image/fail/TC_56.jpg')
            print(error_message)
            self.assertEqual(error_message, "Số điện thoại không hợp lệ x")

    # # TC_57
    # def test57(self):
    #     with open("Data/order_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         username = data["test_cases_order"][7]["username"]
    #         password = data["test_cases_order"][7]["password"]
    #         quantity = data["test_cases_order"][7]["quantity"]
    #         order_username = data["test_cases_order"][7]["order_username"]
    #         order_phone_number = data["test_cases_order"][7]["order_phone_number"]
    #         order_address = data["test_cases_order"][7]["order_address"]
    #         self.login(username, password)
    #         success_message_element_login = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-success"))
    #         )
    #         success_message_login = success_message_element_login.text.strip()

    #         print(success_message_login)
    #         # Chọn sản phẩm 1 cần mua
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div:nth-child(3) > div > div:nth-child(2) > div:nth-child(1) > div > div.inner-content > h3 > a").click()
    #         # Xóa ô nhập số lượng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").clear()
    #         # Nhập số lượng cần mua
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").send_keys(quantity)
    #         # Chon buttong thêm vào giỏ hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > button").click()

    #         # Lấy thông tin số lượng sản phẩm có trong giỏ hàng
    #         # quantity_on_cart = self.driver.find_element(
    #         #     By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(3) > a").text
    #         # print(quantity_on_cart)

    #         # Chọn giỏ hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(3) > a").click()

    #         # Chọn thanh toán
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(2) > div > div > a").click()
    #         # time.sleep(5)
    #         # Điền thông tin nhận hàng
    #         self.driver.find_element(
    #             By.ID, "fullName").send_keys(order_username)
    #         self.driver.find_element(
    #             By.ID, "phone").send_keys(order_phone_number)
    #         self.driver.find_element(By.ID, "address").send_keys(order_address)

    #         # Chọn đặt hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(3) > div > div > form > div:nth-child(4) > button").click()

    #         error_message_element = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-success"))
    #         )
    #         error_message = error_message_element.text.strip()
    #         self.driver.save_screenshot('image/fail/TC_57.jpg')
    #         print(error_message)
    #         self.assertEqual(error_message, "Số điện thoại không hợp lệ x")

    # TC_58
    # def test58(self):
    #     with open("Data/order_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         username = data["test_cases_order"][8]["username"]
    #         password = data["test_cases_order"][8]["password"]
    #         quantity = data["test_cases_order"][8]["quantity"]
    #         order_username = data["test_cases_order"][8]["order_username"]
    #         order_phone_number = data["test_cases_order"][8]["order_phone_number"]
    #         order_address = data["test_cases_order"][8]["order_address"]
    #         self.login(username, password)
    #         success_message_element_login = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-success"))
    #         )
    #         success_message_login = success_message_element_login.text.strip()

    #         print(success_message_login)
    #         # Chọn sản phẩm 1 cần mua
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div:nth-child(3) > div > div:nth-child(2) > div:nth-child(1) > div > div.inner-content > h3 > a").click()
    #         # Xóa ô nhập số lượng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").clear()
    #         # Nhập số lượng cần mua
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").send_keys(quantity)
    #         # Chon buttong thêm vào giỏ hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > button").click()

    #         # Lấy thông tin số lượng sản phẩm có trong giỏ hàng
    #         # quantity_on_cart = self.driver.find_element(
    #         #     By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(3) > a").text
    #         # print(quantity_on_cart)

    #         # Chọn giỏ hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(3) > a").click()

    #         # Chọn thanh toán
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(2) > div > div > a").click()
    #         # time.sleep(5)
    #         # Điền thông tin nhận hàng
    #         self.driver.find_element(
    #             By.ID, "fullName").send_keys(order_username)
    #         self.driver.find_element(
    #             By.ID, "phone").send_keys(order_phone_number)
    #         self.driver.find_element(By.ID, "address").send_keys(order_address)

    #         # Chọn đặt hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(3) > div > div > form > div:nth-child(4) > button").click()

    #         error_message_element = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-success"))
    #         )
    #         error_message = error_message_element.text.strip()
    #         self.driver.save_screenshot('image/fail/TC_58.jpg')
    #         print(error_message)
    #         self.assertEqual(error_message, "Số điện thoại không hợp lệ x")

    # # TC_59
    # def test59(self):
    #     with open("Data/order_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         username = data["test_cases_order"][9]["username"]
    #         password = data["test_cases_order"][9]["password"]
    #         quantity = data["test_cases_order"][9]["quantity"]
    #         order_username = data["test_cases_order"][9]["order_username"]
    #         order_phone_number = data["test_cases_order"][9]["order_phone_number"]
    #         order_address = data["test_cases_order"][9]["order_address"]
    #         self.login(username, password)
    #         success_message_element_login = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-success"))
    #         )
    #         success_message_login = success_message_element_login.text.strip()

    #         print(success_message_login)
    #         # Chọn sản phẩm 1 cần mua
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div:nth-child(3) > div > div:nth-child(2) > div:nth-child(1) > div > div.inner-content > h3 > a").click()
    #         # Xóa ô nhập số lượng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").clear()
    #         # Nhập số lượng cần mua
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").send_keys(quantity)
    #         # Chon buttong thêm vào giỏ hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > button").click()

    #         # Lấy thông tin số lượng sản phẩm có trong giỏ hàng
    #         # quantity_on_cart = self.driver.find_element(
    #         #     By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(3) > a").text
    #         # print(quantity_on_cart)

    #         # Chọn giỏ hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(3) > a").click()

    #         # Chọn thanh toán
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(2) > div > div > a").click()
    #         # time.sleep(5)
    #         # Điền thông tin nhận hàng
    #         self.driver.find_element(
    #             By.ID, "fullName").send_keys(order_username)
    #         self.driver.find_element(
    #             By.ID, "phone").send_keys(order_phone_number)
    #         self.driver.find_element(By.ID, "address").send_keys(order_address)

    #         # Chọn đặt hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(3) > div > div > form > div:nth-child(4) > button").click()

    #         error_message = self.driver.find_element(
    #             By.ID, 'address').get_attribute("validationMessage")
    #         # self.driver.save_screenshot('image/pass/3.jpg')
    #         print(error_message)
    #         self.assertEqual(error_message, "Please fill out this field.")

    # # TC_60
    # def test60(self):
    #     with open("Data/order_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         username = data["test_cases_order"][10]["username"]
    #         password = data["test_cases_order"][10]["password"]
    #         quantity = data["test_cases_order"][10]["quantity"]
    #         order_username = data["test_cases_order"][10]["order_username"]
    #         order_phone_number = data["test_cases_order"][10]["order_phone_number"]
    #         order_address = data["test_cases_order"][10]["order_address"]
    #         self.login(username, password)
    #         success_message_element_login = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-success"))
    #         )
    #         success_message_login = success_message_element_login.text.strip()

    #         print(success_message_login)
    #         # Chọn sản phẩm 1 cần mua
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div:nth-child(3) > div > div:nth-child(2) > div:nth-child(1) > div > div.inner-content > h3 > a").click()
    #         # Xóa ô nhập số lượng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").clear()
    #         # Nhập số lượng cần mua
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").send_keys(quantity)
    #         # Chon buttong thêm vào giỏ hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > button").click()

    #         # Lấy thông tin số lượng sản phẩm có trong giỏ hàng
    #         # quantity_on_cart = self.driver.find_element(
    #         #     By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(3) > a").text
    #         # print(quantity_on_cart)

    #         # Chọn giỏ hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(3) > a").click()

    #         # Chọn thanh toán
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(2) > div > div > a").click()
    #         # time.sleep(5)
    #         # Điền thông tin nhận hàng
    #         self.driver.find_element(
    #             By.ID, "fullName").send_keys(order_username)
    #         self.driver.find_element(
    #             By.ID, "phone").send_keys(order_phone_number)
    #         self.driver.find_element(By.ID, "address").send_keys(order_address)

    #         # Chọn đặt hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(3) > div > div > form > div:nth-child(4) > button").click()

    #         error_message_element = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-success"))
    #         )
    #         error_message = error_message_element.text.strip()
    #         self.driver.save_screenshot('image/fail/TC_60.jpg')
    #         print(error_message)
    #         self.assertEqual(error_message, "Địa chỉ không hợp lệ x")

    # # TC_61
    # def test61(self):
    #     with open("Data/order_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         username = data["test_cases_order"][11]["username"]
    #         password = data["test_cases_order"][11]["password"]
    #         quantity = data["test_cases_order"][11]["quantity"]
    #         order_username = data["test_cases_order"][11]["order_username"]
    #         order_phone_number = data["test_cases_order"][11]["order_phone_number"]
    #         order_address = data["test_cases_order"][11]["order_address"]
    #         self.login(username, password)
    #         success_message_element_login = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-success"))
    #         )
    #         success_message_login = success_message_element_login.text.strip()

    #         print(success_message_login)
    #         # Chọn sản phẩm 1 cần mua
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div:nth-child(3) > div > div:nth-child(2) > div:nth-child(1) > div > div.inner-content > h3 > a").click()
    #         # Xóa ô nhập số lượng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").clear()
    #         # Nhập số lượng cần mua
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > input").send_keys(quantity)
    #         # Chon buttong thêm vào giỏ hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(1) > div > div:nth-child(2) > form > button").click()

    #         # Lấy thông tin số lượng sản phẩm có trong giỏ hàng
    #         # quantity_on_cart = self.driver.find_element(
    #         #     By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(3) > a").text
    #         # print(quantity_on_cart)

    #         # Chọn giỏ hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > header > div > div > div.col-4 > div > ul > li:nth-child(3) > a").click()

    #         # Chọn thanh toán
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(2) > div > div > a").click()
    #         # time.sleep(5)
    #         # Điền thông tin nhận hàng
    #         self.driver.find_element(
    #             By.ID, "fullName").send_keys(order_username)
    #         self.driver.find_element(
    #             By.ID, "phone").send_keys(order_phone_number)
    #         self.driver.find_element(By.ID, "address").send_keys(order_address)

    #         # Chọn đặt hàng
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > div > div:nth-child(3) > div > div > form > div:nth-child(4) > button").click()

    #         error_message_element = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.CLASS_NAME, "alert-success"))
    #         )
    #         error_message = error_message_element.text.strip()
    #         self.driver.save_screenshot('image/fail/TC_61.jpg')
    #         print(error_message)
    #         self.assertEqual(error_message, "Địa chỉ không hợp lệ x")


if __name__ == "__main__":
    unittest.main()
