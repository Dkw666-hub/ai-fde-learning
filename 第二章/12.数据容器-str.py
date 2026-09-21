"""
数据容器 - 字符串
 1.字符串特点：
    不可变性、有序性、可迭代性
 2.字符串的索引：
    正向索引：从0开始
    反向索引：从-1开始
 3.字符串的切片
    语法：
    s[start:end:step]
    start：开始索引默认为0
    end：结束索引默认为-1
    step：步长默认为1
"""


# # 字符串 ---》基本操作 不可变性、有序性、可迭代性
# s = "Hello-Python"
#
# print(s)
# print(s[7])  # 正向索引
# print(s[-5]) # 反向索引
#
# for i in s:
#     print(i)
#
# # 切片 正向
# print(s[0:5:1])
# print(s[:5:1])
# print(s[:5:])
# print(s[:5])
#
# print(s[6:12:1])
# print(s[6::1])
#
# #-----------------------------------------
# # 步长 --》正数：从前往后数； 负数：从后往前截取
# print('------------------------------')
# print(s[-1:-7:-1])
# print(s[-1::-2])



"""
字符串的常用方法
find（）      在字符串中查找字符，返回第一次出现的位置，找不到返回 -1        s.find（’Python‘）
count（）     统计子串在字符串中出现的次数                              s.count('H')
upper（）     将字符串中的所有字母转换为大写                             s.upper()
lower（）     将字符串中的所有字母转换为小写                             s.lower()
split（）     将字符串按照指定分隔符分割成列表                           s.split(' ')
strip()      去除字符串两端的空白字符或指定字符                          s.strip()/s.strip(' ')
replace()    将字符串中的指定字符替换为子串                             s.replace('H','c')  
startswith() 检查字符串是否以指定子串开头，返回布尔值                     s.startswith('H')
endswith()   检查字符串是否以指定子串结束，返回布尔值                     s.endswith('H')
"""

# --------------------字符串常用方法 --------------------
# s = 'Hello-Python-Hello-World '

# # find() 在字符串中查找字符，返回第一次出现的位置，找不到返回 -1
# index = s.find('o')
# print(index)
#
# # count() 统计子串在字符串中出现的次数
# c = s.count('l')
# print(c)
#
# # upper（）     将字符串中的所有字母转换为大写
# u = s.upper()
# print(u)
#
#
# # lower（）     将字符串中的所有字母转换为小写                             s.lower()
# l = s.lower()
# print(l)
#
# # split（）     将字符串按照制定分隔符分割成列表                           s.split(' ')
# sl = s.split("-")
# print(sl)
#
# # strip()      去除字符串两端的空白字符或指定字符                          s.strip()/s.strip(' ')
# print(type(s))
# ss = s.strip()
# print(ss)
#
# # replace()    将字符串中的指定字符替换为子串                             s.replace('H','c')
# sr = s.replace('-','_')
# print(sr)
#
# # startswith() 检查字符串是否以指定子串开头，返回布尔值                     s.startswith('H')
# print(s.startswith('Hello'))
#
# # endswith()   检查字符串是否以指定子串结束，返回布尔值
# print(s.endswith('Python'))
#
# print(('------------------------'))
# print(s)


# 字符串 - 案例1：
#邮箱格式校验：用户输入一个邮箱，验证邮箱格式是否正确，（包含一个@，至少一个，）
#如果正确的输出：邮箱格式正确 错误输出：邮箱格式错误

# # 方式一：
# # 1.接受用户邮箱
# email = input("请输入邮箱：")
#
# # 2.判断邮箱的格式
# if email.count('@') == 1 and email.find('.') >= 1:
#     print(f'{email}邮箱格式正确！')
# else:
#     print(f'{email}邮箱格式错误！')

# # 方式二：
# email = input("请输入邮箱：")
#
# # 2.判断邮箱的格式
# if email.count('@') == 1 and '.' in email:
#     print(f'{email}邮箱格式正确！')
# else:
#     print(f'{email}邮箱格式错误！')


# # 字符串---练习1：
# #输入一个字符串判断是否是回文(两边对称)
#
# # 方式一：
# # 1.接受用户字符串
# huiwen_str = input('请输入一串回文：')
#
# # 2.判断是否是回文
# if huiwen_str[::] ==huiwen_str[::-1]:
#     print(f'{huiwen_str} 是回文')
# else:
#     print(f'{huiwen_str} 不是回文')
#
#
"""
# 方式二(双指针法): 思路是从两边向中间遍历, 基于索引获取两边字符对比, 如果两边的字符不相等, 则不是回文, 否则是回文。
## 1. 输入一个字符串, 判断该字符串是否是回文(两边对称) 。  "黄山落叶松叶落山黄"  "上海自来水来自海上"
s = input('请输入一串回文：')

left = 0 # 左索引
right = len(s) - 1 # 右索引
flag = True

while left < right:
    if s[left] != s[right]:
        flag = False
        break
    left += 1
    right -= 1

if flag:
    print(f"'{s}' 是回文")
else:
    print(f"'{s}' 不是回文")
"""


# # 字符串---练习2：
# #将用户输入的10个字符，反转后全部转化为大写，然后记录在列表中，最后将列表内容，遍历输出出来
#
# # 1.接收用户输入10个字符串
# s_10  = []
# s_10i = []
# for j in range(10):
#     s = input('请输入字符串：')
#     # 2.将字符串进行反转---》全部转化为大写---》记录在列表中---》列表内容遍历输出
#     s_10i.append(s)
#     s_10.append(s[::-1].upper())
# print('输入字符串列表为',s_10i)
# print('反转大写后',s_10)
# print('-----------------')
#
# # 列表遍历输出
# for i in s_10:
#     print(i,end=' ')



