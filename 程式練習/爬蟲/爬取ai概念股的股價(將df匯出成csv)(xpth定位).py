import requests
from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

# 输入 Yahoo 股市类股网址
url_1 = "https://tw.stock.yahoo.com/class-quote?category=AI%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7&categoryLabel=%E6%A6%82%E5%BF%B5%E8%82%A1"
web = requests.get(url_1)  # 取得网页内容(html)

# 使用 lxml 解析 HTML
tree = etree.HTML(web.text)

# 定位到目标的母区块
# 使用 XPath 定位母区块
parent_block = tree.xpath('//*[@id="main-1-ClassQuotesTable-Proxy"]/div/div[3]/div[2]/div/div/ul')

# 检查是否找到了母区块
if parent_block:
    parent_block = parent_block[0]  # 获取第一个匹配的母区块
    # 从母区块中提取所有 <a> 标签的 href 属性
    urls = parent_block.xpath(".//li/div/div[1]/div[2]/div/a/@href")
    print(urls)
else:
    print("未找到目标母区块")

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
        }

# 使用 ThreadPoolExecutor 并发执行
results = []

with ThreadPoolExecutor() as executor:
    futures = executor.map(getStock, urls)
    for result in futures:
        if result:
            results.append(result)

#print(results)
#将结果转换为 DataFrame
df = pd.DataFrame(results)

# 保存为 CSV 文件
df.to_csv(r"C:\python\程式練習\stock_data.csv", index=False, encoding='utf-8-sig')

# print(urls[0])





# # 定位到母节点
# content_section = tree.xpath("//div[@id='main-container']/section[@id='content']")[0]

# # 从母节点开始选择其他元素
# article_titles = content_section.xpath(".//article/h2")
# for title in article_titles:
#     print(title.text)