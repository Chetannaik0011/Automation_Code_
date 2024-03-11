import time

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox


def test_res():
    firefox_option=Options()
    firefox_option.add_argument("--disable-notification")
    drive=Firefox(options=firefox_option)
    drive.set_window_size(1920,1080)
    drive.implicitly_wait(10)
    drive.get("https://www.getcalley.com/page-sitemap.xml")

    def go_back(drive):
        time.sleep(1)
        drive.back()
        time.sleep(1)

    drive.find_element(By.XPATH,"//a[text()='https://www.getcalley.com/']").click()
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