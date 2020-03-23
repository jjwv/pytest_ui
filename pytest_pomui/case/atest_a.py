from selenium import webdriver
from pytest_pomui.pages.login_page import LoginPage
from pytest_pomui.pages.articleclassify_page import ArticleclassifyPage

class TestArticleclassify():

    def test_edit_classify(self, login):
        driver = login
        edit = ArticleclassifyPage(driver)
        edit.click_classify_nav()
        edit.edit_classify("测试yyy")
        res2 = edit.is_edit_classify_success("测试yyy")
        print("编辑是否成功：%s" % res2)
        assert res2  # 断言

    def test_edit_classify1(self, login):
        driver = login
        edit = ArticleclassifyPage(driver)
        edit.click_classify_nav()
        edit.edit_classify("测试yyy")
        res2 = edit.is_edit_classify_success("测试yyy")
        print("编辑是否成功：%s"%res2)
        assert res2  # 断言
