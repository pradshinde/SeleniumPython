from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from SeleniumPython_Amazon.Pages.basePage import basePage

from SeleniumPython_Amazon.driver.webDriver import webDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

class HomePage(basePage):
    HelloUsername_xpath="//div[@class='nav-line-1-container']//*[@id='nav-link-accountList-nav-line-1']//*[not(contains(text(),'Hello, sign in')]"

    def __init__(self):
        self.bp=basePage()
#----------------------------Creation Block-----------------------------------

#--------------------------------------Functional Block-----------------------------



#---------------------Verification Block--------------------------------

    def verify_HelloUsername(self):

        self.elementDisplayed(self.HelloUsername_xpath, "xpath", "User successfully logged in")



