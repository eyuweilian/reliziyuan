from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from .dingwei import Login,Add,Modify,Delate,Check
from selenium.webdriver.chrome.webdriver import WebDriver
class Basecase(object):
    def __init__(self,driver:WebDriver):
        self.driver=driver
class Login_demo(Basecase):
    def admin(self,key):
        WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element(*Login.txtUsername))
        admin=self.driver.find_element(*Login.txtUsername)
        admin.click()
        admin.clear()
        admin.send_keys(key)
    def password(self,keyword):
        WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element(*Login.txtPassword))
        password=self.driver.find_element(*Login.txtPassword)
        password.click()
        password.clear()
        password.send_keys(keyword)
    def enter(self):
        WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element(*Login.button))
        button=self.driver.find_element(*Login.button)
        button.click()
class Tiaozhuan(Basecase):
    def zhaopin(self):
        WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element(*Login.link))
        link=self.driver.find_element(*Login.link)
        link.click()
    def kongque(self):
        WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element(*Login.link1))
        link1=self.driver.find_element(*Login.link1)
        link1.click()
class ResultPage(Basecase):
    def result(self):
        WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element(*Login.yibiaopan))
        return self.driver.page_source
class Add_demo(Basecase):
    def add(self):
        WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element(*Add.btnAdd))
        add=self.driver.find_element(*Add.btnAdd)
        add.click()
    def addJobVacancy_jobTitle(self):
        WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element(*Add.addJobVacancy_jobTitle))
        addJobVacancy_jobTitle=self.driver.find_element(*Add.addJobVacancy_jobTitle)
        Select(addJobVacancy_jobTitle).select_by_visible_text('0000')
    def addJobVacancy_name(self,value):
        WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element(*Add.addJobVacancy_name))
        addJobVacancy_name=self.driver.find_element(*Add.addJobVacancy_name)
        addJobVacancy_name.click()
        addJobVacancy_name.clear()
        addJobVacancy_name.send_keys(value)
    def addJobVacancy_hiringManager(self,value1):
        WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element(*Add.addJobVacancy_hiringManager))
        addJobVacancy_hiringManager=self.driver.find_element(*Add.addJobVacancy_hiringManager)
        addJobVacancy_hiringManager.click()
        addJobVacancy_hiringManager.clear()
        addJobVacancy_hiringManager.send_keys(value1)
    def addJobVacancy_noOfPositions(self,value2):
        WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element(*Add.addJobVacancy_noOfPositions))
        addJobVacancy_noOfPositions=self.driver.find_element(*Add.addJobVacancy_noOfPositions)
        addJobVacancy_noOfPositions.click()
        addJobVacancy_noOfPositions.clear()
        addJobVacancy_noOfPositions.send_keys(value2)
    def addJobVacancy_description(self,value3):
        WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element(*Add.addJobVacancy_description))
        addJobVacancy_description=self.driver.find_element(*Add.addJobVacancy_description)
        addJobVacancy_description.click()
        addJobVacancy_description.clear()
        addJobVacancy_description.send_keys(value3)
    def savebutton(self):
        WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element(*Add.savebutton))
        savebutton=self.driver.find_element(*Add.savebutton)
        savebutton.click()
class Modify_demo(Basecase):
    def savebutton(self):
        WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element(*Modify.savebutton))
        savebutton=self.driver.find_element(*Modify.savebutton)
        savebutton.click()
    def addJobVacancy_name(self,value):
        WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element(*Modify.addJobVacancy_name))
        addJobVacancy_name=self.driver.find_element(*Modify.addJobVacancy_name)
        addJobVacancy_name.click()
        addJobVacancy_name.clear()
        addJobVacancy_name.send_keys(value)
    def savebutton_hover(self):
        WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element(*Modify.savebutton_hover))
        savebutton_hover=self.driver.find_element(*Modify.savebutton_hover)
        savebutton_hover.click()
    def cancel(self):
        WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element(*Modify.cancel))
        cancel=self.driver.find_element(*Modify.cancel)
        cancel.click()
class Delate_demo(Basecase):
    def ohrmList_chkSelectRecord_num(self):
        WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element(*Delate.ohrmList_chkSelectRecord_num))
        ohrmList_chkSelectRecord_num=self.driver.find_element(*Delate.ohrmList_chkSelectRecord_num)
        ohrmList_chkSelectRecord_num.click()
    def delete(self):
        WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element(*Delate.delete))
        delate=self.driver.find_element(*Delate.delete)
        delate.click()
    def dialogDeleteBtn(self):
        WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element(*Delate.dialogDeleteBtn))
        dialogDeleteBtn=self.driver.find_element(*Delate.dialogDeleteBtn)
        dialogDeleteBtn.click()
class Check_demo(Basecase):
    def vacancySearch_jobTitle(self):
        WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element(*Check.vacancySearch_jobTitle))
        addJobVacancy_jobTitle = self.driver.find_element(*Check.vacancySearch_jobTitle)
        Select(addJobVacancy_jobTitle).select_by_visible_text('000')
    def vacancySearch_jobVacancy(self):
        WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element(*Check.vacancySearch_jobVacancy))
        addJobVacancy_jobTitle = self.driver.find_element(*Check.vacancySearch_jobVacancy)
        Select(addJobVacancy_jobTitle).select_by_visible_text('333')
    def vacancySearch_hiringManager(self):
        WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element(*Check.vacancySearch_hiringManager))
        addJobVacancy_jobTitle = self.driver.find_element(*Check.vacancySearch_hiringManager)
        Select(addJobVacancy_jobTitle).select_by_visible_text('888 888 888')
    def vacancySearch_status(self):
        WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element(*Check.vacancySearch_status))
        addJobVacancy_jobTitle = self.driver.find_element(*Check.vacancySearch_status)
        Select(addJobVacancy_jobTitle).select_by_visible_text('所有')
    def btnSrch(self):
        WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element(*Check.btnSrch))
        addJobVacancy_jobTitle = self.driver.find_element(*Check.btnSrch)
        addJobVacancy_jobTitle.click()
    def btnRst(self):
        WebDriverWait(self.driver, 10, 1).until(lambda driver: driver.find_element(*Check.btnRst))
        addJobVacancy_jobTitle = self.driver.find_element(*Check.btnRst)
        addJobVacancy_jobTitle.click()

