import sys

def answer(n):
  seq = ''
  list = range(1,int(n))
  for num in list:
    seq += str(num)
    if seq.find(n) > -1:
      return seq.find(n) + 1
  return seq.find(n) + 1


print(answer(sys.argv[1]))

