def main():
    name_of_exam = input("Enter the name of the exam: ")
    total_marks = int(input("Enter the total marks for the exam: "))
    marks_obtained = int(input("Enter the marks obtained: "))
    percentage = marks_obtained / total_marks * 100

    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    elif percentage >= 50:
        grade = 'E'
    else:
        grade = 'F'

    print(f"{name_of_exam} Grade Calculator")
    print(f"Total marks: {total_marks}")
    print(f"You got {percentage}% which is a {grade}.")


if __name__ == '__main__':
    main()
