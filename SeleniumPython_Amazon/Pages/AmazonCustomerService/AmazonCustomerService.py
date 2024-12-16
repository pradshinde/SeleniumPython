from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from SeleniumPython_Amazon.driver.webDriver import webDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from SeleniumPython_Amazon.Pages.basePage import basePage

class AmazonCustomerService(basePage):
    AmazonCustomerService_label_xpath="//*[@class='page-container']/*[contains(text(),'Welcome to Amazon Customer Service')]"

    def __init__(self):
        self.bp=basePage()
#----------------------------Creation Block-----------------------------------

#--------------------------------------Functional Block-----------------------------



#---------------------Verification Block--------------------------------

    def verify_AmazonCustomerService(self):

        self.elementDisplayed(self.AmazonCustomerService_label_xpath, "xpath", "mazon Customer Service page has been successfully opened")



