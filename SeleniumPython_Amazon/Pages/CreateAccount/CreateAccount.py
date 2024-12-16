from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from SeleniumPython_Amazon.driver.webDriver import webDriver
#from SeleniumPython_Amazon.Pages.landingPage.landingPage import landingPage
from SeleniumPython_Amazon.Pages.basePage import basePage



class CreateAccount(basePage):
    icon_xpath = "//div[@class='a-section a-spacing-medium a-text-center']//*[@class='a-icon a-icon-logo']"
    CreateAccount_xpath="//div[@class='a-box-inner']//*[@class='a-spacing-small']"
    YourName_label_xpath = "//div[@class='a-row a-spacing-base']//*[@for='ap_customer_name']"
    customer_textbox_xpath = "//div[@class='a-row a-spacing-base']//*[@type='text']"
    email_textbox_xpath= "//div[@class='a-box-inner']//*[@for='ap_email']"
    Password_Label_xpath="//label[@for='ap_password' and @class='a-form-label' and contains(text(),'Password')]"
    password_textbox_xpath = "//div[@class='a-row a-spacing-base']//*[@id='ap_password']"
    PasswordChk_Label_xpath = "//label[@for='ap_password_check' and @class='a-form-label' and contains(text(),'Re-enter password')]]"
    passwordChk_textbox_xpath = "//div[@class='a-row a-spacing-base']//*[@id='ap_password_check']"
    continue_button_xpath = "//input[@id='continue']"
    textrow_label_xpath = "//div[@id='legalTextRow']"
    Buying_forWork_label_xpath = "//span[@class='a-text-bold']"
    BusinessAcntRegister_Link_xpath="//*[@class='a-section a-spacing-base']//*[@id='ab-enhanced-registration-link']"
    AlreadyAcnt_label_xpath="//*[contains(text(),'Already have an account?')]"
    SignIn_Link_xpath="//div[@class='a-row']//*[@class='a-link-emphasis']"
    Help_footerlabel_xpath = "//*[@class='a-section a-spacing-small a-text-center a-size-mini']//*[contains(text(),'Help')]"
    last_footer_line_label_xpath= "//div[@class='a-section a-spacing-none a-text-center']/*[@class='a-size-mini a-color-secondary']"
    PasswordMatch_alert_xpath = "//div[@class='a-box-inner a-alert-container']//*[contains(text(),'Passwords must match')]"
    LessPswdChars_alert_xpath = "//div[@class='a-box-inner a-alert-container']//*[contains(text(),'Enter at least 6 characters')]"

    def __init__(self):
        self.bp = basePage()
        # self.lp=landingPage()


    def verify_icon(self):

        self.elementDisplayed(self.icon_xpath, "xpath", "Icon is displayed")


    def click_icon(self):

        self.click(self.icon_xpath, "xpath")

    def verify_CreateAccount_label(self):

        self.elementDisplayed(self.CreateAccount_xpath, "xpath", "Create account label is displayed")


    def verify_YourName_label(self):

        self.elementDisplayed(self.YourName_label_xpath, "xpath", "Your name label is displayed")


    def enter_customer_name(self,customer_textbox):

        self.bp.sedKeys(self.customer_textbox_xpath,"xpath",customer_textbox)

    def enter_emailID(self,email_mobilenumber):

        self.bp.sedKeys(self.email_textbox_xpath,"xpath",email_mobilenumber)

    def verify_Password_Label(self):

        self.elementDisplayed(self.Password_Label_xpath, "xpath", "Password label is displayed")


    def enter_password(self,password):

        self.bp.sedKeys(self.password_textbox_xpath,"xpath",password)

    def verify_PasswordChk_Label(self):

        self.elementDisplayed(self.PasswordChk_Label_xpath, "xpath", "Re-enter password label is displayed")


    def enter_passwordChk_textbox(self,password):

        self.bp.sedKeys(self.passwordChk_textbox_xpath, "xpath", password)

    def click_Continuebtn(self):

        self.click(self.continue_button_xpath, "xpath")

    def verify_textrow_label(self):

        self.elementDisplayed(self.textrow_label_xpath, "xpath", "Legal Text Row is displayed")


    def verify_Buying_for_work(self):

        self.elementDisplayed(self.Buying_forWork_label_xpath, "xpath", "Buying for work? is displayed")


    def click_BusinessAcnt_register_Link(self):

        self.click(self.BusinessAcntRegister_Link_xpath, "xpath")

    def verify_AlreadyAcnt_label(self):

        self.elementDisplayed(self.AlreadyAcnt_label_xpath, "xpath", "Already have an account? is displayed")


    def click_SignIn_Link(self):

        self.click(self.SignIn_Link_xpath, "xpath")

    def verify_Help_footerlabel(self):

        self.elementDisplayed(self.Help_footerlabel_xpath, "xpath", "Help footer label is displayed")

    def verify_last_footer_line(self):

        self.elementDisplayed(self.last_footer_line_label_xpath, "xpath", "The last footer line is displayed")


#------------------------------FUNCTIONAL BLOCK--------------------------------------

    def CreatAct(self):
        # self.lp.hoverAccount_list()
        # self.lp.click_StartHere_Link()
        self.verify_CreateAccount_label()

    def LandingPageEntry(self):
        self.CreatAct()
        self.click_icon()
        # self.lp.verify_amazonLogo()

    def password_mismatch_chk(self,password,password1):  #enter different password on Re-enter password field
        self.enter_customer_name()
        self.enter_emailID()
        self.enter_password(password)
        self.enter_passwordChk_textbox(password1)
        self.click_Continuebtn()
        self.elementDisplayed(self.PasswordMatch_alert_xpath, "xpath", "Error: Passwords must match")



    def LessPaswdChars_chk(self,password):
        self.enter_customer_name()
        self.enter_emailID()
        self.enter_password(password)
        self.elementDisplayed(self.LessPswdChars_alert_xpath, "xpath", "Error:Enter at least 6 characters")
