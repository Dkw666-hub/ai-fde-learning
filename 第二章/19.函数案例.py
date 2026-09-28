# 案例:
# 案例1.定义一个函数:根据传入的底和高计算三角形面积的函数(三角形面积=底*高/2)。
def triangle_area(b , h):
    """
    根据传入的底和高计算三角形面积
    :param b: 底
    :param h: 高
    :return: 面积
    """
    return b * h / 2

print('三角形面积：',triangle_area(3,4))


# 案例2.定义一个函数:计算传入的字符串中元音字母的个数(元音字母为 aeiouAEIOU)。
def count_aeiou(s):
    """
    计算传入的字符串中元音字母的个数
    :param s: 传入字符串
    :return: 元音个数
    """
    count = 0
    for y in s:
        if y in 'aeiouAEIOU':
            count += 1
    return count

print("hello world hello python OK 中元音字母个数为：",count_aeiou('hello world hello python OK'))


# 案例3.定义一个函数:计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数),并返回。
def calculate_list(score_list):
    """
    计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数),并返回.
    :param score_list: 传入的成绩列表
    :return: 最高分，最低分，平均分
    """
    max_score = max(score_list)
    min_score = min(score_list)
    avg_score = round(sum(score_list) / len(score_list) , 1)
    return max_score, min_score, avg_score

s_list = [520,450,620,321,456,521,321,666]
max,min,avg, = calculate_list(s_list)

print(f'最高分：{max}  最低分：{min}  平均分：{avg}')




# 练习:
# 练习1.定义一个函数，根据传入的分数，计算对应的分数等级并返回。
# 分数>= 90:A
# 分数>= 75:B
# 分数>= 60:C
# 分数<60:D

def calculate_list_grade(scores):
    """
    根据传入的分数，计算对应的分数等级并返回。
    :param scores: 传入分数
    :return: 分数等级 分数>= 90:A
                     分数>= 75:B
                     分数>= 60:C
                     分数<  60:D
    """
    if 0 <= scores <= 100:
        if scores >= 90:
            return "A"
        elif scores >= 75:
            return "B"
        elif scores >= 60:
            return "C"
        else:
            return "D"
        if scores < 60:
            return 'D'
        elif 60 <= scores < 75:
            return 'C'
        elif 75 <= scores < 90:
            return 'B'
        elif 90 <= scores:
            return 'A'
    else:
        print('输出成绩有误！')

print('您的成绩等级是：',calculate_list_grade(100))



# 练习2.定义一个函数，用于判断一个字符串是否是回文串，返回bool值。
# 把字符串反转，如果和原字符串相同，就是回文串。(如:"level"，"radar"，"黄山落叶松叶落山黄")
def palindrome_judge(s):
    """
    判断一个字符串是否是回文串，返回bool值。
    :param s: 字符串
    :return:  是回文：True 不是回文：False
    """
    return s == s[::-1]
    sfan = s[::-1]
    if sfan == s:
        return True
    else:
        return False

print(palindrome_judge('level'))
print(palindrome_judge('radar'))
print(palindrome_judge('黄山落叶松叶落山黄'))
print(palindrome_judge('黄山落叶松叶落山'))


# 练习3.定义一个函数:完成时间转换功能，将传入的秒转换为小时、分钟、秒。
def times_unit_conversion(seconds):
    """
    完成时间转换功能，将传入的秒转换为小时、分钟、秒。
    :param second: 传入秒
    :return: 小时，分钟，秒
    """
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    second = (seconds % 3600) % 60
    return f"{seconds} 转换为 {hours} 小时 {minutes} 分钟 {second} 秒"
print(times_unit_conversion(6000))


    # hour = round(seconds / 3600,1)
    # minute = round(seconds / 60,1)
    # return hour, minute, seconds

# hour,minute,seconds = times_unit_conversion(2000)
# print(f'2000秒等于 {hour}时  {minute}分钟  {seconds}秒')



# 练习4.定义一个函数:根据传入的三角形三个边的边长，判定三角形的类型(等边、等腰、普通，或者不能构成三角形)。
def triangle_judge(side_len1, side_len2, side_len3):
    """
    根据传入的三角形三个边的边长，判定三角形的类型(等边、等腰、普通，或者不能构成三角形)。
    :param side_len1: 边长1
    :param side_len2: 边长2
    :param side_len3: 边长3
    :return: 三角形类型
    """
    if side_len1 + side_len2 > side_len3 and side_len2 + side_len3 > side_len1 and side_len1 + side_len2 > side_len3:
        if side_len1 == side_len2 == side_len3:
            return '等边三角形~'
        elif side_len1 == side_len2 or side_len2 == side_len3 or side_len1 == side_len3:
            return '等腰三角形~'
        else:
            return '普通三角形'
    else:
        return '这不是三角形！'

print(triangle_judge(0.1,0.5,10))
print(triangle_judge(3,4,5))