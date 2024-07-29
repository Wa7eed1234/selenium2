# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# c="c:\desktop\chromedriver"
# # chrom_path="/Users/ibrahimfakhry/Desktop/chromedriver"
# driver=webdriver.Chrome(executable_path=c)
# driver.get("https://identity.classter.com/ids/login?signin=78e109f3b5cbe0a5843c482a775c48b6")
#
# # Find the input element using its ID or other selector (e.g., name, class, xpath)
# input_element = driver.find_element(By.XPATH,'//*[@id="username"]' )
#
#
#
#
# # Fill in the input field with the desired value
# input_element.send_keys("awaelahmed1@ams-benha.com")
# next=driver.find_element(By.XPATH,'//*[@id="btnNext"]' )
# next.click()
# time.sleep(10)
# password=driver.find_element(By.XPATH,'//*[@id="i0118"]')
# password.send_keys("ahmed#123")
#
#
# next2=driver.find_element(By.XPATH,'//*[@id="idSIButton9"]')
# next2.click()
#
# yes=driver.find_element(By.XPATH,'//*[@id="lightbox"]/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]')
# yes.click()
# time.sleep(10)
# messege=driver.find_element(By.XPATH,'//*[@id="Menu_15"]/a')
# messege.click()
#
# time.sleep(5)
#
# # SSS=driver.find_element(By.XPATH,'//*[@id="page-wrapper"]/div[2]/div[1]/div[6]')
# # SSS.click()
# # time.sleep(5)
# no=driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[2]/div[1]/div[6]/div/div/div/div[3]/div/div/div/button')
# no.click()
#
# time.sleep(5)
# ms=driver.find_element(By.XPATH,'//*[@id="messageSubject"]')
# ms.send_keys("computer")
# time.sleep(5)
#
#
#
# sent=driver.find_element(By.XPATH,'//*[@id="send"]  ')
# sent.click()
#
#
# ok = driver.find_element(By.XPATH, '/html/body/div[8]')
# time.sleep(3)
#     # Locate the confirm button by CSS selector
# confirm_button = driver.find_element(By.CSS_SELECTOR, "button.confirm")
#
# # Click on the confirm button
# confirm_button.click()
#
# time.sleep(1000)
import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

c="c:\desktop\chromedriver"
# chrom_path="/Users/ibrahimfakhry/Desktop/chromedriver"
driver=webdriver.Chrome(executable_path=c)
driver.get("https://identity.classter.com/ids/login?signin=78e109f3b5cbe0a5843c482a775c48b6")

# Find the input element using its ID or other selector (e.g., name, class, xpath)
input_element = driver.find_element(By.XPATH,'//*[@id="username"]' )


# Fill in the input field with the desired value
input_element.send_keys("awaelahmed1@ams-benha.com")
next=driver.find_element(By.XPATH,'//*[@id="btnNext"]' )
next.click()
time.sleep(10)
password=driver.find_element(By.XPATH,'//*[@id="i0118"]')
password.send_keys("ahmed#123")


next2=driver.find_element(By.XPATH,'//*[@id="idSIButton9"]')
next2.click()

yes=driver.find_element(By.XPATH,'//*[@id="lightbox"]/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]')
yes.click()
time.sleep(10)
messege=driver.find_element(By.XPATH,'//*[@id="Menu_15"]/a')
messege.click()
time.sleep(5)
for i in range (100):
    sent=driver.find_element(By.XPATH,'//*[@id="page-wrapper"]/div[2]/div[1]/div[6]/div/div/div/div[3]/div/div/div/button')
    sent.click()
    time.sleep(5)
    ms=driver.find_element(By.XPATH,'//*[@id="messageSubject"]')
    ms.send_keys("this is the code , where is the money")
    time.sleep(5)
    next22=driver.find_element(By.XPATH,'//*[@id="send"]')
    next22.click()
    time.sleep(5)
    ok=driver.find_element(By.XPATH,'/html/body/div[8]')
    time.sleep(3)
    # Locate the confirm button by CSS selector
    confirm_button = driver.find_element(By.CSS_SELECTOR, "button.confirm")

    # Click on the confirm button
    confirm_button.click()



time.sleep(1000)