# # 获取键盘上的数据 -- input(...)
# name = input("请输入您的姓名：")
# age = input("请输入您的年龄：")
# print(f"您的姓名是 {name} ，您的年龄是 {age} ")



# # 案例：银行卡ATM取款，余额100000
#         1.输入取款密码
#         2.输入取款金额
#         3.计算余额并输出
 # 总金额
# total = 100000
 # 密码
# password=666888

# inputpassword = input("请输入六位密码:")
# if int(inputpassword) == password:
#         print(f"密码正确: {password}")
#         num = input("请输入取款金额")
#         if total < int(num):
#             print("您的余额不足")
#         else:
#             print(f"您的余额为：{total - int(num)}" )
     
# else:
#         print("密码错误")



# 练习：根据用户输入的两个数字，计算两个数之和，并将其输出到控制台

num1 = int(input("请输入数字"))
num2 = int(input("请输入数字"))
print(f"{num1} + {num2}的和为：{int(num1) + int(num2)}")





