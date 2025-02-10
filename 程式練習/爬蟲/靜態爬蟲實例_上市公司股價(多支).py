import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
# 建立要抓取的股票网址清单
stock_urls = [
    ' https://tw.stock.yahoo.com/quote/3231.TW',
    'https://tw.stock.yahoo.com/quote/2439.TW'
]

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
    print(f'{title.get_text()} : {a.get_text()} ( {s}{b.get_text()} )')

# 使用 ThreadPoolExecutor 并发执行
with ThreadPoolExecutor() as executor:
    executor.map(getStock, stock_urls)  # 开始同时爬取股价
