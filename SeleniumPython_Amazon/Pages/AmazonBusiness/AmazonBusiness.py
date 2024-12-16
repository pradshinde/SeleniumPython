from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from SeleniumPython_Amazon.Pages.basePage import basePage

from SeleniumPython_Amazon.driver.webDriver import webDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

class AmazonBusiness(basePage):
    AmazonBusiness_logo_xpath="//*[@class='a-link-nav-icon']"

    def __init__(self):
        self.bp=basePage()
#----------------------------Creation Block-----------------------------------

#--------------------------------------Functional Block-----------------------------



#---------------------Verification Block--------------------------------

    def verify_AmazonBusiness(self):

        self.elementDisplayed(self.AmazonBusiness_logo_xpath, "xpath", "Amazon Business page has been successfully opened")



