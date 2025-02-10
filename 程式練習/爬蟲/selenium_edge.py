from selenium import webdriver
from selenium.webdriver.edge.service import Service



# 指定 Edge WebDriver 的路径
PATH = r"C:\selenium\msedgedriver.exe"  # 注意路径前加 r，表示原始字符串
service = Service(PATH)

# 初始化 Edge WebDriver、前往目标网址
driver = webdriver.Edge(service=service)
driver.get("https://www.nccu.edu.tw/app/home.php")  # 要進去的網址

# 等待几秒钟，方便观察页面加载情况
import time
time.sleep(5)

# 关闭浏览器
driver.quit()


#實例
# driver.get("https://tw.stock.yahoo.com")

# # 等待几秒钟，确保页面加载完成
# import time
# time.sleep(2)

# # 定位超链接并点击
# try:
#     link = driver.find_element(By.LINK_TEXT, "AI概念股")
#     link.click()
#     print("超链接已点击！")
# except Exception as e:
#     print("未找到超链接或点击失败：", e)



# # 等待几秒钟，观察结果
# time.sleep(5)

# # 关闭浏览器
# driver.quit()
































