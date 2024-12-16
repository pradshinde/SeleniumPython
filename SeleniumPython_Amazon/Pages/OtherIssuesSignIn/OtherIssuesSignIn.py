from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from SeleniumPython_Amazon.driver.webDriver import webDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from SeleniumPython_Amazon.Pages.basePage import basePage

class OtherIssuesSignIn(basePage):
    AccountLoginIssues_label_xpath="//*[@class='contact-us-header']/*[contains(text(),'Account & Login Issues')]"

    def __init__(self):
        self.bp=basePage()
#----------------------------Creation Block-----------------------------------

#--------------------------------------Functional Block-----------------------------



#---------------------Verification Block--------------------------------

    def verify_AccountLoginIssues(self):

        self.elementDisplayed(self.AccountLoginIssues_label_xpath, "xpath", "Account & Login Issues page has been successfully opened")



