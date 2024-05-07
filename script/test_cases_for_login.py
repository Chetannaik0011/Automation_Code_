import time

from generic.basic_file import Base_Test
from selenium.webdriver.common.by import By




class Test_valid(Base_Test):

    def test_valid_login_functionality(self):
        input_email=self.driver.find_element(By.ID,"email")
        input_password=self.driver.find_element(By.ID,"password")
        sign_in=self.driver.find_element(By.XPATH,"//button[@type='submit']")

        input_email.send_keys("chetannaik044@gmail.com")
        input_password.send_keys("Chetan@11")
        sign_in.click()

        time.sleep(5)
        self.driver.get_screenshot_as_file("page.png")
        expect='dashboard'
        try:
            if expect in self.driver.current_url:
                print("valid credential successfully login and navigate to dashboard")


        except:
            print('login credential is invalid')






