import tutorial01 as A1

actual_answers = [9, 12, 80, 5, 81, [2, 6, 18, 54, 162], [5, 7, 9, 11, 13, 15],[0.2, 0.143, 0.111, 0.091, 0.077, 0.067]]
student_answers = []

test_case_1 = A1.add(4, 5)
student_answers.append(test_case_1)

test_case_2 = A1.subtract(14, 2)
student_answers.append(test_case_2)


test_case_3 = A1.multiply(10, 8)
student_answers.append(test_case_3)

test_case_4 = A1.divide(10, 2)
student_answers.append(test_case_4)

test_case_5 = A1.power(3, 4)
student_answers.append(test_case_5)
# Driver code

a = 2  # starting number
r = 3  # Common ratio
n = 5  # N th term to be find

gp = A1.printGP(a, r, n)
gp = list(gp)
student_answers.append(gp)

a = 5  # starting number
d = 2  # difference
n = 6  # Nth term to be find

ap = A1.printAP(a,d,n)
student_answers.append(list(ap))

hp = A1.printHP(a,d,n)
student_answers.append(list(hp))

print(gp)
print(actual_answers)
print(student_answers)

total_test_cases = len(actual_answers)
count_of_correct_test_cases = 0

for x, y in zip(actual_answers, student_answers):
    if x == y:
        count_of_correct_test_cases += 1

print(
    f"Test Cases Passed = '{count_of_correct_test_cases}'  / '{total_test_cases}'")
