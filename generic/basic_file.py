import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome


class Base_Test:

    @pytest.fixture(autouse=True)
    def pre_condition(self):
        self.driver=Chrome()
        self.driver.get("https://app.leadzen.ai/login")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    @pytest.fixture(autouse=True)
    def post_condition(self):
        yield
        self.driver.close()

