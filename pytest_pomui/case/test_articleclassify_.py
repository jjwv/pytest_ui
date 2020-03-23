from selenium import webdriver
from pytest_pomui.pages.login_page import LoginPage
from pytest_pomui.pages.articleclassify_page import ArticleclassifyPage
import allure,pytest,os
from pytest_pomui.common.read_yaml import readyml
import sys, os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))

testdata = [
    ('测试', True),
    ('aaaa', True),
    ('1111', True)
]

ymlpath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "articleclassify.yml")
print(ymlpath)
testdata = readyml(ymlpath).get("article_testdata")
print(testdata)



@allure.feature("文章分类页面")
class TestArticleclassify():
    ''''文章分类页面'''

    @allure.story("编辑文章分类，输入中文，编辑成功")
    @pytest.mark.parametrize("test_inout,expect",testdata)
    def test_edit_classify(self, login,test_inout,expect):
        '''前置条件:1.先登陆
                step1: 点文章分类导航标签
                step2: 编辑页面输入，分类名称，如:文学
                step3: 点保存按钮 ->保存成功
        '''
        driver = login
        #实例化edit页面
        edit = ArticleclassifyPage(driver)
        #点击左侧导航栏
        edit.click_classify_nav()
        #添加分类  标题 内容
        edit.edit_classify(text=test_inout,body='hahah')
        #判断结果
        res2 = edit.is_edit_classify_success(test_inout)
        print("编辑是否成功：%s" % res2)
        #断言
        assert res2 == expect  # 断言

    @allure.story("编辑文章分类-输入重复的分类，保存失败，不能添加重复的")
    @allure.issue("http://49.235.92.12:8080/zentao/bug-view-1.html")
    @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-5-1.html")
    def test_edit_classify1(self, login):
        '''重复编辑文章分类
        step1: 编辑“计算机”
        step2: 保存
        step3: 再次编辑“计算机”
        step4: 保存--》保存失败
        '''
        driver = login
        # 实例化edit页面
        edit = ArticleclassifyPage(driver)
        # 点左侧导航栏
        edit.click_classify_nav()
        # 编辑
        edit.edit_classify(text="计算机", body='hahah')
        # 判断结果
        res1 = edit.is_edit_classify_success("ll")
        print("编辑是否成功：%s" % res1)
        # 断言
        assert res1  # 断言

