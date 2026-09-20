'''
match...case语法 匹配 结构 和 数据 ，匹配成功执行操作

match 表达式 :
    case 值1 :
        操作1
    case 值2 if 条件表达式 :
        操作2
    case 值3 | 值4
        操作4
    case _ :
        默认操作

'''


# #工作日程安排
# day = input("请输入星期几（1-7）")

# match day :
#     case "1" :
#         print("周一你要学习python")
#     case "2" :
#         print("周二你要学习agent")
#     case "3" :
#         print("周三你要去参加招聘会")
#     case "4" :
#         print("周四你要学习java")
#     case "5" :
#         print("周五你要去开会")
#     case "6" | "7" :
#         print("周末啦，可以休息放松啦，并总结一下本周学习内容")
#     case _ :
#         print("匹配失败哦")



# #简易计算器，可以以实现 + - * /运算，用户需要输入需要运算的两个数以及运算符号
# num1 = float(input("请输入第一个数："))
# num2 = float(input("请输入第二个数："))
# operation = input("请输入运算符号：")

# match operation :
#     case "+" :
#         print(f"{num1} + {num2} = {num1 + num2}")
#     case "-" :
#         print(f"{num1} - {num2} = {num1 - num2}")
#     case "*" :
#         print(f"{num1} * {num2} = {num1 * num2}")
#     case "/" if num2 != 0 : #if条件成立才匹配这个值
#         print(f"{num1} / {num2} = {num1 / num2}")
#     case _ :
#         print("操作有误！")



# #简单游戏指令系统：根据玩家输入的不同指令，控制游戏角色执行相应的动作
# while(1):
#     instruction = input("请输入指令：")

#     match instruction :
#         case '上' | 'w' | 'W' :
#             print("角色向上移动")

#         case '下' | 's' | 'S' :
#             print("角色向下移动")

#         case '左' | 'a' | 'A' :
#             print("角色向左移动")

#         case '右' | 'd' | 'D' :
#             print("角色向右移动")

#         case '跳' | ' ' :
#             print("角色跳跃")

#         case '攻击' | 'j' | 'J' :
#             print("角色攻击")

#         case '退出' | 'esc' | 'ESC' :
#             print("角色退出游戏")
#             break
#         case _ :
#             print("操作失败")



