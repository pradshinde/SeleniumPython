from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from SeleniumPython_Amazon.Pages.basePage import basePage

from SeleniumPython_Amazon.driver.webDriver import webDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

class PasswordAssistance(basePage):
    PasswordAssistance_label_xpath="//*[@class='a-box-inner a-padding-extra-large']//*[contains(text(),'Password assistance')]"

    def __init__(self):
        self.bp=basePage()
#----------------------------Creation Block-----------------------------------

#--------------------------------------Functional Block-----------------------------



#---------------------Verification Block--------------------------------

    def verify_PasswordAssistance(self):

        self.elementDisplayed(self.PasswordAssistance_label_xpath, "xpath", "Password Assistance page has been successfully opened")



