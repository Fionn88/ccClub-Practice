from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ["enable-automation"]) #解除自動化控制提示
option.add_experimental_option('useAutomationExtension', False) 
option.add_argument('--disable-infobars')

driver = webdriver.Chrome(options=option) 
driver.maximize_window() #最大化視窗
driver.get("https://www.fujintreeshop.com/categories/hikiniku-reservation") #訂位網址

# driver.find_element('css selector', 'div[class="info-box-inner-wrapper"]').click() # 定位在上一層也可以
driver.find_element('css selector', 'div[class="title text-primary-color   "]').click() # 抓class名稱等於指定字串的第一個標籤
# driver.find_element('css selector', 'div[class*="title text-primary-color"]').click() # 抓class名稱包含指定字串的第一個標籤
driver.implicitly_wait(15)
# driver.execute_script("window.scrollTo(0, 200)") #移動卷軸
while True:
    try:
        driver.find_element('css selector', 'div[class="product-detail-button-container"]').click() #加入購物車按鈕(需等待另一按鈕出現)
        time.sleep(7)
        driver.find_element('css selector', 'div[class="cart-chkt-btn-cont"]').click() #訂單結帳按鈕
        break
    except NoSuchElementException: #如果沒找到,則重試
        driver.execute_script("window.scrollTo(0, 200)") #移動卷軸
        time.sleep(0.2)

time.sleep(6)
driver.execute_script("window.scrollTo(0, 400)") #移動卷軸
time.sleep(6)
driver.find_element('css selector', 'a[class="btn btn-success btn-block btn-checkout"]').click() #前往結帳按鈕
time.sleep(6)

#進入結帳頁面
order_customer_name = driver.find_element('css selector', 'input[id="order-customer-name"]') #顧客名稱
order_customer_email = driver.find_element('css selector', 'input[id="order-customer-email"]') #顧客EMAIL
order_customer_phone = driver.find_element('css selector', 'input[id="order-customer-phone"]') #顧客電話
order_customer_name.send_keys("王小明")
order_customer_email.send_keys("123@gmail.com")
order_customer_phone.send_keys("0911111111") #輸入資料
time.sleep(6)
driver.find_element('css selector', 'input[data-e2e-id="order-delivery-recipient-is-customer_checkbox"]').click() #按下checkbox按鈕
#地址下拉式選單
time.sleep(5)
driver.execute_script("window.scrollTo(0, 400)") #移動卷軸
address_select = Select(driver.find_element('css selector', 'select[name="order[delivery_address][city]"]'))
address_select.select_by_index(1)
time.sleep(5)
address2_select = Select(driver.find_element('css selector', 'select[id="tw_address_2"]'))
address2_select.select_by_index(1)
time.sleep(5)
address3 = driver.find_element('css selector', 'input[name="order[delivery_address][address_1]"]')
address3.send_keys("愛心路5號") #輸入地址
#提交前要先選擇我同意checkbox
driver.find_element('css selector', 'input[data-e2e-id="checkout-policy_checkbox"]').click() 
# driver.find_element('css selector', 'button[id="place-order-recaptcha"]').click() #提交訂單按鈕
time.sleep(13)
# driver.close()