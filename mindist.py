import math

def seed_data(file):
  list = []

  with open(file,"r") as my_file:
    for file_line in my_file:
        list.append([int(f) for f in file_line.split()])

  return list

def distance(dot1, dot2):
  return math.sqrt((dot1[0]-dot2[0])**2 + (dot2[1] - dot1[1])**2)

def income():
  list = seed_data("data.txt")

  min = math.fabs(list[0][0] - list[1][0]) + math.fabs(list[1][1] - list[0][1])
  min_dots = [list[0], list[1]]
  for dot1 in list:
    for dot2 in list[:list.index(dot1)]:
      x = math.fabs(dot1[0] - dot2[0])
      y = math.fabs(dot1[1] - dot2[1])

      if x + y < min:
        min = x + y
        min_dots = [dot1, dot2]

  return(distance(min_dots[0], min_dots[1]))


print(income())