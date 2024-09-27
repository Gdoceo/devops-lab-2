numbers = input("Enter a number between 1 and 10").split()

numbers = [float(num) for num in numbers]

average = sum(numbers) / len(numbers)

print(average)

