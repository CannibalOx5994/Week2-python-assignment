my_list = []                           # Create empty list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
 # my_list = [10, 20, 30, 40]

my_list.insert(1, 15)                  # Insert 15 at second position
  # my_list = [10, 15, 20, 30, 40]

my_list.extend([50, 60, 70])           # Extend with another list
  # my_list = [10, 15, 20, 30, 40, 50, 60, 70]

my_list.pop()                          # Remove last element
  # my_list = [10, 15, 20, 30, 40, 50, 60]

my_list.sort()                         # Sort ascending
 #my_list = [10, 15, 20, 30, 40, 50, 60]

print(my_list.index(30))               # Find index of 30   #  Output = 3
