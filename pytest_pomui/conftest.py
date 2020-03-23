import pytest
from selenium import webdriver
from pytest_pomui.pages.login_page import LoginPage
import time
from selenium.webdriver.chrome.options import Options

import sys, os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))

# 命令行参数
def pytest_addoption(parser):
    '''添加命令行参数'''
    parser.addoption(
        "--headless" , action="store",
        default="no", help="set chrome headless option yes or no"
    )

# request 内置的fixture
@pytest.fixture(scope="session")
def driver(request):
    '''只打开浏览器和关闭浏览器'''

   #无头浏览器
    headless = request.config.getoption("--headless")
    chrome_options = Options()
    chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度
    if headless =="yes":
        chrome_options.add_argument('--headless')  # 无界面

    driver = webdriver.Chrome(chrome_options=chrome_options)

    # driver = webdriver.Chrome()
    # driver.maximize_window() # 最大化

    def end():
        print("全部用例执行完后 teardown quit dirver")
        time.sleep(5)
        driver.quit()

    request.addfinalizer(end)
    return driver

@pytest.fixture(scope="session")
def login(driver):
    web = LoginPage(driver)
    web.login()
    return driver

















