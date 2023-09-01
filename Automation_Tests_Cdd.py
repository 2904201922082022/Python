import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


#step 1
def test_access_salsa():
    url = 'https://salsa-dev.vercel.app/login'
    # set chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    # set driver
    driver = webdriver.Chrome(os.getcwd()+'/chromedriver', options=chrome_options)
    driver.get(url)
    # take screenshot
    driver.save_screenshot('screenshot.png')
    driver.quit()

#step 2
#user input login field

driver1 = webdriver.login_xpath
driver1.find_element_by_xpath.login_xpath.send_keys.login_value
webdriver.save_screenshot("step2.png")


#step 3
#user input password
driver2 = webdriver.pwd_xpath
driver2.find_element_by_xpath.pwd_xpath.send_keys.pwd_value
webdriver.save_screenshot("step3.png")

#step 4
#user can access Salsa
driver3 = webdriver.Continue_Btn
driver3.find_element_by_xpath.Continue_Btn.click()
webdriver.save_screenshot("step4.png")
TimeoutError.sleep(2)