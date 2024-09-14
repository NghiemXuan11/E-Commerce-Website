from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest
import json

# # Khởi tạo trình duyệt
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# try:
#     # Mở trang web (đặt URL của trang web chứa đoạn HTML trên)
#     driver.get('https://storecs.vercel.app/')

#     # Đợi một chút để đảm bảo trang tải hoàn toàn
#     time.sleep(3)

#     # Tìm nút tìm kiếm và click vào nó
#     # Thay 'search-button-id' bằng ID thực của nút tìm kiếm
#     search_button = driver.find_element(
#         By.CSS_SELECTOR, 'body > header > div > div > div.col-5 > form > div > button')
#     search_button.click()

#     # Đợi một chút để đảm bảo kết quả tìm kiếm tải hoàn toàn
#     time.sleep(3)

#     # Tìm tất cả các sản phẩm
#     product_items = driver.find_elements(By.CLASS_NAME, 'product-item')

#     # In thông tin về từng sản phẩm
#     for product in product_items:
#         title = product.find_element(By.CLASS_NAME, 'inner-title').text
#         price_new = product.find_element(By.CLASS_NAME, 'inner-price-new').text
#         price_old = product.find_element(By.CLASS_NAME, 'inner-price-old').text
#         discount = product.find_element(By.CLASS_NAME, 'inner-discount').text
#         print(
#             f"Title: {title}, New Price: {price_new}, Old Price: {price_old}, Discount: {discount}")

# finally:
#     # Đóng trình duyệt
#     driver.quit()


class TestRegisterFunction(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://storecs.vercel.app/')

    def tearDown(self):
        self.driver.quit()

    # Happy Cases
    # TC_36
    # def test36(self):
    #     # Đợi một chút để đảm bảo trang tải hoàn toàn
    #     time.sleep(3)
    #     with open("Data/searching_function_data.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         keyword = data["test_cases_searching"][0]["keyword"]
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > header > div > div > div.col-5 > form > div > input").send_keys(keyword)
    #         # Tìm nút tìm kiếm và click vào nó
    #         # Thay 'search-button-id' bằng ID thực của nút tìm kiếm
    #         search_button = self.driver.find_element(
    #             By.CSS_SELECTOR, 'body > header > div > div > div.col-5 > form > div > button')
    #         search_button.click()

    #         # Đợi một chút để đảm bảo kết quả tìm kiếm tải hoàn toàn
    #         time.sleep(3)
    #         self.driver.save_screenshot('image/fail/TC_36.jpg')
    #         # Tìm tất cả các sản phẩm
    #         product_items = self.driver.find_elements(
    #             By.CLASS_NAME, 'product-item')

    #         # In thông tin về từng sản phẩm
    #         for product in product_items:
    #             title = product.find_element(By.CLASS_NAME, 'inner-title').text
    #             price_new = product.find_element(
    #                 By.CLASS_NAME, 'inner-price-new').text
    #             price_old = product.find_element(
    #                 By.CLASS_NAME, 'inner-price-old').text
    #             discount = product.find_element(
    #                 By.CLASS_NAME, 'inner-discount').text
    #             print(
    #                 f"Title: {title}, New Price: {price_new}, Old Price: {price_old}, Discount: {discount}")

    # TC_37
    def test37(self):
        # Đợi một chút để đảm bảo trang tải hoàn toàn
        time.sleep(3)
        with open("Data/searching_function_data.json", encoding="utf-8") as f:
            data = json.load(f)
            keyword = data["test_cases_searching"][1]["keyword"]
            self.driver.find_element(
                By.CSS_SELECTOR, "body > header > div > div > div.col-5 > form > div > input").send_keys(keyword)
            # Tìm nút tìm kiếm và click vào nó
            # Thay 'search-button-id' bằng ID thực của nút tìm kiếm
            search_button = self.driver.find_element(
                By.CSS_SELECTOR, 'body > header > div > div > div.col-5 > form > div > button')
            search_button.click()

            # Đợi một chút để đảm bảo kết quả tìm kiếm tải hoàn toàn
            time.sleep(3)
            self.driver.save_screenshot('image/fail/TC_37.jpg')
            # Tìm tất cả các sản phẩm
            product_items = self.driver.find_elements(
                By.CLASS_NAME, 'product-item')

            # In thông tin về từng sản phẩm
            for product in product_items:
                title = product.find_element(By.CLASS_NAME, 'inner-title').text
                price_new = product.find_element(
                    By.CLASS_NAME, 'inner-price-new').text
                price_old = product.find_element(
                    By.CLASS_NAME, 'inner-price-old').text
                discount = product.find_element(
                    By.CLASS_NAME, 'inner-discount').text
                print(
                    f"Title: {title}, New Price: {price_new}, Old Price: {price_old}, Discount: {discount}")

    # TC_38
    def test38(self):
        # Đợi một chút để đảm bảo trang tải hoàn toàn
        time.sleep(3)
        with open("Data/searching_function_data.json", encoding="utf-8") as f:
            data = json.load(f)
            keyword = data["test_cases_searching"][2]["keyword"]
            self.driver.find_element(
                By.CSS_SELECTOR, "body > header > div > div > div.col-5 > form > div > input").send_keys(keyword)
            # Tìm nút tìm kiếm và click vào nó
            # Thay 'search-button-id' bằng ID thực của nút tìm kiếm
            search_button = self.driver.find_element(
                By.CSS_SELECTOR, 'body > header > div > div > div.col-5 > form > div > button')
            search_button.click()

            # Đợi một chút để đảm bảo kết quả tìm kiếm tải hoàn toàn
            time.sleep(3)
            self.driver.save_screenshot('image/fail/TC_38.jpg')
            # Tìm tất cả các sản phẩm
            product_items = self.driver.find_elements(
                By.CLASS_NAME, 'product-item')

            # In thông tin về từng sản phẩm
            for product in product_items:
                title = product.find_element(By.CLASS_NAME, 'inner-title').text
                price_new = product.find_element(
                    By.CLASS_NAME, 'inner-price-new').text
                price_old = product.find_element(
                    By.CLASS_NAME, 'inner-price-old').text
                discount = product.find_element(
                    By.CLASS_NAME, 'inner-discount').text
                print(
                    f"Title: {title}, New Price: {price_new}, Old Price: {price_old}, Discount: {discount}")

    # TC_39
    def test39(self):
        # Đợi một chút để đảm bảo trang tải hoàn toàn
        time.sleep(3)
        with open("Data/searching_function_data.json", encoding="utf-8") as f:
            data = json.load(f)
            keyword = data["test_cases_searching"][3]["keyword"]
            self.driver.find_element(
                By.CSS_SELECTOR, "body > header > div > div > div.col-5 > form > div > input").send_keys(keyword)
            # Tìm nút tìm kiếm và click vào nó
            # Thay 'search-button-id' bằng ID thực của nút tìm kiếm
            search_button = self.driver.find_element(
                By.CSS_SELECTOR, 'body > header > div > div > div.col-5 > form > div > button')
            search_button.click()

            # Đợi một chút để đảm bảo kết quả tìm kiếm tải hoàn toàn
            time.sleep(3)

            # Tìm tất cả các sản phẩm
            product_items = self.driver.find_elements(
                By.CLASS_NAME, 'product-item')
            self.driver.save_screenshot('image/fail/TC_39.jpg')
            # In thông tin về từng sản phẩm
            for product in product_items:
                title = product.find_element(By.CLASS_NAME, 'inner-title').text
                price_new = product.find_element(
                    By.CLASS_NAME, 'inner-price-new').text
                price_old = product.find_element(
                    By.CLASS_NAME, 'inner-price-old').text
                discount = product.find_element(
                    By.CLASS_NAME, 'inner-discount').text
                print(
                    f"Title: {title}, New Price: {price_new}, Old Price: {price_old}, Discount: {discount}")

    # Negative Cases
    # TC_40
    # def test40(self):
    #     # Đợi một chút để đảm bảo trang tải hoàn toàn
    #     time.sleep(3)
    #     with open("Data/searching_function.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         keyword = data["test_cases_searching"][4]["keyword"]
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > header > div > div > div.col-5 > form > div > input").send_keys(keyword)
    #         # Tìm nút tìm kiếm và click vào nó
    #         # Thay 'search-button-id' bằng ID thực của nút tìm kiếm
    #         search_button = self.driver.find_element(
    #             By.CSS_SELECTOR, 'body > header > div > div > div.col-5 > form > div > button')
    #         search_button.click()

    #         # Đợi một chút để đảm bảo kết quả tìm kiếm tải hoàn toàn
    #         time.sleep(3)

    #         # Tìm tất cả các sản phẩm
    #         product_items = self.driver.find_elements(
    #             By.CLASS_NAME, 'product-item')

    #         # In thông tin về từng sản phẩm
    #         for product in product_items:
    #             title = product.find_element(By.CLASS_NAME, 'inner-title').text
    #             price_new = product.find_element(
    #                 By.CLASS_NAME, 'inner-price-new').text
    #             price_old = product.find_element(
    #                 By.CLASS_NAME, 'inner-price-old').text
    #             discount = product.find_element(
    #                 By.CLASS_NAME, 'inner-discount').text
    #             print(
    #                 f"Title: {title}, New Price: {price_new}, Old Price: {price_old}, Discount: {discount}")

    #         message = self.driver.find_element(
    #             By.CSS_SELECTOR, 'body > div > div:nth-child(2) > div > div').text
    #         print(message)
    #         self.assertEqual(message, "Không tìm thấy sản phẩm nào.")

    # TC_41
    # def test41(self):
    #     # Đợi một chút để đảm bảo trang tải hoàn toàn
    #     time.sleep(3)
    #     with open("Data/searching_function.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         keyword = data["test_cases_searching"][5]["keyword"]
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > header > div > div > div.col-5 > form > div > input").send_keys(keyword)
    #         # Tìm nút tìm kiếm và click vào nó
    #         # Thay 'search-button-id' bằng ID thực của nút tìm kiếm
    #         search_button = self.driver.find_element(
    #             By.CSS_SELECTOR, 'body > header > div > div > div.col-5 > form > div > button')
    #         search_button.click()

    #         # Đợi một chút để đảm bảo kết quả tìm kiếm tải hoàn toàn
    #         time.sleep(3)

    #         # Tìm tất cả các sản phẩm
    #         product_items = self.driver.find_elements(
    #             By.CLASS_NAME, 'product-item')

    #         # In thông tin về từng sản phẩm
    #         for product in product_items:
    #             title = product.find_element(By.CLASS_NAME, 'inner-title').text
    #             price_new = product.find_element(
    #                 By.CLASS_NAME, 'inner-price-new').text
    #             price_old = product.find_element(
    #                 By.CLASS_NAME, 'inner-price-old').text
    #             discount = product.find_element(
    #                 By.CLASS_NAME, 'inner-discount').text
    #             print(
    #                 f"Title: {title}, New Price: {price_new}, Old Price: {price_old}, Discount: {discount}")

    #         message = self.driver.find_element(
    #             By.CSS_SELECTOR, 'body > div > div:nth-child(2) > div > div').text
    #         print(message)
    #         self.assertEqual(message, "Không tìm thấy sản phẩm nào.")

    # TC_42
    # def test42(self):
    #     # Đợi một chút để đảm bảo trang tải hoàn toàn
    #     time.sleep(3)
    #     with open("Data/searching_function.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         keyword = data["test_cases_searching"][6]["keyword"]
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > header > div > div > div.col-5 > form > div > input").send_keys(keyword)
    #         # Tìm nút tìm kiếm và click vào nó
    #         # Thay 'search-button-id' bằng ID thực của nút tìm kiếm
    #         search_button = self.driver.find_element(
    #             By.CSS_SELECTOR, 'body > header > div > div > div.col-5 > form > div > button')
    #         search_button.click()

    #         # Đợi một chút để đảm bảo kết quả tìm kiếm tải hoàn toàn
    #         time.sleep(3)

    #         # Tìm tất cả các sản phẩm
    #         product_items = self.driver.find_elements(
    #             By.CLASS_NAME, 'product-item')

    #         # In thông tin về từng sản phẩm
    #         for product in product_items:
    #             title = product.find_element(By.CLASS_NAME, 'inner-title').text
    #             price_new = product.find_element(
    #                 By.CLASS_NAME, 'inner-price-new').text
    #             price_old = product.find_element(
    #                 By.CLASS_NAME, 'inner-price-old').text
    #             discount = product.find_element(
    #                 By.CLASS_NAME, 'inner-discount').text
    #             print(
    #                 f"Title: {title}, New Price: {price_new}, Old Price: {price_old}, Discount: {discount}")

    #         message = self.driver.find_element(
    #             By.CSS_SELECTOR, 'body > div > div:nth-child(2) > div > div').text
    #         print(message)
    #         self.assertEqual(message, "Không tìm thấy sản phẩm nào.")

    # TC_43
    # def test43(self):
    #     # Đợi một chút để đảm bảo trang tải hoàn toàn
    #     time.sleep(3)
    #     with open("Data/searching_function.json", encoding="utf-8") as f:
    #         data = json.load(f)
    #         keyword = data["test_cases_searching"][7]["keyword"]
    #         self.driver.find_element(
    #             By.CSS_SELECTOR, "body > header > div > div > div.col-5 > form > div > input").send_keys(keyword)
    #         # Tìm nút tìm kiếm và click vào nó
    #         # Thay 'search-button-id' bằng ID thực của nút tìm kiếm
    #         search_button = self.driver.find_element(
    #             By.CSS_SELECTOR, 'body > header > div > div > div.col-5 > form > div > button')
    #         search_button.click()

    #         # Đợi một chút để đảm bảo kết quả tìm kiếm tải hoàn toàn
    #         time.sleep(3)

    #         # Tìm tất cả các sản phẩm
    #         product_items = self.driver.find_elements(
    #             By.CLASS_NAME, 'product-item')

    #         # In thông tin về từng sản phẩm
    #         for product in product_items:
    #             title = product.find_element(By.CLASS_NAME, 'inner-title').text
    #             price_new = product.find_element(
    #                 By.CLASS_NAME, 'inner-price-new').text
    #             price_old = product.find_element(
    #                 By.CLASS_NAME, 'inner-price-old').text
    #             discount = product.find_element(
    #                 By.CLASS_NAME, 'inner-discount').text
    #             print(
    #                 f"Title: {title}, New Price: {price_new}, Old Price: {price_old}, Discount: {discount}")

    #         message = self.driver.find_element(
    #             By.CSS_SELECTOR, 'body > div > div:nth-child(2) > div > div').text
    #         print(message)
    #         self.assertEqual(message, "Không tìm thấy sản phẩm nào.")


if __name__ == "__main__":
    unittest.main()
