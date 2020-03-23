from pytest_pomui.common.base import Base
import allure


class ArticleclassifyPage(Base):

    # loc_文章分类 = ("xpath", '//*[@href="/xadmin/hello/articleclassify/"]') # 2个
    loc_文章分类= ("xpath",'//*[@id = "left-side"]/ul[1]/li[11]/a')
    loc_ziji_文章 = ("xpath", "//*[@href='/xadmin/yoyo/article/']")

    loc_增加_文章分类 = ('xpath', '//*[@id="content-block"]/div[1]/div[2]/div/a')

    loc_输入标题 = ("id", "id_n")
    loc_输入内容 = ("id", "id_body")

    loc_保存 = ("xpath", "//*[text()=' 保存']")
    loc_table = ("xpath", "//table")

    @allure.step("点文章分类导航标签")
    def click_classify_nav(self):
        '''点文章分类导航标签'''
        self.click(self.loc_文章分类)

    @allure.step("编辑文章分类页面，编辑内容后保存")
    def edit_classify(self, text="测试123",body ="哈哈哈"):
        '''编辑文章分类'''
        # self.click(self.loc_ziji_文章)
        self.click(self.loc_增加_文章分类)
        self.send(self.loc_输入标题, text)
        # self.send(self.loc_输入内容,body)
        # 复数定位点击元素
        self.finds(self.loc_保存)[1].click()

    @allure.step("判断编辑是否成功")
    def is_edit_classify_success(self, text="测试"):
        '''判断编辑是否成功， 返回True 和 False'''
        # 判断  text 在table列表里面
        table = self.get_text(self.loc_table)
        return text in table

if __name__ == '__main__':
    from selenium import webdriver
    from pytest_pom.pages.login_page import LoginPage
    driver = webdriver.Chrome()
    driver.maximize_window() # 最大化
    web = LoginPage(driver)
    web.login()
    res = web.is_login_success()
    print("登录结果：%s"%res)

    # 编辑
    edit = ArticleclassifyPage(driver)
    edit.click_classify_nav()
    edit.edit_classify(text="测试123",body='hahaha')
    res2 = edit.is_edit_classify_success("测试123")
    print("编辑是否成功：%s"%res2)

    # import time
    # time.sleep(3)
    driver.close()


