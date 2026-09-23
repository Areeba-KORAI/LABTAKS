total_marks = 0
max_possible = 500

for i in range(1, 6):
  marks = float(input(f"Enter marks for subject {i} (out of 100): "))
  total_marks += marks

percentage = (total_marks / max_possible) * 100

if percentage >= 90:
  grade = "A+"
elif percentage >= 80:
  grade = "A"
elif percentage >= 70:
  grade = "B"
elif percentage >= 60:
  grade = "C"
elif percentage >= 50:
  grade = "D"
else:
  grade = "F"

result= "Pass" if percentage >= 50 else "Fail"

print(f"\nTotal Marks: {total_marks} / {max_possible}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"result: {result}")