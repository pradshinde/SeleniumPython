import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import element_located_selection_state_to_be

from SeleniumPython_Amazon.driver.webDriver import webDriver
from SeleniumPython_Amazon.Pages.landingPage.landingPage import landingPage
from SeleniumPython_Amazon.Pages.CreateAccount.CreateAccount import CreateAccount
from SeleniumPython_Amazon.Pages.HomePage.HomePage import HomePage
from SeleniumPython_Amazon.Pages.ConditionsOfUse.ConditionsOfUse import ConditionsOfUse
from SeleniumPython_Amazon.Pages.PrivacyNoticePage.PrivacyNoticePage import PrivacyNoticePage
from SeleniumPython_Amazon.Pages.Password_assistance.Password_assistance import PasswordAssistance
from SeleniumPython_Amazon.Pages.OtherIssuesSignIn.OtherIssuesSignIn import OtherIssuesSignIn
from SeleniumPython_Amazon.Pages.AmazonBusiness.AmazonBusiness import AmazonBusiness
from SeleniumPython_Amazon.Pages.AmazonCustomerService.AmazonCustomerService import AmazonCustomerService
from SeleniumPython_Amazon.Pages.basePage import basePage

#********************************LOCATORS*************************************************
#ID, Class, Name, XPATH, Tagname, Css selector
#XPATH: absolute(/)--> Immediate next, relative(//)--> not sure property
#xpath axes: contains, parent,following-sibling,ancestor,starts-with
#parent: //*[@id='ap_email']//parent::div//parent::div//*[contains(text(),'Sign in')]
#following-sibling : //*[@id='ap_email']//parent::div//parent::div//following-sibling::div[@id='auth-email-missing-alert']
#ancestor: //*[@id='ap_email']//ancestor::div
# starts-with: //*[starts-with(@name,'em')] for email

class LoginPage(landingPage):
    email_textbox_xpath ="//*[@name='email']"
    continue_button_xpath ="//input[@id='continue']"
    password_textbox_xpath = "//input[@type='password']"
    signin_button_xpath  = "//input[@aria-labelledby='auth-signin-button-announce']"


    Needhelp_link_xpath  ="//span[@class='a-expander-prompt']"
    Buying_forWork_label_xpath ="//span[@class='a-text-bold']"
    create_NewAccount_btn_xpath ="//*[@id='createAccountSubmit']"
    last_footer_line_label_xpath ="//div[@class='a-section a-spacing-none a-text-center']/*[@class='a-size-mini a-color-secondary']"
    icon_xpath ="//div[@class='a-section a-spacing-medium a-text-center']//*[@class='a-icon a-icon-logo']"
    signIn_label_xpath ="//*[@class='a-box-inner a-padding-extra-large']//*[@class='a-spacing-small']"
    emailMobileNumber_label_xpath ="//*[contains(text(),'Email or mobile phone number')]"
    Help_footerlabel_xpath ="//*[@class='a-section a-spacing-small a-text-center a-size-mini']//*[contains(text(),'Help')]"
    textrow_label_xpath ="//div[@id='legalTextRow']"
    auth_emailID_label_xpath ="//div[@class='a-row a-spacing-base']//*[@id='auth-email-claim']"
    change_link_xpath ="//div[@class='a-row a-spacing-base']//*[@id='ap_change_login_claim']"
    Password_label_xpath ="//div[@class='a-column a-span5']//*[contains(text(),'Password')]"
    ForgotPassword_link_xpath ="//div[@class='a-column a-span7 a-text-right a-span-last']//*[contains(text(),'Forgot password?')]"
    ConditionsOfuse_link_xpath="//*[@id='legalTextRow']//*[contains(text(),'Conditions of Use')]"
    PrivacyNotice_link_xpath = "//*[@id='legalTextRow']//*[contains(text(),'Privacy Notice')]"
    ForgotYrPassword_xpath="//*[@aria-expanded='true']//*[contains(text(),'Forgot your password?')]"
    OtherIssues_xpath = "//*[@aria-expanded='true']//*[contains(text(),'Other issues with Sign-In')]"
    ShopAmazonBusiness_link_xpath="//*[@id='ab-signin-link-section']//*[contains(text(),'Shop on Amazon Business')]"
    Help_link_xpath = "//*[@class='a-section a-spacing-small a-text-center a-size-mini']//*[contains(text(),'Help')]"
    EnterYrPassword_alert_xpath="//div[@class='a-box-inner a-alert-container']//*[contains(text(),'Enter your password')]"
    EnterYrEmail_alert_xpath = "//*[@class='a-box-inner a-alert-container']/*[contains(text(),'Enter your email or mobile phone number')]"
    ValidEmail_alert_xpath = "//*[@class='a-box-inner a-alert-container']/*[contains(text(),'Enter a valid email address or phone number')]"
    InvalidAcnt_xpath = "//*[@class='a-box-inner a-alert-container']"
    EmailPA_xpath="//div[@class='a-section a-spacing-large']//*[@id='ap_email']"



    def __init__(self):
        self.bp=basePage()
        self.lp=landingPage()
        self.ca=CreateAccount()
        self.hp=HomePage()
        self.cond=ConditionsOfUse()
        self.pn=PrivacyNoticePage()
        self.PA=PasswordAssistance()
        self.OI=OtherIssuesSignIn()
        self.AB=AmazonBusiness()
        self.acs=AmazonCustomerService

    def enter_emailID(self,email_mobilenumber):
        self.bp.sedKeys(self.email_textbox_xpath,"xpath",email_mobilenumber)

    def click_Continuebtn(self):
        self.click(locator=self.continue_button_xpath,LocatorType="xpath")

    def enter_password(self,password):
        self.sedKeys(self.password_textbox_xpath,"xpath",password)

    def click_signinbtn(self):
       self.click(self.signin_button_xpath,"xpath")

    def click_Needhelf_Link(self):

        self.click(self.Needhelp_link_xpath,"xpath")

    def verify_Buying_for_work(self):
        self.elementDisplayed(self.Buying_forWork_label_xpath,"xpath","Buying for work? is displayed")


    def click_createNew_account(self):

        self.click(self.create_NewAccount_btn_xpath,"xpath")

    def verify_last_footer_line(self):

        self.elementDisplayed(self.last_footer_line_label_xpath,"xpath","The last footer line is displayed")


    def verify_icon(self):

        self.elementDisplayed(self.icon_xpath, "xpath", "Icon is displayed")


    def click_icon(self):

        self.click(self.icon_xpath, "xpath")

    def verify_signIn_label(self):

        self.elementDisplayed(locator=self.signIn_label_xpath, LocatorType="xpath", msg="Sign In label is displayed")


    def verify_emailMobileNumber_label(self):

        self.elementDisplayed(self.emailMobileNumber_label_xpath, "xpath", "Email or mobile phone number label is displayed")


    def verify_Help_footerlabel(self):

        self.elementDisplayed(self.Help_footerlabel_xpath, "xpath", "Help footer label is displayed")


    def verify_textrow_label(self):

        self.elementDisplayed(self.textrow_label_xpath, "xpath", "Legal Text Row is displayed")


    def verify_auth_emailID_label(self):

        self.elementDisplayed(self.auth_emailID_label_xpath, "xpath", "Email address is displayed for authorization")


    def click_change_link(self):

        self.click(self.change_link_xpath, "xpath")

    def verify_Password_label(self):

        self.elementDisplayed(self.Password_label_xpath, "xpath", "Password label is displayed")


    def click_ForgotPassword_link(self):

        self.click(self.ForgotPassword_link_xpath, "xpath")

    def click_ConditionsOfuse_link(self):

        self.click(self.ConditionsOfuse_link_xpath, "xpath")

    def click_PrivacyNotice_link(self):

        self.click(self.PrivacyNotice_link_xpath, "xpath")

    def click_Help_link(self):

        self.click(self.Help_link_xpath, "xpath")
#----------------------------FUNCTIONAL BLOCK---------------------------------------------

    def Login(self,email,paswd):
        self.lp.hoverAccount_list()
        self.lp.click_SignInAcnt_Btn()
        time.sleep(10)
        #self.verify_signIn_label()
        self.enter_emailID(email)
        self.click_Continuebtn()
        self.verify_Password_label()
        self.enter_password(paswd)
        self.click_signinbtn()
        self.hp.HelloUsername_xpath()

    def validate_blankEmailEntry(self,Email):
        # self.lp.hoverAccount_list()
        # self.lp.click_SignInAcnt_Btn()
        self.verify_signIn_label()
        self.enter_emailID(Email)
        self.click_Continuebtn()
        self.elementDisplayed(self.EnterYrEmail_alert_xpath, "xpath", "Email cannot be blank")


    def invalid_EmailEntry(self,Email):  #enter invalid email address like missing (@, .com)
        # self.lp.hoverAccount_list()
        # self.lp.click_SignInAcnt_Btn()
        self.verify_signIn_label()
        self.enter_emailID(Email)
        self.click_Continuebtn()
        self.elementDisplayed(self.ValidEmail_alert_xpath, "xpath", "Invalid email format: '@' is missing")



    def invalid_AcontEntry(self,Email): #enter non registered email address
        # self.lp.hoverAccount_list()
        # self.lp.click_SignInAcnt_Btn()
        self.verify_signIn_label()
        self.enter_emailID(Email)
        self.click_Continuebtn()
        self.elementDisplayed(self.InvalidAcnt_xpath, "xpath", "There was a problem with the email")




    def validate_blankPasswordEntry(self,password):
        # self.lp.hoverAccount_list()
        # self.lp.click_SignInAcnt_Btn()
        self.verify_signIn_label()
        self.enter_emailID()
        self.click_Continuebtn()
        self.verify_Password_label()
        self.enter_password(password)
        self.click_signinbtn()
        self.elementDisplayed(self.EnterYrPassword_alert_xpath, "xpath", "Password cannot be blank")


    def LandingPageEntry(self):
        self.click_icon()
        # self.lp.verify_amazonLogo()

    def CreatAct(self):
        self.click_createNew_account()
        self.ca.verify_CreateAccount_label()

    def validate_EmailID(self,email_mobilenumber):
        for i in range (52):
            self.enter_emailID(email_mobilenumber)
        Text=self.GetAttribute(self.email_textbox_xpath, "xpath","value")
        if (len(Text)>50):
            print("Email field accepts more than 50 characters")
        else:
            print("Email field accepts only 50 characters")


    def EntryTo_ConditionsOfUse(self):
        self.click_ConditionsOfuse_link()
        self.cond.verify_ConditionsOfUse()

    def EntryTo_PrivacyNotice(self):
        self.click_PrivacyNotice_link()
        self.pn.verify_PrivacyNotice()

    def NeedHelp_FunctionChk(self):
        self.click_Needhelf_Link()
        # Check if both elements are displayed after first time Need Help click
        if (self.elementDisplayed(self.ForgotYrPassword_xpath, "xpath","NeedHelp Function Check 1 is successful")) and (self.elementDisplayed(self.OtherIssues_xpath, "xpath","NeedHelp Function Check 1 is successful")):
            print("NeedHelp Function Check Passed")
        self.click_Needhelf_Link()
        # Check if both elements are no longer displayed after second time Need Help click
        if not self.elementDisplayed(self.ForgotYrPassword_xpath, "xpath","NeedHelp Function Check 2 is successful") and not self.elementDisplayed(self.OtherIssues_xpath, "xpath","NeedHelp Function Check 2 is successful"):
            print("NeedHelp Function Check Passed")


    def ForgotYrPassword_Check(self):
        self.click_Needhelf_Link()
        self.click(self.ForgotYrPassword_xpath, "xpath")
        self.PA.verify_PasswordAssistance()


    def OtherIssuesSignIn_Check(self):
        self.click_Needhelf_Link()
        self.click(self.OtherIssues_xpath, "xpath")
        self.OI.verify_AccountLoginIssues()

    def AmazonBusiness_Check(self):
        self.click(self.ShopAmazonBusiness_link_xpath, "xpath")
        self.AB.verify_AmazonBusiness()


    def Help_Check(self):
        self.click_Help_link()
        self.acs.verify_AmazonCustomerService()

    def Change_Validation(self):
        self.enter_emailID()
        self.click_Continuebtn()
        self.verify_Password_label()
        self.click_change_link()
        self.verify_signIn_label()

    def FrogotPassword_Validation(self):
        self.enter_emailID()
        self.click_Continuebtn()
        self.verify_Password_label()
        self.click_ForgotPassword_link()
        self.PA.verify_PasswordAssistance()
        self.elementDisplayed(self.EmailPA_xpath, "xpath", "Password Assistance page opened with Email address entry")


