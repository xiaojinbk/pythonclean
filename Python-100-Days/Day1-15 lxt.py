# 练习 1：华氏温度转摄氏温度

# f = float(input('请输入华氏温度'))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))

# 练习 2：输入圆的半径计算计算周长和面积。

# import math
#
# radius = float(input('请输入圆的半径'))
# perimeter = 2 * math.pi * radius
# area = math.pi * radius * radius
# print('周长：%.2f' % perimeter)
# print('面积：%.2f' % area)

# 练习 3：输入年份判断是不是闰年

# year = int(input('请输入年份：'))
# is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
# print(is_leap)

# 练习 4：英制单位与公制单位互换

# value = float(input("请输入长度："))
# # unit = input("请输入单位：")
# # if unit == 'in' or unit == '英寸':
# #     print('%f英寸 = %f厘米' % (value, value * 2.54))
# # elif unit == 'cm' or unit == '厘米':
# #     print('%f厘米 = %f英寸' % (value, value / 2.54))
# # else:
# #     print('请输入有效单位')

# 练习 5：掷骰子决定做什么

# from random import randint
#
# face = randint(1, 6)
# if face == 1:
#     result = '唱首歌'
# elif face == 2:
#     result = '跳个舞'
# elif face == 3:
#     result = '学狗叫'
# elif face == 4:
#     result = '学猫叫'
# elif face == 5:
#     result = '学猪叫'
# else:
#     result = '念绕口令'
#
# print(result)

# 练习 6：百分制成绩转等级制

# score = float(input('请输入成绩'))
# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >= 70:
#     grade = 'C'
# elif score >= 60:
#     grade = 'D'
# else:
#     grade = 'E'
#
# print('对应的等级是：', grade)

# 练习 7：输入三条边长如果能构成三角形就计算周长和面积

# import math
#
# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))
# if a + b > c and a + c > b and b + c > a:
#     print('周长:%f' % (a + b + c))
#     p = (a + b + c) / 2
#     area = math.sqrt(p * (p - a) * (p - b) * (p - c))
#     print('面积:%f' % area)
# else:
#     print('不能构成三角形')

# 练习 8：个人所得税计算器。

# salary = float(input('本月收入：'))
# insurance = float(input('五险一金：'))
# diff = salary - insurance - 3500
#
# if diff <= 0:
#     rate = 0
#     deduction = 0
# elif diff < 1500:
#     rate = 0.03
#     deduction = 0
# elif diff < 4500:
#     rate = 0.1
#     deduction = 105
# elif diff < 9000:
#     rate = 0.2
#     deduction = 555
# elif diff < 35000:
#     rate = 0.25
#     deduction = 1005
# elif diff < 55000:
#     rate = 0.3
#     deduction = 2755
# elif diff < 80000:
#     rate = 0.35
#     deduction = 5505
# else:
#     rate = 0.45
#     deduction = 13505
#
# tax = abs(diff * rate - deduction)
# print('个人所得税：%2.f元' % tax)
# print("实际到手收入：%2.f元" % (diff + 3500 - tax))

