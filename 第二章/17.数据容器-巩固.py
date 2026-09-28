# 要求：请写一段 Python 代码，完成以下 5 个任务（不能用现成的函数，只能自己写逻辑）：
#
# 计算每个学生的总分：遍历列表，为每个学生字典新增一个键 "total"（总分），值是语数外三科之和。
#
# 计算每科的平均分：分别计算语文、数学、英语的全班平均分（保留1位小数）。
#
# 找出总分最高的学生：输出总分最高学生的姓名和总分。（如果有并列，输出第一个即可）
#
# 格式化输出成绩单：按以下格式打印全班成绩单（要求用 f-string 对齐，名字占 5 个字符宽度，左对齐）：

# #========== 成绩单 ==========
# 姓名: 张三   | 语文: 90 | 数学: 95 | 英语: 88 | 总分: 273
# 姓名: 李四   | 语文: 85 | 数学: 92 | 英语: 96 | 总分: 273

students = [
    {"name": "张三", "chinese": 90, "math": 95, "english": 88},
    {"name": "李四", "chinese": 85, "math": 92, "english": 96},
    {"name": "王五", "chinese": 95, "math": 88, "english": 90},
    {"name": "赵六", "chinese": 78, "math": 85, "english": 82},
    {"name": "孙七", "chinese": 92, "math": 96, "english": 94}
]

# 1.遍历列表，计算学生总分,并新增键值对，总分

for student in students:
    total = student['chinese'] + student['math'] + student['english']
    student['total'] = total
    print(student)

# 2.计算每科的平均分：分别计算语文、数学、英语的全班平均分（保留1位小数）。
# 方式一：
# chinese_total = []
# math_total = []
# english_total = []
# for student in students:
#     chinese_total.append(student['chinese'])
#     math_total.append(student['math'])
#     english_total.append(student['english'])

# 方式二：
chinese_total = [student['chinese'] for student in students]
math_total = [student['math'] for student in students]
english_total = [student['english'] for student in students]
scores_total = [student['total'] for student in students]

chinese_avg = sum(chinese_total) / len(chinese_total)
math_avg = sum(math_total) / len(math_total)
english_avg = sum(english_total) / len(english_total)
print(f'语文平均分：{chinese_avg:.2f} \n 数学平均分：{math_avg:.2f} \n 英语平均分：{english_avg:.2f}')

# 找出🐣单科/总分最高的学生：输出总分最高学生的姓名和总分。（如果有并列，输出第一个即可）

chinese_max_name = [student['name'] for student in students if student['chinese'] == max(chinese_total)]
math_max_name = [student['name'] for student in students if student['math'] == max(math_total)]
english_max_name = [student['name'] for student in students if student['english'] == max(english_total)]
total_max_name= [student['total'] for student in students if student['total'] == max(scores_total)]

print(f"语文最高分：{chinese_max_name} \n 数学最高分：{math_max_name} \n 英语最高分：{english_max_name}")




