from SeleniumPython_Amazon.driver.webDriver import webDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from SeleniumPython_Amazon.utility.logger import logger


class seleniumdriver:

    def __init__(self):
        self.webdriver= webDriver()
        self.driver=self.webdriver.setUP()
        self.log=logger.logging(self)

    def getByType(self,LocatorType):

        try:
            locatorType= LocatorType.lower()
            if (locatorType== "id"):
                return By.ID
            elif (locatorType=="name"):
                return By.NAME
            elif (locatorType=="class"):
                return By.CLASS_NAME
            elif (locatorType=="xpath"):
                return By.XPATH
            elif (locatorType=="tagname"):
                return By.TAG_NAME
            elif (locatorType=="cssselector"):
                return By.CSS_SELECTOR
            self.log.info("****** By type is callable")

        except:
            self.log.error("****** By type is not callable")


    def findElement(self, locator, LocatorType):
        element=None
        try:
            bytype =self.getByType(LocatorType)
            element = self.driver.find_element(bytype,locator)
            self.log.info("****** ELEMENT IS IDENTIFIED WITH LOCATOR",locator)

        except:
            self.log.error("****** ELEMENT IS NOT IDENTIFIED WITH LOCATOR",locator)
        return element

    def sedKeys(self, locator, LocatorType, value):
        try:
            element = self.findElement(locator, LocatorType)
            element.send_keys(value)
            self.log.info("****** ELEMENT IS IDENTIFIED WITH LOCATOR", locator)
        except:
            self.log.error("****** ELEMENT IS NOT IDENTIFIED WITH LOCATOR", locator)


    def click(self, locator, LocatorType):
        try:
            element = self.findElement(locator, LocatorType)
            element.click()
            self.log.info("****** ELEMENT IS IDENTIFIED WITH LOCATOR", locator)
        except:
             self.log.error("****** ELEMENT IS NOT IDENTIFIED WITH LOCATOR", locator)

    def elementDisplayed(self, locator, LocatorType, msg):
        try:
            element = self.findElement(locator, LocatorType)
            if element.is_displayed():
                self.log.info("****** ELEMENT IS IDENTIFIED WITH LOCATOR", locator,msg)
        except:
            self.log.error("****** ELEMENT IS NOT IDENTIFIED WITH LOCATOR",locator)



    def elementEnabled(self, locator, LocatorType, msg):
        try:
            element = self.findElement(locator, LocatorType)
            if (element.is_enabled()):
                self.log.info("****** ELEMENT IS IDENTIFIED WITH LOCATOR", locator, msg)
        except:
            self.log.error("****** ELEMENT IS NOT IDENTIFIED WITH LOCATOR",locator)


    def elementSelected(self, locator, LocatorType, msg):
        try:
            element = self.findElement(locator, LocatorType)
            if (element.is_selected()):
                self.log.info("****** ELEMENT IS IDENTIFIED WITH LOCATOR", locator, msg)
        except:
            self.log.error("****** ELEMENT IS NOT IDENTIFIED WITH LOCATOR",locator)

    def DropdnSelectByValue(self, locator, LocatorType, value):
        try:
            element = self.findElement(locator, LocatorType)
            Options = Select(element)
            Options.select_by_value(value)
            self.log.info("****** ELEMENT IS IDENTIFIED WITH LOCATOR", locator)
        except:
            self.log.error("****** ELEMENT IS NOT IDENTIFIED WITH LOCATOR",locator)

    def DropdnSelectByIndex(self, locator, LocatorType, index):
        try:
            element = self.findElement(locator, LocatorType)
            Options = Select(element)
            Options.select_by_index(index)
            self.log.info("****** ELEMENT IS IDENTIFIED WITH LOCATOR", locator)
        except:
            self.log.error("****** ELEMENT IS NOT IDENTIFIED WITH LOCATOR",locator)

    def DropdnSelectByText(self, locator, LocatorType, text):
        try:
            element = self.findElement(locator, LocatorType)
            Options = Select(element)
            Options.select_by_visible_text(text)
            self.log.info("****** ELEMENT IS IDENTIFIED WITH LOCATOR", locator)
        except:
            self.log.error("****** ELEMENT IS NOT IDENTIFIED WITH LOCATOR",locator)

    def hoverElement(self, locator, LocatorType):
        try:
            element = self.findElement(locator, LocatorType)
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
            self.log.info("****** ELEMENT IS IDENTIFIED WITH LOCATOR", locator)
        except:
            self.log.error("****** ELEMENT IS NOT IDENTIFIED WITH LOCATOR", locator)

    def ClkNHold(self, locator, LocatorType):
        try:
            element = self.findElement(locator, LocatorType)
            action = ActionChains(self.driver)
            action.click_and_hold(element).perform()
            self.log.info("****** ELEMENT IS IDENTIFIED WITH LOCATOR", locator)
        except:
            self.log.error("****** ELEMENT IS NOT IDENTIFIED WITH LOCATOR", locator)

    def ClkNHoldRelease(self, locator, LocatorType):
        try:
            element = self.findElement(locator, LocatorType)
            action = ActionChains(self.driver)
            self.ClkNHold(locator, LocatorType)  # Hold the click
            action.release(element).perform()  # Release the click
            self.log.info("****** ELEMENT IS IDENTIFIED WITH LOCATOR", locator)
        except:
            self.log.error("****** ELEMENT IS NOT IDENTIFIED WITH LOCATOR", locator)

    def Doubleclick(self, locator, LocatorType):
        try:
            element = self.findElement(locator, LocatorType)
            action = ActionChains(self.driver)
            action.double_click(element).perform()
            self.log.info("****** ELEMENT IS IDENTIFIED WITH LOCATOR", locator)
        except:
            self.log.error("****** ELEMENT IS NOT IDENTIFIED WITH LOCATOR", locator)


    def Key_Down(self, locator, LocatorType, key):
        try:
            element = self.findElement(locator, LocatorType)
            action = ActionChains(self.driver)
            action.key_down(element, key).perform()
            self.log.info("****** ELEMENT IS IDENTIFIED WITH LOCATOR", locator)
        except:
            self.log.error("****** ELEMENT IS NOT IDENTIFIED WITH LOCATOR", locator)


    def Key_Up(self, locator, LocatorType, key):
        try:
            element = self.findElement(locator, LocatorType)
            action = ActionChains(self.driver)
            action.key_up(key, element).perform()
            self.log.info("****** ELEMENT IS IDENTIFIED WITH LOCATOR", locator)
        except:
            self.log.error("****** ELEMENT IS NOT IDENTIFIED WITH LOCATOR", locator)


    def GetAttribute(self, locator, LocatorType, name):
        element = None
        try:
            element = self.findElement(locator, LocatorType)
            element.get_attribute(name)
            self.log.info("****** ELEMENT IS IDENTIFIED WITH LOCATOR", locator)
        except:
            self.log.error("****** ELEMENT IS NOT IDENTIFIED WITH LOCATOR", locator)
        return element