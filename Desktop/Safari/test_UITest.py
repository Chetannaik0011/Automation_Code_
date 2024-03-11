import time

from selenium.webdriver.safari.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Safari
from selenium import webdriver


def test_res():
    safari_option=Options( )
    grid_url = "https://oauth-nchetan655-8c45f:498063b4-192f-4367-ba26-cd8e51b28dba@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
    drive = webdriver.Remote(command_executor=grid_url, options=safari_option)

    drive.set_window_size(1920, 1080)
    drive.implicitly_wait(20)
    drive.get("https://www.getcalley.com/page-sitemap.xml")

    def go_back(drive):
        time.sleep(1)
        drive.back()
        time.sleep(1)

    drive.find_element(By.XPATH, "//a[text()='https://www.getcalley.com/']").click()
    drive.get_screenshot_as_file("./homepage1.png")
    go_back(drive)

    drive.find_element(By.XPATH, "//a[contains(text(),'https://www.getcalley.com/calley-call-')]").click()
    drive.get_screenshot_as_file("./homepage2.png")
    go_back(drive)

    drive.find_element(By.XPATH, "//a[contains(text(),'https://www.getcalley.com/calley-pro')]").click()
    drive.get_screenshot_as_file("./homepage3.png")
    go_back(drive)

    drive.find_element(By.XPATH, "//a[contains(text(),'best-auto')]").click()
    drive.get_screenshot_as_file("./homepage4.png")
    go_back(drive)

    drive.find_element(By.XPATH, "//a[contains(text(),'how-calley')]").click()
    drive.get_screenshot_as_file("./homepage5.png")
    go_back(drive)

    print("Top 5 link succesfully open")

    drive.quit()