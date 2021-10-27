import allure
import time
import yaml
from selenium import webdriver
import pytest
from 人力资源.pages.opetion import Login_demo,ResultPage,Tiaozhuan,Add_demo,Modify_demo,Delate_demo,Check_demo
from selenium.webdriver.support.select import Select
@allure.title('人力资源管理系统的增删改查')
@allure.feature('增删改查')
class Testrenli(object):
    @pytest.fixture(scope='module', autouse=True)
    def driver_init(self):
        allure.step('打开浏览器')
        self.driver = webdriver.Chrome(r'C:\Users\mengchao\PycharmProjects\exam_ui_auto\driver\chromedriver.exe')
        self.driver.implicitly_wait(10)
        allure.step('进入人力资源管理系统')
        self.driver.get('http://121.37.175.123:8080')
        yield self.driver
        self.driver.quit()

    @pytest.mark.parametrize('key',['admin'])
    @pytest.mark.parametrize('keyword',['Bitnami.12345'])
    @allure.story('登录步骤')
    def test_login(self,driver_init,key,keyword):
        allure.step('初始化参数')
        login_demo=Login_demo(driver_init)
        resultPage=ResultPage(driver_init)
        tiaozhuan=Tiaozhuan(driver_init)
        allure.step('1.添写账号')
        login_demo.admin(key)
        allure.step('2.填写密码')
        login_demo.password(keyword)
        login_demo.enter()
        allure.step('3.断言')
        assert '仪表盘' in resultPage.result()
        tiaozhuan.zhaopin()
        tiaozhuan.kongque()
    @allure.description('选择职称与职位数与描述和招聘经理')
    @pytest.mark.parametrize('key1', ['开发工程师'])
    @pytest.mark.parametrize('key2', ['888 888 888'])
    @pytest.mark.parametrize('key3', ['20'])
    @pytest.mark.parametrize('key4', ['职位不错'])
    @allure.story('添加职位空缺')
    def test_add(self,driver_init,key1,key2,key3,key4):
        allure.step('初始化参数')
        add_demo = Add_demo(driver_init)
        allure.step('添加东西')
        add_demo.add()
        add_demo.addJobVacancy_jobTitle()
        add_demo.addJobVacancy_name(key1)
        add_demo.addJobVacancy_hiringManager(key2)
        add_demo.addJobVacancy_noOfPositions(key3)
        add_demo.addJobVacancy_description(key4)
        allure.step('保存')
        add_demo.savebutton()

    @allure.description('更换职位名称名字')
    @pytest.mark.parametrize('key', ['开发工程师1'])
    @allure.story('修改职称')
    def test_modify(self,driver_init,key):
        allure.step('初始化参数')
        modify_demo=Modify_demo(driver_init)
        allure.step('修改数据')
        modify_demo.savebutton()
        modify_demo.addJobVacancy_name(key)
        modify_demo.savebutton_hover()
        modify_demo.cancel()
    @allure.story('删除职称')
    def test_delate(self,driver_init):
        allure.step('初始化参数')
        delate_demo=Delate_demo(driver_init)
        allure.step('删除数据')
        delate_demo.ohrmList_chkSelectRecord_num()
        delate_demo.delete()
        delate_demo.dialogDeleteBtn()
    @allure.story('搜索职称')

    def test_check(self,driver_init):
        allure.step('初始化参数')
        check_demo=Check_demo(driver_init)
        allure.step('查找数据')
        check_demo.vacancySearch_jobTitle()
        check_demo.vacancySearch_jobVacancy()
        check_demo.vacancySearch_hiringManager()
        check_demo.vacancySearch_status()
        check_demo.btnSrch()
        check_demo.btnRst()


if __name__ == '__main__':
    pytest.main()