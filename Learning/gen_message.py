names = input("Enter names: ").title().split(",")
assignments = input("Enter missing assignments: ").split(",")
grades = input("Enter grades: ").split(",")

for i in range(len(names)):
    message = f"Hi {names[i]},\n\nThis is a reminder that you have {assignments[i]} assignments left to \
submit before you can graduate. Your current grade is {grades[i]} and can increase \
to {grades[i] + 2*assignments[i]} if you submit all assignments before the due date.\n\n"
    print(message)