from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from SeleniumPython_Amazon.driver.webDriver import webDriver
from selenium.webdriver.support.ui import Select
from SeleniumPython_Amazon.Pages.basePage import basePage


class AddtoCart(basePage):
    icon_xpath = "//div[@id='nav-logo']//*[@id='nav-logo-sprites']"
    UpdateLocation_Link_xpath="//div[@id='glow-ingress-block']"
    allCategory_dropdn_xpath = "//div[@class='nav-search-scope nav-sprite']//*[@id='searchDropdownBox']"
    searchText_xpath="//div[@class='ac-input-container']//*[@id='twotabsearchtextbox']"
    SearchSubmit_Btn_xpath="//div[@class='nav-search-submit nav-sprite']"
    ChangeLanguage_Dropdn_xpath = "//div[@id='nav-tools']//*[@id='icp-nav-flyout']"
    account_list_link_xpath = "//div[@id='nav-tools']//*[@id='nav-link-accountList']"
    NavOrderes_Btn_xpath = "//div[@id='nav-tools']//*[@id='nav-orders']"
    NavCart_Btn_xpath = "//div[@id='nav-tools']//*[@id='nav-cart']"
    OpenAllCategory_Btn_xpath = "//div[@class='nav-left']/*[@aria-label='Open All Categories Menu']"
    NavHoliday_Link_xpath = "//div[@id='nav-xshop']//*[contains(text(),'Black Friday Deals')]"
    MedicalCare_Link_xpath="//div[@id='nav-xshop']//*[@class='nav-a']"
    BestSelllers_Link_xpath ="//div[@id='nav-xshop']//*[contains(text(),'Best Sellers')]'"
    Prime_Link_xpath = "//div[@id='nav-xshop']/*[@id='nav-link-amazonprime']"
    ABasics_Link_xpath = "//div[@id='nav-xshop']/*[contains(text(),'Amazon Basics')]"
    Groceries_Link_xpath = "//*[@id='nav-xshop']/*[@id='nav-link-groceries']"
    NewReleases_Link_xpath = "//*[@id='nav-xshop']/*[@data-csa-c-slot-id='nav_cs_7'] "
    Music_Link_xpath= "//*[@id='nav-xshop']/*[@data-csa-c-slot-id='nav_cs_8']"
    ShopBlackFriday_Link_xpath = "//*[@id='nav-swmslot']/*[@id='swm-link']"
    CartEmpty_label_xpath="//*[@class='a-column a-span8 a-span-last']/*[contains(text(),'Your Amazon Cart is empty')]"
    TodaysDeals_Link_xpath = "//*[@class='a-section a-spacing-none sc-shop-todays-deals-link']"
    SignInAcnt_Btn_xpath = "//*[@class='a-button a-button-primary']"
    SignUp_Btn_xpath = "//*[@id='a-autoid-1']"
    RecentlyViewed_label_xpath="//*[@class='a-carousel-heading a-inline-block']"
    PersonalizedRecommandation_label_xpath="//*[@class='rhf-sign-in-title']"
    SignIn_Btn_xpath="//*[@class='action-button']"
    NewCustomer_label_xpath="//*[@class='rhf-sign-in-tooltip-new-customer']"
    Starthere_Link_xpath="//*[@class='sign-in-tooltip-link']"
    BacktoTop_label_xpath="//*[@class='navFooterBackToTopText']"
    navFooterColsGettoknow_label_xpath="//*[contains(text(),'Get to Know Us')]"
    Footer_Links_Careers_xpath="//*[@class='nav_a' and contains(text(),'Careers')]"
    bottomlogo_xpath="//*[@class='nav-logo-base nav-sprite']"
    ChangeLanguageBtm_Dropdn_xpath="//*[@id='icp-touch-link-language']"
    LinkCountry_Link_xpath="//*[@id='icp-touch-link-country']"
    DescText_AmazonRenewed_Link_xpath="//*[@class='nav_a' and contains(text(),'Amazon Renewed')]"
    bottomNavIcon_xpath="//*[@id='nav-icon-ccba']"






    def __init__(self):
        self.bp = basePage()



    def verify_icon(self):

        self.elementDisplayed(self.icon_xpath, "xpath", "Icon is displayed")


    def click_UpdateLocation_Link(self):

        self.click(locator=self.UpdateLocation_Link_xpath,LocatorType="xpath")

    def select_BooksCategory(self):

        self.DropdnSelectByValue(self.allCategory_dropdn_xpath, "xpath", "search-alias=stripbooks")


    def select_BabyCategory(self):

        self.DropdnSelectByText(self.allCategory_dropdn_xpath, "xpath", "Baby")


    def select_AlexaSkilsCategory(self):

        self.DropdnSelectByIndex(self.allCategory_dropdn_xpath, "xpath", 2)


    def enter_searchText(self,searchText):

        self.bp.sedKeys(self.searchText_xpath,"xpath",searchText)

    def click_SearchSubmit_Btn(self):

        self.click(locator=self.SearchSubmit_Btn_xpath,LocatorType="xpath")


    def hover_ChangeLanguage_Dropdn(self):

        self.hoverElement(self.ChangeLanguage_Dropdn_xpath, "xpath")


    def hoverAccount_list_Dropdn(self):

        self.hoverElement(self.account_list_link_xpath, "xpath")

    def click_NavOrderes_Btn(self):

        self.click(locator=self.NavOrderes_Btn_xpath,LocatorType="xpath")

    def click_NavCart_Btn(self):

        self.click(locator=self.NavCart_Btn_xpath,LocatorType="xpath")

    def click_OpenAllCategory_Btn(self):

        self.click(locator=self.OpenAllCategory_Btn_xpath,LocatorType="xpath")

    def click_NavHoliday_Link(self):

        self.click(locator=self.NavHoliday_Link_xpath,LocatorType="xpath")

    def hover_MedicalCare_Link(self):

        self.hoverElement(self.MedicalCare_Link_xpath, "xpath")

    def click_BestSelllers_Link(self):

        self.click(locator=self.BestSelllers_Link_xpath,LocatorType="xpath")

    def hover_Prime_Link(self):

        self.hoverElement(self.Prime_Link_xpath, "xpath")

    def click_ABasics_Link(self):

        self.click(locator=self.ABasics_Link_xpath,LocatorType="xpath")

    def hover_Groceries_Link(self):

        self.hoverElement(self.Groceries_Link_xpath, "xpath")

    def click_NewReleases_Link(self):

        self.click(locator=self.NewReleases_Link_xpath,LocatorType="xpath")

    def click_Music_Link(self):

        self.click(locator=self.Music_Link_xpath, LocatorType="xpath")

    def click_ShopBlackFriday_Link(self):

        self.click(locator=self.ShopBlackFriday_Link_xpath, LocatorType="xpath")

    def verify_CartEmpty_label(self):

        self.elementDisplayed(self.CartEmpty_label_xpath, "xpath", "Your Amazon Cart is empty label is displayed")


    def click_TodaysDeals_Link(self):

        self.click(locator=self.TodaysDeals_Link_xpath, LocatorType="xpath")

    def click_SignInAcnt_Btn(self):

        self.click(locator=self.SignInAcnt_Btn_xpath, LocatorType="xpath")

    def click_SignUp_Btn(self):

        self.click(locator=self.SignUp_Btn_xpath, LocatorType="xpath")

    def verify_RecentlyViewed_label(self):

        self.elementDisplayed(self.RecentlyViewed_label_xpath, "xpath", "Recently viewed label is displayed")


    def verify_PersonalizedRecommandation_label(self):

        self.elementDisplayed(self.PersonalizedRecommandation_label_xpath, "xpath", "See personalized recommendations label is displayed")


    def click_SignIn_Btn(self):

        self.click(locator=self.SignIn_Btn_xpath, LocatorType="xpath")

    def verify_NewCustomer_label(self):

        self.elementDisplayed(self.NewCustomer_label_xpath, "xpath", "New customer? label is displayed")


    def click_Starthere_Link(self):

        self.click(locator=self.Starthere_Link_xpath, LocatorType="xpath")

    def click_BacktoTop_label(self):

        self.click(locator=self.BacktoTop_label_xpath, LocatorType="xpath")

    def verify_navFooterCols_Gettoknow_label(self):

        self.elementDisplayed(self.navFooterColsGettoknow_label_xpath, "xpath", "Get to Know Us label is displayed")


    def click_Footer_Careers_Link(self):

        self.click(locator=self.Footer_Links_Careers_xpath, LocatorType="xpath")

    def verify_bottomlogo(self):

        self.elementDisplayed(self.bottomlogo_xpath, "xpath", "Amazon logo at bottom is displayed")


    def hover_ChangeLanguageBtm_Dropdn(self):

        self.hoverElement(self.ChangeLanguageBtm_Dropdn_xpath, "xpath")

    def click_LinkCountry_Link(self):

        self.click(locator=self.LinkCountry_Link_xpath, LocatorType="xpath")

    def click_DescText_AmazonRenewed_Links(self):

        self.click(locator=self.DescText_AmazonRenewed_Link_xpath, LocatorType="xpath")

    def verify_bottomNavIcon(self):

        self.elementDisplayed(self.bottomNavIcon_xpath, "xpath", "Navigation icon at bottom  is displayed")





