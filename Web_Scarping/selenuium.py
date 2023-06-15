from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
url = "https://kktix.com/"
driver.get(url)

search_input = driver.find_element(By.NAME, "search")
search_input.send_keys("展覽")
search_input.submit()

time.sleep(2)
time_console = driver.find_element(By.XPATH, '//*[@id="dLabe2"]/i')
time_console.click()
time.sleep(2)
this_month = driver.find_element(By.XPATH, '//*[@id="new_search_form"]/div/div/div[1]/div[2]/div[1]/ul/li[1]/ul/li[2]')
this_month.click()
time.sleep(2)
while True:
    info = driver.find_elements(By.CLASS_NAME,"pull-right")
    for i in range(len(info)):
            info = driver.find_elements(By.CLASS_NAME,"pull-right")
            info[i].click()
            time.sleep(1)
            print(f"*{driver.find_element(By.CLASS_NAME,'header-title').text}*")
            
            timezone = driver.find_elements(By.CLASS_NAME,"timezoneSuffix")
            driver.execute_script("window.history.go(-1)")
            time.sleep(1)