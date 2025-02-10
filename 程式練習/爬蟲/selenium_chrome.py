#下載chromedriver
import requests
import os
import zipfile
import platform

# API URL
#api_url = "https://googlechromelabs.github.io/chrome-for-testing/latest-versions-per-milestone-with-downloads.json"

# 发送请求
try:
    response = requests.get(api_url, timeout=10)  # 设置超时时间
    response.raise_for_status()  # 检查请求是否成功
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Failed to fetch ChromeDriver details: {e}")
    print("Please check the URL or your network connection and try again.")
    exit(1)

# 获取 ChromeDriver 的版本信息
try:
    # 假设你已经知道需要的 Chrome 版本号
    chrome_version = "132.0.6834.111"
    version_info = data['milestones']['132']['downloads']['chromedriver']
except KeyError as e:
    print(f"Failed to find ChromeDriver version information: {e}")
    print("Please check the API response structure or Chrome version.")
    exit(1)

# 判断当前操作系统
current_os = platform.system().lower()  # windows, linux, or darwin
target_arch = "win64" if current_os == "windows" else "linux64" if current_os == "linux" else "mac-x64"

# 找到对应的下载链接
download_url = None
for info in version_info:
    if target_arch in info['platform']:
        download_url = info['url']
        break

if not download_url:
    print(f"No suitable ChromeDriver found for {current_os}")
else:
    # 下载 ChromeDriver
    driver_zip = "chromedriver.zip"
    try:
        with requests.get(download_url, stream=True) as r:
            r.raise_for_status()  # 检查下载请求是否成功
            with open(driver_zip, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print(f"Downloaded ChromeDriver from {download_url}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download ChromeDriver: {e}")
        exit(1)

    # 解压 ChromeDriver
    try:
        with zipfile.ZipFile(driver_zip, 'r') as zip_ref:
            zip_ref.extractall("./chromedriver")
        print(f"ChromeDriver for {current_os} extracted successfully to ./chromedriver!")
    except zipfile.BadZipFile as e:
        print(f"Failed to extract ChromeDriver: {e}")
        exit(1)

    # 清理下载的 zip 文件
    os.remove(driver_zip)
    print("Cleanup done. ChromeDriver is ready to use.")

    


import os
print("Current Working Directory:", os.getcwd())




from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('./chromedriver/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")









from selenium import webdriver

# 設定 WebDriver 路徑
driver_path = "C:\\Users\\旻駿\\chromedriver\\chromedriver-win64\\chromedriver.exe"

# 啟動瀏覽器
driver = webdriver.Chrome(driver_path)

# 打開 Google
driver.get("https://www.google.com")
print("Title:", driver.title)

# 關閉瀏覽器
driver.quit()

