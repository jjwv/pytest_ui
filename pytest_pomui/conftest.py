import pytest
from selenium import webdriver
from pytest_pomui.pages.login_page import LoginPage
import time
from selenium.webdriver.chrome.options import Options



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
        chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在报错问题
        chrome_options.add_argument('--disable-gpu')  # 禁用GPU硬件加速。如果软件渲染器没有就位，则GPU进程将不会启动。
        chrome_options.add_argument('--disable-dev-shm-usage')


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

















