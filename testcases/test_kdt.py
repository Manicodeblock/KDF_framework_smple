from Utilities import Xlutils
import time
from selenium.webdriver.common.action_chains import ActionChains

from Utilities.CustomLogger import LogGen
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import inspect
from LoginFunction.login import keyworddrivenframework
from Utilities.CustomLogger import LogGen
from webdriver_manager.chrome import ChromeDriverManager


class Test_loginkdt():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    path = "/Users/ticvictech/PycharmProjects/project_kdt/keywordDrivenFiles/keyworddrivenfile_Mk_login.xlsx"
    logger = LogGen.loggen()
    action = ActionChains(driver)


    # This function is to get the keywords from the Excel sheet




    def test_login(self):
        self.rows = Xlutils.getRowCount(self.path, 'Sheet1')
        self.logger.info("Number of Rows in a Excel:")
        self.logger.info(self.rows)
        self.columns = Xlutils.getColumnCount(self.path, 'Sheet1')
        self.logger.info("Number of Rows in a Excel:")
        self.logger.info(self.columns)
        time.sleep(2)
        # Create an instance of the class
        my_instance = keyworddrivenframework(self)
        # Use inspect to get a list of methods from keyworddrivenframework class
        methods_list = [name for name, _ in inspect.getmembers(my_instance, inspect.ismethod)]
        print("methods list ***********")
        print(methods_list[1])
        self.lgn = keyworddrivenframework(self.driver)
        time.sleep(2)
        self.driver.get("http://10.0.8.111:3000/")
        time.sleep(3)
        for r in range(2, self.rows + 1):
            value = Xlutils.readData(self.path, 'Sheet1', r, 3)
            if value == "test":
            # if value == methods_list[i]:
                print(r)
            else:
                print("test else part")











        # for r in methods_list:
        #     print(r)
        #     if r == "openBrowser":
        #         time.sleep(2)
        #         pass
        #         # self.lgn.openBrowser()
        #     elif r == "goToUrl":
        #         pass
        #         # self.lgn.goToUrl()
        #         time.sleep(2)
        #     elif r == "enterUserName":
        #         self.lgn.enterUserName()
        #         time.sleep(2)
        #     elif r == "enterPassword":
        #         self.lgn.enterPassword()
        #         time.sleep(2)
        #     elif r == "clickLogin":
        #         self.lgn.clickLogin()
        #         time.sleep(2)
        #     elif r == "click logout":
        #         self.lgn.clicklogout()
        #
        #



















