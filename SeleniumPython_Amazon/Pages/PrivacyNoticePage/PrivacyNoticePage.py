from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from SeleniumPython_Amazon.Pages.basePage import basePage
from SeleniumPython_Amazon.driver.webDriver import webDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

class PrivacyNoticePage(basePage):
    PrivacyNotice_link_xpath="//*[@class='help-service-content']//*[contains(text(),'Amazon.com Privacy Notice')]"

    def __init__(self):
       self.bp=basePage()
#----------------------------Creation Block-----------------------------------

#--------------------------------------Functional Block-----------------------------



#---------------------Verification Block--------------------------------

    def verify_PrivacyNotice(self):

        self.elementDisplayed(self.PrivacyNotice_link_xpath, "xpath", "Privacy Notice page has been successfully opened")



