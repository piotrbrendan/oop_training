import abc
import uuid
from collections import defaultdict



class IntroToPython:

    def lesson(self):
        return f""" Hello {self.student}. define two variables,
               an integer named a with value 1
               and a string named b with value 'hello'"""

    def check(self, code):

        return code == 'a = 1\nb = \'hello\''

class Assignment(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def lesson(self):
        pass

    @abc.abstractmethod
    def check(self,code):
        pass

    @classmethod
    def __subclasshook__(cls,C):
        if cls is Assignment:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True

        return NotImplemented

class Statistics(Assignment):

    def lesson(self):
        return f"""Good work {self.student}. Now calc avg of 1, 5, 18, -3 
                and assign to a variable named 'avg'
                """
    def check(self,code):
        import numpy as np

        global_vars = {}
        local_vars = {}


        code = '\n'.join(['import numpy as np',code])
        exec(code, global_vars, local_vars)

        return local_vars.get('avg') == np.mean([1,5,18,-3])


class Algebra:

    def lesson(self):
        return f"""Hello {self.student}. This is your {self.correct_attempts+1} attempt :)
        """

    def check(self,code):
        return True #default to True

class AssignmentGrader:
    def __init__(self,student,AssignmentClass):
        self.assignment = AssignmentClass()
        self.assignment.student = student

        self.attempts = 0
        self.correct_attempts = 0
        self.assignment.correct_attempts = self.correct_attempts

    def check(self,code):
        self.attempts +=1
        result = self.assignment.check(code)
        if result:
            self.correct_attempts +=1

        return result

    def lesson(self):
        return self.assignment.lesson()


class Grader:
    def __init__(self):
        self.student_graders = {}
        self.assignment_classes = {}
        self.student_graders_all = defaultdict(list)

    def register(self, assignment_class):
        if not issubclass(assignment_class, Assignment):
            raise RuntimeError(
                "Your class does not have the right methods"
            )
        id = uuid.uuid4()
        self.assignment_classes[id] = assignment_class
        return id

    def start_assignment(self, student, id):
        self.student_graders[student] = AssignmentGrader(student, self.assignment_classes[id])
        self.student_graders_all[student].append(self.student_graders[student])

    def get_lesson(self, student):
        assignment = self.student_graders[student]
        return assignment.lesson()

    def check_assignment(self, student, code):
        assignment = self.student_graders[student]
        return assignment.check(code)

    def assignment_summary(self, student):
        grader = self.student_graders[student]
        return f"""
        {student}'s attempts at {grader.assignment.__class__.__name__}:
        attempts: {grader.attempts}
        correct: {grader.correct_attempts}
        passed: {grader.correct_attempts > 0}
           """

    def all_assignment_summary(self, student):
        student_graders_all = self.student_graders_all[student]

        num_courses = len(set(student_graders_all))
        total_attempts = 0
        correct_attempts = 0
        for grader in student_graders_all:
            total_attempts += grader.attempts
            correct_attempts += grader.correct_attempts

        return f"""{student} took {num_courses} made total {total_attempts} 
                of which {correct_attempts}
                were correct"""

#have all assignments done by student in one container