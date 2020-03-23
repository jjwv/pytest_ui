from pytest_pomui.common.base import Base
from pytest_pomui.common.config import host
import allure


login_url = host + "/xadmin/"

class LoginPage(Base):

    loc_用户名 = ("id", "id_username")
    loc_密码 = ("id", "id_password")
    loc_登录按钮 = ("xpath", "//*[text()='登录']")
    loc_登录 = ("css", "#panel-login>div.panel-body>button")

    # 判断登录成功
    loc_panduan = ("css", "#top-nav>div.navbar-header>a")
    loc_后台页面 = ("xpath", "//*[text()='Django Xadmin']")

    @allure.step("步骤：登录web页面")
    def login(self, username="admin", password="yoyo123456"):
        '''登录'''
        self.driver.get(login_url)
        self.send(self.loc_用户名, username)
        self.send(self.loc_密码, password)
        self.click(self.loc_登录按钮)

    @allure.step("步骤：登录后判断")
    def is_login_success(self):
        '''判断是否登录成功 True  False'''
        result = self.get_text(self.loc_panduan)
        print("登录完成后，获取页面文本元素: %s" %result)
        return result == "后台页面"

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window() # 最大化
    web = LoginPage(driver)
    web.login()
    res = web.is_login_success()
    assert res
    print("登录结果：%s"%res)
    import time
    time.sleep(5)
    driver.quit()