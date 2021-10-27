from selenium.webdriver.common.by import By


class Login():
    txtUsername=(By.ID,'txtUsername')
    txtPassword=(By.ID,'txtPassword')
    button=(By.CLASS_NAME,'button')
    yibiaopan=(By.XPATH,'//*[@id="content"]/div/div[1]/h1')
    link=(By.LINK_TEXT,'招聘')
    link1=(By.LINK_TEXT,'职位空缺')
class Add():
    btnAdd=(By.NAME,'btnAdd')
    addJobVacancy_jobTitle=(By.ID,'addJobVacancy_jobTitle')
    addJobVacancy_name=(By.ID,'addJobVacancy_name')
    addJobVacancy_hiringManager=(By.ID,'addJobVacancy_hiringManager')
    addJobVacancy_noOfPositions=(By.ID,'addJobVacancy_noOfPositions')
    addJobVacancy_description=(By.ID,'addJobVacancy_description')
    savebutton=(By.CLASS_NAME,'savebutton')
class Modify():
    savebutton=(By.CLASS_NAME,'savebutton')
    addJobVacancy_name=(By.ID,'addJobVacancy_name')
    savebutton_hover=(By.CLASS_NAME,'savebutton')
    cancel=(By.CLASS_NAME,'cancel')
class Delate():
    ohrmList_chkSelectRecord_num=(By.ID,'ohrmList_chkSelectRecord_89')
    delete=(By.CLASS_NAME,'delete')
    dialogDeleteBtn=(By.ID,'dialogDeleteBtn')
class Check():
    vacancySearch_jobTitle=(By.ID,'vacancySearch_jobTitle')
    vacancySearch_jobVacancy=(By.ID,'vacancySearch_jobVacancy')
    vacancySearch_hiringManager=(By.ID,'vacancySearch_hiringManager')
    vacancySearch_status=(By.ID,'vacancySearch_status')
    btnSrch=(By.ID,'btnSrch')
    btnRst=(By.ID,'btnRst')