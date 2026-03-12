import sys

sys.argv.pop(0)

numbers = []
for arg in sys.argv:
    if arg.isdigit():
        numbers.append(float(arg))

avg = sum(numbers) / len(numbers)

print(avg)
