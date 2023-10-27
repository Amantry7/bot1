# h1 = int(input())*3600
# m1 = int(input())*60
# s1 = int(input())
# h2 = int(input())*3600
# m2 = int(input())*60
# s2 = int(input())
# print((h2 + m2 + s2)-(h1 + m1 + s1))


# def calc_average(lst):    return sum(lst) // len(lst)
  
# def determine_grade(av):    if 90 <= av <= 100:
#         return 'A'    elif 80 <= av < 90:
#         return 'B'    # etc
#     return 'F'
  
# N = 5ratings = []
# for i in range(N):    ratings.append(int(input(f'Введите {i}-ю оценку: ')))
# average = calc_average(ratings)print('ваш средний бал составляет:', average)
# print(determine_grade(average))


file_write = open('geeks.txt', 'w')
file_write.write("dfshkijl")
file_write.close
file_read = open('geeks.txt', 'r')
res = file_read.read()
print(res)