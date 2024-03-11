import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.action_chains import ActionChains

#approach1
def test_functional():
    drive=Chrome()
    drive.implicitly_wait(10)
    drive.get("https://demo.dealsdray.com/")
    drive.maximize_window()
    drive.find_element(By.NAME,"username").send_keys('prexo.mis@dealsdray.com')
    drive.find_element(By.NAME,"password").send_keys('prexo.mis@dealsdray.com')
    drive.find_element(By.XPATH,"//button[@type='submit']").submit()
    drive.find_element(By.XPATH,"//span[text()='chevron_right']").click()
    drive.find_element(By.XPATH,"//span[text()='Orders']").click()
    drive.find_element(By.XPATH,"//button[@align='right']").click()
    time.sleep(2)
    drive.find_element(By.XPATH,"//input[@type='file']").send_keys("E:/demo-data.xlsx")
    drive.find_element(By.XPATH,"//button[contains(text(),'Import')]").click()
    time.sleep(2)
    drive.find_element(By.XPATH,"//button[contains(text(),'Validate')]").click()
    wait=WebDriverWait(drive,10)
    wait.until(Ec.alert_is_present())

    alert=drive.switch_to.alert
    alert.accept()
    time.sleep(3)

    drive.get_screenshot_as_file("pagescreenshot.png")
    print("Test completed")

    drive.quit()