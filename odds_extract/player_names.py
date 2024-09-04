from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
url = 'https://www.rezultati.com/'
from selenium.webdriver.support.wait import WebDriverWait

def findTextBox():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div[1]/div/div[2]/div/button[2]').click()
    driver.find_element(By.XPATH, '//html/body/header/div/div[1]/div/span').click()
    driver.find_element(By.XPATH, '/html/body/header/div/div[1]/div/div/div/div[2]/div/button').click()
#driver.find_element(By.XPATH, '/html/body/header/div/div[1]/div/div/div/div[2]/div/ul/li[36]/button').click()
#driver.find_element(By.XPATH, '/html/body/header/div/div[1]/div/div/div/div[2]/div/button').click()
#element.click()
    actions = ActionChains(driver)

    # Navigate through the dropdown using arrow keys
    for _ in range(10):  # Adjust the range to scroll to the desired option
        actions.send_keys(Keys.ARROW_DOWN).perform()
        actions.send_keys(Keys.ARROW_DOWN).perform()
        actions.send_keys(Keys.ARROW_DOWN).perform()
    # Add a slight delay if needed to mimic natural scrolling
    #import time

    time.sleep(3)
    # Select the highlighted option by pressing Enter
    actions.send_keys(Keys.ENTER).perform()
    driver.find_element(By.XPATH, '/html/body/header/div/div[1]/div/div/div/div[2]/div/ul/li[36]/button').click()

    return driver


def findPlayerName(name, driver: webdriver.Chrome):
    #driver = findTextBox()
    driver.find_element(By.XPATH, '/html/body/header/div/div[1]/div/div/div/div[2]/input').send_keys(name)
    time.sleep(2.5)

    s = driver.find_element(By.XPATH, '/html/body/header/div/div[1]/div/div/div/div[3]/div/a[1]/div[2]').text

    driver.find_element(By.XPATH, '/html/body/header/div/div[1]/div/div/div/div[2]/input').clear()

    return s
    #driver.find_element(By.XPATH, '/html/body/header/div/div[1]/div/div/div/div[2]/input').send_keys('Nadal')

    #a  = driver.find_element(By.XPATH, '/html/body/header/div/div[1]/div/div/div/div[3]/div/a[1]/div[2]').text
    #print(a)

#driver.find_element(By.XPATH, '/html/body/header/div/div[1]/div/div/div/div[3]/div/a[1]/div[2]').click()
# Keep the browser open for 10 seconds to see the result
    #driver.quit()




#print(s)
#print(name)
#time.sleep(10)
