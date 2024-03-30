#載入Selenium相關模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys


# 定義driver的變數，然後選擇webdriver裡面的chrome功能
# 新版的Selenium已經不需要再建立物件實體 (讚!)
driver = webdriver

# 設置 Chrome 選項 - 設定不要一直自己關掉
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# 初始化 WebDriver 並傳入選項
driver = webdriver.Chrome(options=chrome_options)

#取得網頁
driver.get("https://www.fujintreeshop.com/categories/hikiniku-reservation")
#print(driver.page_source) 取得網頁原始碼
#<div class="title text-primary-color   "> 空格代表這個元素有兩個不同的屬性，因此如果使用title text-primary-color   會找不到
#tags=driver.find_elements(By.CLASS_NAME, "text-primary-color   ") 只用第二個屬性當作篩選標準 (CLASS NAME只能選一種)
products=driver.find_elements(By.CSS_SELECTOR,".title.text-primary-color") #使用CSS選擇器，同時符合兩種屬性的標籤會被印出來
driver.implicitly_wait(30) #30秒內有找到的話就可以 (全局有效?)
for product in products:
    if "鑰匙圈" in product.text:
        product.click()
        break
    else:
        continue
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
#time.sleep(1)
driver.maximize_window() #把網頁放到最大

#選擇顏色
color=driver.find_element(By.XPATH,'//*[@id="Content"]/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/variation-label-selector/div/div/div[2]')
color.click()

#加入購物車
cart=driver.find_element(By.XPATH,'//*[@id="btn-main-checkout"]')
cart.click()
time.sleep(0.5) #等待0.5秒加入購物車

#前往購物車
gotoCart=driver.find_element(By.XPATH,'//*[@id="btn-checkout"]')
gotoCart.click()

#往下捲動200px才能看到頁面
driver.execute_script("window.scrollBy(0, arguments[0]);", 200)
time.sleep(0.5)

#選擇付款方式 -- 注意使用select的時候只需要用find_element
paymentMethod=driver.find_element(By.CSS_SELECTOR,"[id='order-payment-method']") 
select = Select(paymentMethod) #要先初始化Select (chatGPT說一定要這樣，我也不知道為什麼)
select.select_by_visible_text("虛擬帳戶線上匯款")

#等待付款方式跳轉後按結帳
time.sleep(0.5)
#checkOut=driver.find_element(By.XPATH,'//*[@id="checkout-container"]/div/div[3]/div[5]/div[2]/section/div[2]/a')
checkOut=driver.find_element(By.CSS_SELECTOR,'.btn.btn-success.btn-block.btn-checkout') #無法用id定位，可能是因為id是在網頁加載的時候動態生成的
checkOut.click()

#輸入姓名
customerName = driver.find_element(By.ID, "order-customer-name")
customerName.send_keys("盧豆皮")

#輸入email
customerEmail = driver.find_element(By.ID, "order-customer-email")
customerEmail.send_keys("123@gmail.com")

#輸入電話
customerPhone = driver.find_element(By.ID, "order-customer-phone")
customerPhone.send_keys("0912345798")

#選擇送貨資料同顧客資料的checkbox
copyInfo = driver.find_element(By.CSS_SELECTOR, "[data-e2e-id='order-delivery-recipient-is-customer_checkbox']")
copyInfo.click()

#找不到方法變更電話國碼 QQ
# countryList = driver.find_element(By.CSS_SELECTOR,"aria-expanded")
# countryList.click()
# phoneCountry = driver.find_elements(By.XPATH,'//*[@id="iti-0__item-af"]')#li不能使用select，有顯示option才能使用select
# for country in phoneCountry:
#     print(country.text)

#選擇縣市
addressCity = driver.find_element(By.CSS_SELECTOR, "[custom-translation='城市 / 縣']")
select = Select(addressCity)
select.select_by_visible_text("宜蘭縣")

#選擇地區
addressArea = driver.find_element(By.CSS_SELECTOR, "[custom-translation='地區']")
select = Select(addressArea)
select.select_by_visible_text("264 員山鄉")

#輸入地址
addressDetail = driver.find_element(By.CSS_SELECTOR, "[custom-translation='地址']")
addressDetail.send_keys("新店路123號")

#同意隱私政策、不同意註冊會員
agreePoliy =  driver.find_element(By.CSS_SELECTOR, "[data-e2e-id='checkout-policy_checkbox']")
agreeSignup = driver.find_element(By.CSS_SELECTOR, "[data-e2e-id='checkout-signup_checkbox']")
#送出訂單
placeOrder = driver.find_element(By.ID, "place-order-recaptcha")

agreePoliy.click()
agreeSignup.click()
placeOrder.click()