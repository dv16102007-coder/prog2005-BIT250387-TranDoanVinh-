def bai_tap3 ():
 n=int(input("Nhập số từ 1 đến 9:"))
 if 1 <= n <= 9:
  for i in range(1,10):
   print(n, "x", i, "=", n*i)
 else:
  print("Số không hợp lệ")

