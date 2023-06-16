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
    info = driver.find_elements(By.CLASS_NAME,"fa-angle-right")
    print(info)
# =========== Index Error, Debug ..... ================
    for i in range(len(info)):
        info = driver.find_elements(By.CLASS_NAME,"fa-angle-right")
        print(info)
        # Error Happened
        info[i].click()
        time.sleep(1)
        print(f"*{driver.find_element(By.CLASS_NAME,'header-title').text}*")
            
        timezone = driver.find_elements(By.CLASS_NAME,"timezoneSuffix")
        start = timezone[0].text
        end = timezone[1].text
        print(f"時間：{start}~{end}")
        print("-----------------------")
        driver.execute_script("window.history.go(-1)")
        time.sleep(2)
    next_page = driver.find_elements(By.XPATH,"/html/body/div[3]/div[2]/section[1]/div/div[2]/ul/li")
    try:
        if next_page[-1].text != ',':
            print(f"共{next_page[-1].text}頁")
            break
        next_page[-1].click()
    except IndexError:
        break