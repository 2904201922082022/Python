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

