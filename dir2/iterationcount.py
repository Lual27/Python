sum = 0
iteration_count = int(
  input("How many numbers would you like to input? ")
)
for i in range(iteration_count):
  num = int(input(f"Enter the integer number {i + 1}:"))
  sum += num
print(f"Average is : {sum / iteration_count}")