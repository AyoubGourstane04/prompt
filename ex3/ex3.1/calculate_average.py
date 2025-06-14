def calculate_average(numbers_list): 
    # This function calculates the average of numbers in a list 
    # It has some issues 
    total = 0
    for num in numbers_list: 
     total += num 
    average = total / len(numbers_list) 
    return average 

# Example of usage (might cause errors) 
my_nums = [1, 2, 'three', 4] # <-- Error here 
avg = calculate_average(my_nums) 
print(f"Average: {avg}")