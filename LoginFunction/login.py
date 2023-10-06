import time
from Utilities.CustomLogger import LogGen
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from Utilities import Xlutils


class keyworddrivenframework:
    logger = LogGen.loggen()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    dropdwon_logout_xpath = "//*[@class='ant-dropdown-trigger text-white font-WorkSansMedium text-sm cursor-pointer']"
    button_logout_xpath = '//*[contains(text(),"Logout")]'
    path = "/Users/ticvictech/PycharmProjects/project_kdt/keywordDrivenFiles/keyworddrivenfile_Mk_login.xlsx"

    def __init__(self, driver):
        self.driver = driver

    # openBrowser
    def openBrowser(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def goToUrl(self):
        self.driver.get("http://10.0.8.111:3000/")

    def enterUserName(self):
        self.driver.find_element(By.XPATH, "//input[@type='text' or @type='email' or @name='username']").send_keys(
            "madmin@gmail.com")

    def enterPassword(self):
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Test@123")

    def clickLogin(self):
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def clicklogout(self):
        self.driver.find_element(By.XPATH, self.dropdwon_logout_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()

    def words(self):
        self.rows = Xlutils.getRowCount(self.path, 'Sheet1')
        self.logger.info("Number of Rows in a Excel:")
        self.logger.info(self.rows)
        self.columns = Xlutils.getColumnCount(self.path, 'Sheet1')
        self.logger.info("Number of Rows in a Excel:")
        self.logger.info(self.columns)
        for r in range(2, self.rows + 1):
            value = Xlutils.readData(self.path, 'Sheet1', r, 3)
            print(value)
