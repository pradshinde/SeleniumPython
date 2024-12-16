from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Chromeservice
from webdriver_manager.chrome import ChromeDriverManager


class webDriver():

    def setUP(self):

        URL= "https://www.amazon.com/"

        driver= webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(URL)

        return driver


