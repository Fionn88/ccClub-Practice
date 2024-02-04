# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome(options=chrome_options)
# url = "https://www.fujintreeshop.com/categories/hikiniku-reservation"
# driver.get(url)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 你的資訊
url = "https://www.fujintreeshop.com/categories/hikiniku-reservation"

# 方法一：執行前需開啟chromedriver.exe且與執行檔在同一個工作目錄
driver = webdriver.Chrome()

# 最大化視窗
driver.maximize_window()
driver.get(url)


driver.find_element(By.XPATH, '/html/body/div[10]/div/div/div[2]/div[2]/div[2]/div/div[1]/product-item/a/div[1]/div/div[1]/img').click()

# //*[@id="Content"]/div/div/div[2]/div[2]/div[2]/div/div[1]/product-item/a/div[1]/div/div[1]/img
# product_console.click()
# 等待10秒
time.sleep(10)
# 關閉瀏覽器
driver.quit()