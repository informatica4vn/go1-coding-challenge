
def uniqueCourse(data):
  # expected: [{set_of_courses_by_user1}, {set_of_courses_by_user2}]
  list_of_courses = []
  for learner, courses in data.items():
    data[learner] = set(courses)
    list_of_courses.append(data[learner])

    # used SET symmetric_difference() method keeps all items EXCEPT the duplicates.
  unique_courses = list_of_courses[0]
  for course_set in list_of_courses[1:]:
    unique_courses ^= course_set
    return unique_courses 

# test
input = {
  "Learner-0001": [
    "Course-0001",
    "Course-0002",
    "Course-0003"
  ],
  "Learner-0002": [
    "Course-0002",
    "Course-0003",
    "Course-0004"
  ]
}

print(uniqueCourse(input))
