import requests
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://tw.stock.yahoo.com/quote/3481.TW'    # 輸入Yahoo 股市類股網址
web = requests.get(url)                          # 取得網頁內容(html)
soup = BeautifulSoup(web.text, "html.parser")    
#將html文字檔轉成樹狀結構，後面會更方便提取，資訊會直接存在soup中
#後續就是直接對soup處理，如:soup.select()或soup.find()

#目標抓股票名稱、即時價格和漲跌幅
# 找到 h1 的内容，通常<h1>标签包含页面的标题信息。
title = soup.find_all(class_=["Fw(b)", "Fz(24px)"])[0]
# print(title)
  
#股價
# 挑選 class 中同時有 Fz(32px)和Fw\(b\) 的内容
#select()方法查找所有class为Fz(32px)的元素，并取第一个元素。
a = soup.select('.Fw\(b\).Fz\(32px\)')[0]
# print(a)

#漲幅
# 挑選 class 中同時有 Fz(20px)和Fw\(b\) 的内容
b = soup.select('.Fw\(b\).Fz\(20px\)')[0]  
# print(b.get_text())

#漲跌
# # 定义一个变量s，用于存储股票的涨跌状态（+表示上涨，-表示下跌）。
s = ''  

# 涨跌状态判断逻辑：
# 首先尝试查找id为main-0-QuoteHeader-Proxy的元素，然后在其内部查找class为C($c-trend-down)的元素。
# 如果找到，表示股票下跌，将s设置为-。
# 如果没有找到C($c-trend-down)，则尝试查找class为C($c-trend-up)的元素。
# 如果找到，表示股票上涨，将s设置为+。
# 如果两个条件都不满足，表示股票平盘，将s设置为-
try:
    if soup.select('#main-0-QuoteHeader-Proxy')[0].select('.C\(\$c-trend-down\)')[0]:
        s = '-'
except:
    try:
        if soup.select('#main-0-QuoteHeader-Proxy')[0].select('.C\(\$c-trend-up\)')[0]:
            s = '+'
    except:
        s = '-'
print(s)
# 使用格式化字符串（f-string）打印股票信息：
# title.get_text()：获取股票名称（<h1>标签的内容）。
# a.get_text()：获取股票当前价格（class为Fz(32px)的内容）。
# s：股票的涨跌状态（+或-）。
# b.get_text()：股票的涨跌幅度（class为Fz(20px)的内容）
print(f'{title.get_text()} : {a.get_text()} ( {s}{b.get_text()} )')  # 印出结果


# =============================================================================
# try...except：
# 用于异常处理。捕获代码运行过程中可能出现的错误或异常，并提供处理这些异常的逻辑。
# 语法结构：
# try:
#     # 尝试执行的代码
# except ExceptionType as e:
#     # 如果捕获到指定类型的异常，执行这里的代码
# =============================================================================

# =============================================================================
# name = "Alice"
# age = 30
# print(f"Hello, my name is {name} and I am {age} years old.")
# 输出：
# Hello, my name is Alice and I am 30 years old.
# =============================================================================





