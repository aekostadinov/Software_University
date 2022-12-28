"""Write a function students_credits which receives a different number of strings.
Each string will be in the format: "{course name}-{credits}-{max test points}-{diyan's points}".
Your task is to calculate the credits Diyan manages to get from all courses. The credits he gets are proportional to
his points on the test. For example, if the credits of a course are 25, and Diyan achieved to get 50 of 100 max test
points, he will get 12.5 credits for the course.Also, you need to keep track of each course and Diyan's credits and
sort them in descending order by Diyan's credits.Finally, return a string on multiple lines containing:
    -Diyan's achievement message:
        oIf the sum of all of Diyan's credits is more than or equal to 240, return:
"Diyan gets a diploma with {total credits} credits."
        oOtherwise, return: "Diyan needs {credits needed} credits more for a diploma."
    -Information for each course and Diyan's credits:
        o"{course name} - {diyan's credits}"
        oNote: Each course data should be on a new line.
    -All credits must be formatted to the first decimal place.

Note: Submit only the function in the judge system

Input
    -There will be no input, just any number of strings with courses data passed to your function
Output
    -The function should return a string in the format described above:"""


def students_credits(*args):
    course_track = {}
    credits = 0
    result = ''
    for str in args:
        course_name, max_credits, max_test_points, student_points = [float(el) if el.isdigit() else el for el in str.split("-")]
        credits_get = max_credits * (student_points / max_test_points)
        credits += credits_get
        course_track[course_name] = credits_get
    sorted_courses = dict(sorted(course_track.items(), key=lambda x: -x[1]))
    if credits >= 240:
        result += f"Diyan gets a diploma with {credits:.1f} credits." + "\n"
    else:
        credits_needed = 240 - credits
        result += f"Diyan needs {credits_needed:.1f} credits more for a diploma." + "\n"
    for name, credit in sorted_courses.items():
        result += f"{name} - {credit:.1f}" + "\n"
    return result

# print(
#     students_credits(
#             "Discrete Maths-40-500-450",
#             "AI Development-20-400-400",
#             "Algorithms Advanced-50-700-630",
#             "Python Development-15-200-200",
#             "JavaScript Development-12-500-480",
#             "C++ Development-30-500-405",
#             "Game Engine Development-70-100-70",
#             "Mobile Development-25-250-225",
#             "QA-20-300-300",
#     )
# )
