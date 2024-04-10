import time

from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



def test_flipkart_application():
    drive=Chrome()
    drive.implicitly_wait(50)
    drive.get("https://www.amazon.com/")
    drive.maximize_window()
    action=ActionChains(drive)
    element=drive.find_element(By.XPATH," //span[contains(text(),'Back to to')]")
    action.scroll_to_element(element).perform()
    drive.find_element(By.XPATH,"(//span[text()='Sign in'])[3]").click()
    drive.find_element(By.ID,"ap_email").send_keys('9380995158')
    drive.find_element(By.ID,"continue").click()
    drive.find_element(By.ID,"ap_password").send_keys('Chetu07@n')
    drive.find_element(By.ID,"signInSubmit").click()



    try:
        result=drive.find_element(By.XPATH,"//span[text()='Hello, Chetan']").is_displayed()
        print("Login succesfull")
        assert result


    except:
        print("Login unsuccesfull")



#test for search product

def test_search_product():
    drive = Chrome()
    drive.implicitly_wait(50)
    drive.get("https://www.amazon.com/")
    drive.maximize_window()
    drive.find_element(By.ID,"twotabsearchtextbox").send_keys("iphone15 plus")
    drive.find_element(By.ID,"nav-search-submit-button").click()
    product_text=drive.find_element(By.XPATH,"(//span[@class='a-size-medium a-color-base a-text-normal'])[1]").text
    print("product text:-",product_text)
    product_price=drive.find_element(By.XPATH,"//span[@class='a-price-whole']").text
    print("productprice:-",product_price)
    time.sleep(5)
