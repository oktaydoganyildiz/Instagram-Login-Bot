from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://www.instagram.com/?hl=tr")
time.sleep(2)

email=browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
password=browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
email.send_keys("") #Write your Username
password.send_keys("") #Write your Password

login_button=browser.find_element_by_xpath("//*[@id='loginForm']/div[1]/div[3]/button")
login_button.click()

time.sleep(5)

notnow=browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")
notnow.click()

time.sleep(5)

notnow_2=browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
notnow_2.click()



browser.fullscreen_window()




