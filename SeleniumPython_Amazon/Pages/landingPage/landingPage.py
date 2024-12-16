from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from SeleniumPython_Amazon.driver.webDriver import webDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from SeleniumPython_Amazon.Pages.basePage import basePage
#from SeleniumPython_Amazon.Pages.Login.LoginPage import LoginPage


class landingPage(basePage):

    account_list_link_id = "nav-link-accountList"
    allCategory_dropdn_xpath="//*[@id='searchDropdownBox']"
    SignInAcnt_Btn_xpath="//*[@id='nav-flyout-ya-signin']//*[contains(text(),'Sign in')]"
    amazonLogo_Img_xpath="//*[@id='nav-logo']"
    StartHere_Link_xpath = "//*[@id='nav-flyout-ya-newCust']//*[contains(text(),'Start here.')]"
    searchText_xpath="//div[@class='ac-input-overlay']//*[@id='twotabsearchtextbox']"
    Search_xpath="//div[@class='nav-search-submit nav-sprite']"
    Results_xpath="//*[@class='s-no-outline']//*[contain(text(),'Results')]"
    Products_List_xpath="//*[@data-cy='title-recipe']//*[@class='a-size-medium a-color-base a-text-normal']"
    email_textbox_xpath = "//*[@name='email']"


    # def __init__(self):

#----------------------------Creation Block-----------------------------------
    def hoverAccount_list(self):

        self.hoverElement(self.account_list_link_id,"id")

    def click_SignInAcnt_Btn(self):

        self.click(self.SignInAcnt_Btn_xpath,"xpath")

    def click_StartHere_Link(self):

        self.click(self.StartHere_Link_xpath,"xpath")

    def select_BooksCategory(self):

        self.DropdnSelectByValue(self.allCategory_dropdn_xpath, "xpath", "search-alias=stripbooks")


    def enter_SearchText(self,SearchText):

        self.sedKeys(self.searchText_xpath, "xpath", SearchText)

    def click_Search(self):

        self.click(self.Search_xpath,"xpath")

    def enter_emailID(self,email_mobilenumber):
        self.sedKeys(self.email_textbox_xpath,"xpath",email_mobilenumber)
#--------------------------------------Functional Block-----------------------------
    def SearchProduct(self,searchtext):
        self.enter_SearchText(searchtext)
        self.click_Search()
        element1 = self.driver.find_elements(By.XPATH(self.Products_List_xpath))
        if self.elementDisplayed(self.Results_xpath, "xpath","") and len(element1) > 0:
            print("Search is successful")


#---------------------Verification Block--------------------------------

    def verify_amazonLogo(self):

        self.elementDisplayed(self.amazonLogo_Img_xpath, "xpath", "URL has been opened")



