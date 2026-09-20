"""
案例一；根据用户输入的用户名密码进行登录操作：
    1.正确的用户名密码为：xvyican/666888 admin/123456 dongkewei/888666
    2.输入用户名和密码进行登录，直到登陆成功，程序结束；登录失败提示用户并继续运行
    3.输入的用户名和密码不能为空

    # # #
    break  只能够出现在循环当中，表示结束，跳出循环的含义
    continue 只能够出现在循环当中，表示中断本次循环，直接进入下一次循环
"""

# 案例：
# while True:
# # 1.接受用户输入用户名和密码
#     user_name = input("请输入用户名:")
#     user_password = input("请输入用户密码:")
# # 2.校验：输入的用户名和密码不能为空
#     if user_name == "" or user_password == "":
#         print("用户名或密码不能为空！")
#         continue
# # 3.判断用户名和密码是否正确
#     if user_name == "xvyican" and user_password == "666888":
#         print("登陆成功！欢迎进入B站首页~")
#         break
#     elif user_name == "dongkewei" and user_password == '888666':
#         print("登陆成功！欢迎进入B站首页~")
#         break
#     elif user_name == 'admin' and user_password == '123456':
#         print("登陆成功！欢迎进入B站首页~")
#         break
#     else:
#         print('用户名或密码错误请重新输入：')



# # 练习：新增需求: 5次登录机会，输入错误五次，就不允许在操作了 其他需求同上
# limit = 1
# while limit != 5:
# # 1.接受用户输入用户名和密码
#     user_name = input("请输入用户名:")
#     user_password = input("请输入用户密码:")
# # 2.校验：输入的用户名和密码不能为空
#     if user_name == "" or user_password == "":
#         print("用户名或密码不能为空！")
#         continue
# # 3.判断用户名和密码是否正确
#     if user_name == "xvyican" and user_password == "666888":
#         print("登陆成功！欢迎进入B站首页~")
#         break
#     elif user_name == "dongkewei" and user_password == '888666':
#         print("登陆成功！欢迎进入B站首页~")
#         break
#     elif user_name == 'admin' and user_password == '123456':
#         print("登陆成功！欢迎进入B站首页~")
#         break
#     else:
#         print('用户名或密码错误请重新输入：')
#         limit = limit + 1
#
# print('用户名或密码错误五次，系统已被锁定！



# 练习案例代码
for i in range(5):
    username = input("请输入用户名: ")
    password = input("请输入密码: ")
    if username == "admin" and password == "666888":
        print("登录成功")
        break
    elif username == "zhangsan" and password == "123456":
        print("登录成功")
        break
    elif username == "taoge" and password == "888666":
        print("登录成功")
        break
    else:
        print("登录失败")
        if i == 4:
            print("输入错误五次，不允许再登录")
            break

