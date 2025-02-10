# =============================================================================
# def 函数名(参数列表):
#     """函数文档字符串（可选，用于描述函数的功能）"""
#     # 函数体（函数内部的代码）
#     return 返回值  # 返回值是可选的，如果不写，默认返回 None
# =============================================================================

# 先从最简单的无参数函数开始
def greet():
    """打印问候语"""
    print("Hello, welcome to Python learning!")

greet()

#1. 函数可以接收参数，参数是函数内部使用的变量，用于传递数据。
def add(a, b):
    """返回两个数的和"""
    return a + b

result = add(4, 5)
print(result)  


# 2.默认参数
# 你可以为函数的参数设置默认值，这样在调用函数时可以不传该参数。
def greet(name="Guest"):
    """打印问候语，可以指定名字"""
    print(f"Hello, {name}! Welcome to Python learning.")
greet()  # 使用默认值
# Hello, Guest! Welcome to Python learning.
greet("Alice")  # 指定参数
# Hello, Alice! Welcome to Python learning.


#3. 可变参数
# 如果你不确定函数会接收多少参数，可以使用可变参数。
def sum_numbers(*args):
    """计算任意数量数字的总和"""
    total = 0
    for num in args:
        total += num
    return total

print(sum_numbers(1, 2, 3, 4, 5))  # 输出 15


#4. 关键字参数
# 关键字参数允许你以键值对的形式传递参数，这样可以更灵活地指定参数。
def describe_pet(animal_type, pet_name):
    """打印宠物信息"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")

describe_pet(animal_type="hamster", pet_name="Harry")    


#5. 函数的返回值
# 函数可以返回一个值，使用 return 语句。如果没有 return，函数默认返回 None。
def multiply(a, b):
    """返回两个数的乘积"""
    return a * b
result = multiply(4, 5)
print(result)  # 输出 20

#練習:判斷奇偶
from concurrent.futures import ThreadPoolExecutor
nums=[1,2,3,4]

def leo(num):
    print(num)
    if num % 2 == 0:
        print("even")
    else :
        print("odd")
        
# leo(21)

with ThreadPoolExecutor() as executor:
    executor.map(leo, nums)

#for迴圈和平行運算不一樣的是，他是去遍歷列表的每一個值，一個一個代進去執行的
#而平行運算是將list內的每個值同時執行
for num in nums:
    print(num)
    if num % 2 == 0:
        print("even")
    else :
        print("odd")





























