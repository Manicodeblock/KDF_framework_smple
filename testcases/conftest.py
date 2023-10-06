import os.path
from datetime import datetime
from selenium import webdriver
# https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-pytho
# line number 16,17 are new updation of chrome driver packages and line number 26 and Drivers package contains a drivers no need aftrbthese updation
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup(browser):
    #global driver
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        #driver=webdriver.Chrome(executable_path="Drivers/chromedriverlt")
        print("Launching Chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="/home/ticvictech/Project_IBS/Drivers/geckodriver")
        print("Launching Firefox browser")
    else:
        print("empty")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        #driver = webdriver.Chrome(executable_path="/home/ticvictech/manikandan/PycharmProjects/Sixvercel_project/Drivers/chromedriver")
    return driver

def pytest_addoption(parser): #This method is to select the browser in CLI (run time as argument)
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):#return the browser value
    return request.config.getoption("--browser")
#it is hook for adding environment info into HTML report
#def pytest_configure(config):
 #   config._metadata['Project Name']='Mkanak'
  #  config._metadata['Module name']='LOGIN '
   # config._metadata['Tester'] ='Manikandan'
#it is hook for delete/modyfy environment info into HTML report
#@pytest.mark.optionalhook
#def pytest_metadata(metadata):
 #   metadata.pop("Javahome",None)
  #  metadata.pop("Plugins",None)




