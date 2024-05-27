def calculate_average_grade():
    # Prompt the user for their name and store it in the student_name variable
    student_name = input("Hello friend, what is your name?")

    # Prompt the user for their scores in Math, Science, and English
    # Store the scores in the respective variables: math_score, science_score, english_score
    math_score = int(input("what is your most recent math test score?"))
    science_score = int(input("what is your most recent science test score?"))
    english_score = int(input("what is your most recent english test score?"))

    # Calculate the average grade
    average_grade = (math_score + science_score + english_score)/3

    # Return the student's name and their average grade
    return student_name, average_grade

if __name__ == '__main__':
    # Call the calculate_average_grade function
    student_name, average_grade = calculate_average_grade()

    # Print the student's name and their average grade
    print(f"Hi {student_name} your average grade is {average_grade}.")