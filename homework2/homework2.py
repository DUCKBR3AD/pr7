a = int(input("введите число:"))
try:
except ValueError:
  print("Неправильный ввод, введите ЧИСЛО")
  break
print("Число в двоичном виде:", str(bin(a))[2::],'\n',"Число в восьмеричном виде: ", str(oct(a))[2::])

