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
import threading  # Kiểm thử luồng


# Hàm đăng nhập
def login(driver, email, password):
    # Thay thế bằng URL của hệ thống
    driver.get("https://storecs.vercel.app/admin/auth/login/")
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(
        By.CSS_SELECTOR, "body > div > div > div > form > div:nth-child(3) > button").click()

# Hàm xóa danh mục sản phẩm


def delete_category(driver):
    # Điều hướng tới trang quản lý danh mục sản phẩm
    driver.find_element(
        By.CSS_SELECTOR, "body > div > div.sider > div > ul > li:nth-child(2) > a").click()
    time.sleep(5)
    driver.find_element(
        By.XPATH, '/html/body/div/div[2]/div/table/tbody/tr[3]/td[6]/button').click()
    # Chọn OK - xác nhận xóa
    # Wait for the alert to be displayed and switch to it
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    time.sleep(5)
    # Click "OK" on the alert
    alert.accept()
    time.sleep(5)


def edit_category(driver):
    # Điều hướng tới trang quản lý danh mục sản phẩm
    driver.find_element(
        By.CSS_SELECTOR, "body > div > div.sider > div > ul > li:nth-child(2) > a").click()
    time.sleep(5)
    # Chọn vào sửa
    driver.find_element(
        By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[3]/td[6]/a").click()
    time.sleep(3)

    # Sửa tiêu đề
    driver.find_element(
        By.ID, "title").clear()  # Xóa tiêu đề cũ
    driver.find_element(
        By.ID, "title").send_keys("Test_Case 94 Fix")
    # Sửa vị trí
    driver.find_element(
        By.CSS_SELECTOR, "#position").clear()  # Xóa vị trí cũ
    driver.find_element(
        By.CSS_SELECTOR, "#position").send_keys("4")
    # Điền mô tả vào thẻ iframe (Sửa nội dung)
    driver.switch_to.frame("desc_ifr")
    body = driver.find_element(By.ID, "tinymce")
    body.clear()  # Clear any existing content
    body.send_keys("Đây là nội dung sửa")
    driver.switch_to.default_content()
    time.sleep(3)

    # Upload ảnh mới
    file_input = driver.find_element(By.ID, 'thumbnail')
    file_path = "D:/Project-managerTest/tests/automation-test/image_for_testing/cat.jpg"
    file_input.send_keys(file_path)
    time.sleep(3)

    # Sửa trạng thái
    driver.find_element(
        By.XPATH, '//*[@id="statusInActive"]').click()

    # Chọn button cập nhật
    driver.find_element(
        By.XPATH, '/html/body/div[1]/div[2]/form/div[8]/button').click()
    time.sleep(5)

    # Vào lại danh mục sản phẩm chọn xem đã sửa chưa
    driver.find_element(
        By.XPATH, '/html/body/div[1]/div[1]/div/ul/li[2]/a').click()
    time.sleep(4)


# Khởi tạo trình duyệt cho Admin 1
driver1 = webdriver.Chrome()
# Khởi tạo trình duyệt cho Admin 2
driver2 = webdriver.Chrome()

# Hàm kiểm thử cho Admin 1


def admin1_actions():
    try:
        login(driver1, "nghiemnguyen111121@gmail.com", "nghiem123")
        delete_category(driver1)
    finally:
        driver1.quit()

# Hàm kiểm thử cho Admin 2


def admin2_actions():
    try:
        login(driver2, "nghiemnguyen111131@gmail.com", "11112001Nghiem")
        # Chờ một khoảng thời gian để đảm bảo Admin 1 đã xóa xong
        time.sleep(5)
        delete_category(driver2)
    except Exception as e:
        print("Admin 2 không thể sửa vì danh mục đã bị xóa bởi Admin 1")
    finally:
        driver2.quit()


# Sử dụng threading để thực hiện các hành động đồng thời
thread1 = threading.Thread(target=admin1_actions)
thread2 = threading.Thread(target=admin2_actions)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
