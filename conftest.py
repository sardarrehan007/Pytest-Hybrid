import subprocess
import unittest

import pytest
from selenium.webdriver.chrome import webdriver

from Librariries import *

# from DataDriven import TestData
from Main.ConfigReader import ReadConfig_EXECUTABLE_PATH


@pytest.fixture(params=["chrome"])
def init_driver(request):

    if request.param != "chrome":
        pass
    else:
        chrome_options = webdriver.Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--start-maximized")
        driver: webdriver = webdriver.Chrome(executable_path=ReadConfig_EXECUTABLE_PATH.SET_CHROME_EXECUTABLE_PATH(),
                                             options=chrome_options)

    request.cls.driver = driver
    print("Current session is {}".format(driver.session_id))

    yield

    driver.close()
    driver.quit()
