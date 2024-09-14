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
from email.header import decode_header
import ezgmail


# ezgmail.init()
# ezgmail.send("2151010246nghiem@ou.edu.vn",
#              "Email để test", "Đấy là email để test app")
unreadThreads = ezgmail.unread()
# ttr = ezgmail.summary(unreadThreads)
a = str(unreadThreads[0])
otpmatch = regex.search(r'\b\d{8}\b', a)
otp = otpmatch.group(0)
print(a)
print(otp)
