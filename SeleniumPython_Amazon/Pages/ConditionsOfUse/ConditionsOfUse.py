from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from SeleniumPython_Amazon.driver.webDriver import webDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from SeleniumPython_Amazon.Pages.basePage import basePage

class ConditionsOfUse(basePage):
    ConditionsOfUse_label_xpath="//div[@class='help-content']//*[contains(text(),'Conditions of Use')]"

    def __init__(self):
        self.bp=basePage()
#----------------------------Creation Block-----------------------------------

#--------------------------------------Functional Block-----------------------------



#---------------------Verification Block--------------------------------

    def verify_ConditionsOfUse(self):

        self.elementDisplayed(self.ConditionsOfUse_label_xpath, "xpath", "Conditions of Use page has been successfully opened")



