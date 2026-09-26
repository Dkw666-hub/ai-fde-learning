# 练习 基于现有知识开发一个教务管理系统

# 开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：

# 1.添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
# 2.修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
# 3.删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
# 4.查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
# 5.列出所有学生：遍历所有学生信息并输出。
# 6.统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学生姓名。
# 7.退出系统。

# 学生成绩录入格式：
# student_scores = {name1:{Chinese:XX,Math:XX,English:XX},name2...}

# 1.制作教务管理系统菜单
menu = """          
# # # # # # # # # # # # # # # # # # # # # 【菜单】 # # # # # # # # # # # # # # # # # # # # # #                                                                                    #            
# 1.添加学生信息 2.修改学生信息 3.删除学生信息 4.查询学生信息 5.列出所有学生 6.统计班级成绩 7.退出系统 #                                                                                         #            
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"""

print('欢迎来到教务管理系统！')
# 定义字典
student_scores = {}

while True:
# 输出菜单
    print(menu)
# 2.接收执行的操作
    choice = input('请选择要执行的操作（1-7）：')

# 3.根据用户输入内容操作执行字典的增删改查退
    match choice:
        case '1':
            students_name = input('请输入学生姓名:')
            if students_name not in student_scores :
                Chinese_scores = int(input('请输入语文成绩:'))
                Math_scores = int(input('请输入数学成绩:'))
                English_scores = int(input('请输入英语成绩:'))
                student_scores[students_name] = {'语文成绩':Chinese_scores,'数学成绩':Math_scores,'英语成绩':English_scores}
                print('学生信息添加完毕~')
            else:
                print(f'{students_name}学生信息已存在!')

        case '2':
            students_name = input('请输入要修改的学生姓名:')
            if students_name in student_scores:
                Chinese_scores = int(input('请输入语文成绩:'))
                Math_scores = int(input('请输入数学成绩:'))
                English_scores = int(input('请输入英语成绩:'))
                student_scores[students_name] = {'语文成绩': Chinese_scores, '数学成绩': Math_scores, '英语成绩': English_scores}
                print('学生信息修改完毕~')
            else:
                print(f'{students_name}学生信息不存在!')
        case '3':
            students_name = input('请输入要删除的学生姓名:')
            if students_name in student_scores:
                e = student_scores.pop(students_name)
                print(f'学生{e}的信息已全部删除')
            else:
                print(f'要删除学生{students_name}的信息不存在')

        case '4': # 查询单个学生成绩
            students_name = input('请输入要查询的学生姓名:')
            if students_name in student_scores:
                student_info = student_scores[students_name]
                print(f"学生:{students_name} \t 语文成绩:{student_info['语文成绩']} \t 数学成绩:{student_info['数学成绩']} \t 英语成绩:{student_info['英语成绩']}")
            else:
                print('要查询的学生信息不在系统中！')
        case '5': # 查询全部学生成绩
            for name in student_scores.keys():
                student_info = student_scores[name]
                print(f"学生:{name} \t\t 语文成绩:{student_info['语文成绩']} \t\t 数学成绩:{student_info['数学成绩']} \t\t 英语成绩:{student_info['英语成绩']}")
        case '6': # 统计出班级语文、数学、英语的最高分、最低分、平均分，并输出每个学科最高分最低分学生姓名
                  # student_scores = {name1:{’语文‘:XX,’数学‘:XX,’英语‘:XX},name2...}
            if not student_scores: #判断是否有信息
                print("系统中暂无学生信息，请先添加学生 ~")
                continue
            # 找出最高分、最低分...
            Chinese,Math,English = [],[],[]
            # for name,scores in student_scores.items():
            #     Chinese.append(scores['语文成绩'])
            #     Math.append(scores['数学成绩'])
            #     English.append(scores['英语成绩'])
            Chinese = [scores['语文成绩'] for name,scores in student_scores.items()]
            Math = [scores['数学成绩'] for name,scores in student_scores.items()]
            English = [scores['英语成绩'] for name,scores in student_scores.items()]

            print(f'语文成绩 \n 最高分:{max(Chinese)} \t 最低分:{min(Chinese)} \t 平均分: \t {sum(Chinese) / len(Chinese):.1f}')
            print(f'数学成绩 \n 最高分:{max(Math)} \t 最低分:{min(Math)} \t 平均分: \t {sum(Math) / len(Math):.1f}')
            print(f'英语成绩 \n 最高分:{max(English)} \t 最低分:{min(English)} \t 平均分: \t {sum(English) / len(English):.1f}')
                  # student_scores = {name1:{’语文‘:XX,’数学‘:XX,’英语‘:XX},name2...}
            chinese_max_students = [name for name,scores in student_scores.items() if scores['语文成绩'] == max(Chinese)]
            chinese_min_students = [name for name,scores in student_scores.items() if scores['语文成绩'] == min(Chinese)]

            math_max_students = [name for name,scores in student_scores.items() if scores['数学成绩'] == max(Math)]
            math_min_students = [name for name,scores in student_scores.items() if scores['数学成绩'] == min(Math)]

            english_max_students = [name for name,scores in student_scores.items() if scores['英语成绩'] == max(English)]
            english_min_students = [name for name,scores in student_scores.items() if scores['英语成绩'] == min(English)]
            print(f'语文最高分：{chinese_max_students} \t 语文最低分：{chinese_min_students}')
            print(f'数学最高分：{math_max_students} \t 数学最低分：{math_min_students}')
            print(f'英语最高分：{english_max_students} \t 英语最低分：{english_min_students}')
        case '7':
            print('bye~\n教务系统已退出')
            break
        case _:
            print('操作有误请输入1-7')


# 4.遍历统计输出班级语文数学英语成绩为一个列表，并找出其最高分最低分和平均分