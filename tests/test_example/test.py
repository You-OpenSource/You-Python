from youdotcom.code import Code
from youdotcom.init import Init

driver = Init(webdriver_path="/usr/bin/chromedriver").driver

code = Code.find_code(driver, search="python loop")

print(code)  # idk
