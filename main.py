with open("file1.txt") as file1:
  file_1 = file1.readlines()
  print(file_1)

with open("file2.txt") as file2:
  file_2 = file2.readlines()
  print(file_2)

#new_list = [new_item for item in list if test]
result = [int(num) for num in file_1 if num in file_2]
print(result)
