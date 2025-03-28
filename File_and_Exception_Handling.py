# File and Exception Handling
# Exercise 1: Write a Python program to read a file and display its content
with open("C:\\Users\\17010\\OneDrive\\Desktop\\file1.txt","r") as file1:
    data = file1.read()
    print(data)



# Exercise 2: Write a Python program to copy the contents of one file to another file
print(f"Contents of source file is : ")
with open("C:\\Users\\17010\\OneDrive\\Desktop\\file1.txt","r") as src:
    data = src.read()
    print(data)
    
# writing contents of source file to destination file
with open("C:\\Users\\17010\\OneDrive\\Desktop\\destination.txt", "w") as dest:
    dest.write(data)
    
print(f"Contents of destination file after copying : ")    
with open("C:\\Users\\17010\\OneDrive\\Desktop\\destination.txt","r") as dest:
    content = dest.read()
    print(content)

print(f"Successfully copied the contents of one file to another!!!")



# Exercise 3: Write a Python program to read the content of a file and count the total number of words in that file.
with open("C:\\Users\\17010\\OneDrive\\Desktop\\sample.txt","r") as file3:
    data = file3.read()
    words = data.split()
    count = len(words)
    print(f"Content of file is : {data}")
    print("Total number of words in file =",count)



# Exercise 4: Write a Python program that prompts the user to input a string and converts it to an integer. 
# Use try-except blocks to handle any exceptions that might occur

try:
    user_input = input("Enter a number :")
    value = int(user_input)
    print(f"Inputted value is an integer : {value}")
except ValueError:
    print(f"Invalid input!! Please enter valid input.")



# Exercise 5: Write a Python program that prompts the user to input a list of integers and raises an exception if any of the integers in the list are negative. 

try:
    user_input = input("Enter a list of integers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    
    for num in numbers:
        if num < 0:
            raise ValueError("Negative numbers are not allowed.")
    
    print(f"You entered the valid list of integers: {numbers}")
except ValueError as e:
    print(f"Error: {e}")



# Exercise 6: Write a Python program that prompts the user to input a list of integers and computes the average of those integers. 
# Use try-except blocks to handle any exceptions that might occur.
# Use the finally clause to print a message indicating that the program has finished running.

try:
    user_input = input("Enter a list of integers seperated by spaces: ")
    numbers = list(map(int, user_input.split()))
    total_numbers = len(numbers)
    sum = 0
    for i in numbers:
        sum = sum + i
    average = sum/total_numbers
    print(f"Average of numbers = {average}")
except ValueError:
    print(f"Error: Please enter the valid integers!! ")
except ZeroDivisionError:
    print(f"Cannot find the average of an empty list !!!")
finally:
    print(f"The program has finished running!")



# Exercise 7 :  Write a Python program that prompts the user to input a filename and writes a string to that file. 
# Use try-except blocks to handle any exceptions that might occur and print a welcome message if there is no exception occurred. 
# Describe the step by step process.

try:
    # inputting the file path
    filename = input("Enter the filename path: ")
    # inputting the content to be written in the file
    content = input("Enter the text to write into the file: ")

    # writes the content to the file inputted
    with open(filename, 'w') as file:
        file.write(content)

    # reads the content from the file and prints the content
    with open(filename, 'r') as file:
        data = file.read()
        print(f"Content of file : {data}")
    
    print("Welcome! The file has been written successfully.")
except Exception as e:     # exception will be raised when invalid content or filename is inputted
    print(f"An error occurred: {e}")