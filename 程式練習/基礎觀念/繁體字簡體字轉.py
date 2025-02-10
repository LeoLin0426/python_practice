from opencc import OpenCC
cc = OpenCC('s2t')  # 简体转繁体
print(cc.convert("这是一个测试"))

