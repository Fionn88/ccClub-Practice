
# 爬蟲環境配置

## 背景

- 為了避免套件衝突，在此做法使用Docker 做到環境隔離

### Step By Step

- 啟動 Docker
```
docker run --name test-project -d -v /Users/FionnKuo/Documents/Developer/backend/python-by-docker:/app python:3.8 sleep infinity
```

- 安裝主角 => selenium
在這邊同時應該就會同時安裝 webdriver，這邊的路徑是 `/root/.wdm/drivers/chromedriver/linux64/114.0.5735.90/chromedriver`
```
pip install selenium
```


- 安裝 google-chrome binary
```
wget -qO - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/googlechrome-linux-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/googlechrome-linux-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
apt update
apt install google-chrome-stable
```

- 在 Debug 過程中出現此錯誤，安裝相應套件即可

> ./chromedriver: error while loading shared libraries: libnss3.so: cannot open shared object file: No such file or directory
```
apt-get install libnss3
```


#### 以下用python3 command 執行成功

> python3 test.py
```
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
url = "https://kktix.com/"
driver.get(url)
```