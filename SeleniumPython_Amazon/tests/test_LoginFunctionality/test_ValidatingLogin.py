import pytest

from SeleniumPython_Amazon.driver.webDriver import webDriver
from SeleniumPython_Amazon.Pages.landingPage.landingPage import landingPage
from SeleniumPython_Amazon.Pages.Login.LoginPage import LoginPage
from SeleniumPython_Amazon.Pages.CreateAccount.CreateAccount import CreateAccount


class TestCases():


    @pytest.fixture(autouse=True)
    def initialize(self):

        self.lp=LoginPage()

    @pytest.mark.run(order=1)
    def test_TC01(self):

        self.lp.Login("pradshinde@gmail.com","Lrd_amen1")

    # @pytest.mark.run(Order=2)
    # def test_TC02(self):
    #     landingPage.Search_xpath(self,"Mobile")
    #
    # @pytest.mark.run(Order=3)
    # def test_TC03(self):
    #     landingPage.verify_amazonLogo()
    #
    # @pytest.mark.run(Order=4)
    # def test_TC04(self):
    #     landingPage.select_BooksCategory()
    #
    # @pytest.mark.run(Order=5)
    # def test_TC05(self):
    #     LoginPage.validate_blankEmailEntry(self,"")
    #
    # @pytest.mark.run(Order=6)
    # def test_TC06(self):
    #     LoginPage.invalid_EmailEntry(self,"pradshindegmail.com")
    #
    # @pytest.mark.run(Order=7)
    # def test_TC07(self):
    #     LoginPage.LandingPageEntry()
    #
    # @pytest.mark.run(Order=8)
    # def test_TC08(self):
    #     LoginPage.NeedHelp_FunctionChk()
    #
    # @pytest.mark.run(Order=9cd
    # def test_TC09(self):
    #     LoginPage.ForgotPassword_link_xpath()
    #
    # @pytest.mark.run(Order=10)
    # def test_TC10(self):
    #     CreateAccount.password_mismatch_chk(self,"abcde1","abcdd1")
    #
    #
