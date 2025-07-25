def all(*numbers):
    print("All numbers:", numbers
          )
    sum = 0
    for number in numbers:
        print("Adding:", number)
        sum += number
        return sum, number
    return sum
total = all(1, 2, 3, 4, 5)
print("Total:", total)