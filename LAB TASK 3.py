numbers = []
for i in range(1, 11):
  num = float(input(f"Enter number {i}: "))
  numbers.append(num)

total_sum = sum(numbers)
average = total_sum / len(numbers)
largest = max(numbers)
smallest = min(numbers)
even_count = sum(1 for x in numbers if x % 2 == 0)
odd_count = sum(1 for x in numbers if x % 2 != 0)

print(f"\nSum: {total_sum}")
print(f"Average: {average}")
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")