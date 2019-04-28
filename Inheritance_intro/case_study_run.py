from Inheritance_intro.case_study_assignments import Grader, \
                                          IntroToPython, \
                                          Statistics, \
                                          Algebra

grader = Grader()

itp_id = grader.register(IntroToPython)
stat_id = grader.register(Statistics)
alg_id = grader.register(Algebra)

grader.start_assignment("Tammy", itp_id)

print("Tammy's Lesson:", grader.get_lesson("Tammy"))
print(
   "Tammy's check:",
   grader.check_assignment("Tammy", "a = 1 ; b = 'hello'"),
)
print(
   "Tammy's other check:",
   grader.check_assignment("Tammy", "a = 1\nb = 'hello'"),
)
print(grader.assignment_summary("Tammy"))
grader.start_assignment("Tammy", stat_id)
print("Tammy's Lesson:", grader.get_lesson("Tammy"))
print("Tammy's check:", grader.check_assignment("Tammy", "avg=5.25"))
print(
   "Tammy's other check:",
   grader.check_assignment(
       "Tammy", "avg = np.mean([1, 5, 18, -3])"
   ),
)
print(grader.assignment_summary("Tammy"))

grader.start_assignment("Tammy", alg_id)
print("Tammy's Lesson:", grader.get_lesson("Tammy"))
print("Tammy's check:", grader.check_assignment("Tammy", "avg=5.25"))
print(
   "Tammy's other check:",
   grader.check_assignment(
       "Tammy", "avg = np.mean([1, 5, 18, -3])"
   ),
)

print(grader.all_assignment_summary('Tammy'))
