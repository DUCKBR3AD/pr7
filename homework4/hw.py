a = int(input("ведите число a: "))
b = int(input("ведите число b: "))
c = int(input("ведите число c: "))
try:
except ValueError:
  print("Неправильный ввод, введите число")
  break
x = a*b +4*c
print(x)
