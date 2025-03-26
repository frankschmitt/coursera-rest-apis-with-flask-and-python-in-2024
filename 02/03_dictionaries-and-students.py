# Create a variable called student with a dictionary.
# Must contain three keys: name, school and grades
# Values should be Jose, Computing and a tuple with values 66, 77 and 88
student = { 'name': 'Jose', 'school': 'Computing', 'grades': (66, 77, 88) }


# Assume the target (data) is a dictionary
# Modify the grades variable so it accesses the 'grades' key of the data dictionary
def average_grade(data):
    grades = data['grades'] #change this
    return sum(grades) / len(grades)


# implement the function below
# Given a list of students (dictionaries), calculate the average grade of the class
# You must add all grades of all students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    # nested list comprehension, see https://stackoverflow.com/a/952952/610979
    all_grades = [ g for student in student_list for g in student['grades'] ]
    return sum(all_grades) / len(all_grades)


if __name__ == '__main__':
    jose = { 'name': 'Jose', 'school': 'Computing', 'grades': (66, 77, 88) }
    valim = { 'name': 'Valim', 'school': 'Elixir', 'grades': (99, 110, 121) }
    print(f"jose: {average_grade(jose)}")
    student_list = [jose, valim ]
                    
    print(f"input: {student_list}, avg: {average_grade_all_students(student_list)}")
