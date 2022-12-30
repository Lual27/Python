sum = 0
count = 0
num = int(input("Enter a positive integer, negative to exit: "))
while num >= 0:
  sum += num
  count += 1
  num = int(input("Enter a positive integer, negative to exit : "))
if count > 0:
  print(f"Average is: {sum / count}")
  
