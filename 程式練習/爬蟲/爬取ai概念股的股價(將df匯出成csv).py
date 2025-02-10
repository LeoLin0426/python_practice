import requests
from bs4 import BeautifulSoup
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

# 输入 Yahoo 股市类股网址
url_1 = "https://tw.stock.yahoo.com/class-quote?category=AI%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7&categoryLabel=%E6%A6%82%E5%BF%B5%E8%82%A1"
web = requests.get(url_1)  # 取得网页内容(html)
soup = BeautifulSoup(web.text, "html.parser")

# 定位到目标的 <ul> 列表区块
ul_block = soup.find("ul", class_="M(0) P(0) List(n)")

# 检查是否找到了 <ul> 区块
if ul_block:
    # 提取 <ul> 区块中所有 <a> 标签的 href 属性
    urls = [a['href'] for a in ul_block.find_all('a', href=True)]
else:
    print("未找到目标 <ul> 区块")
    urls = []


# 将刚刚的抓取程式变成「函式」
def getStock(url):
    web = requests.get(url)
    soup = BeautifulSoup(web.text, "html.parser")
    title = soup.find_all(class_=["Fw(b)", "Fz(24px)"])[0]
    a = soup.select('.Fw\(b\).Fz\(32px\)')[0]  # 如果出现错误，可以使用 .Fz\(32px\) 转义
    b = soup.select('.Fw\(b\).Fz\(20px\)')[0]  # 如果出现错误，可以使用 .Fz\(20px\) 转义
    s = ''
    try:
        if soup.select('#main-0-QuoteHeader-Proxy')[0].select('.C\(\$c-trend-down\)')[0]:
            s = '-'
    except:
        try:
            if soup.select('#main-0-QuoteHeader-Proxy')[0].select('.C\(\$c-trend-up\)')[0]:
                s = '+'
        except:
            s = '-'
    # print(f'{title.get_text()} : {a.get_text()} ( {s}{b.get_text()} )')
    return {
            '公司': title.get_text(),
            '漲跌幅':s+b.get_text(),
            '股價': a.get_text()
        } #將結果輸出並以字典儲存

# 使用 ThreadPoolExecutor 并发执行
results = [] #先建立一個list用來存放後面執行輸出的字典

with ThreadPoolExecutor() as executor:
    for result in executor.map(getStock, urls):
        if result: #若輸出結果為真(存在)
            results.append(result) #將輸出的字典放入列表中

# 将结果转换为 DataFrame
df = pd.DataFrame(results)

# 保存为 CSV 文件
df.to_csv(r"C:\Users\旻駿\OneDrive\桌面\python\stock_data.csv", index=False, encoding='utf-8-sig')

# print(urls[0])
