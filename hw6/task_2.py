import datetime
from collections import defaultdict


class DeadlineError(Exception):
    """Raised in case of the late hw submission"""
    pass


class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.datetime.now()

    def is_active(self):
        return datetime.datetime.now() < (self.created + self.deadline)


class HomeworkResult:
    def __init__(self, author, homework: Homework, solution: str):
        if isinstance(homework, Homework):
            self.homework = homework
        else:
            raise TypeError('Given object is NOT a "Homework" object')
        self.solution = solution
        self.author = author
        self.created = datetime.datetime.now()


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Student(Person):
    def do_homework(self, homework: Homework, solution: str):
        if homework.is_active():
            hw_done = HomeworkResult(self, homework, solution)
            return hw_done
        else:
            raise DeadlineError("You are late.")


class Teacher(Person):
    homework_done = defaultdict(str)

    @staticmethod
    def create_homework(text, deadline):
        return Homework(text, deadline)

    @classmethod
    def check_homework(cls, hw_result: HomeworkResult):
        if len(hw_result.solution) > 5 and hw_result.solution not in cls.homework_done.values():
            cls.homework_done[hw_result.homework, hw_result.author] = hw_result.solution
            return True
        else:
            return False

    @classmethod
    def reset_results(cls, hw=None):
        if isinstance(hw, Homework):
            to_pop_list = []  # have to store keys for elements I want to pop from our dict because I can't pop them
            # during cycle, because it's now allowed to change dictionary's size
            for key, value in cls.homework_done.items():
                if key[0] == hw:
                    to_pop_list.append(key)
            for i in to_pop_list:
                cls.homework_done.pop(i)

        elif hw is None:
            cls.homework_done.clear()
        else:
            raise TypeError('this method takes only a "Homework" object as an argument')
