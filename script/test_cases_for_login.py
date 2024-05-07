import time

from generic.basic_file import Base_Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec




class Test_valid(Base_Test):

    def test_valid_login_functionality(self):
        input_email=self.driver.find_element(By.ID,"email")
        input_password=self.driver.find_element(By.ID,"password")
        sign_in=self.driver.find_element(By.XPATH,"//button[@type='submit']")

        input_email.send_keys("chetannaik044@gmail.com")
        input_password.send_keys("Chetan@11")
        sign_in.click()
        try:
            wait=WebDriverWait(self.driver,10)
            wait.until(Ec.url_to_be("https://app.leadzen.ai/dashboard"))
            assert self.driver.current_url=="https://app.leadzen.ai/dashboard"
            print("valid credential successfully login and navigate to dashboard")
        except:
            print("invalid credential")










