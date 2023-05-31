import logging

class StudentProcessor:
     def __init__(self):
      self.students = []
      self.logger = logging.getLogger()
      self.logger.setLevel(logging.INFO)
      self.logger.addHandler(logging.StreamHandler())
     def add_student(self,student):
       self.students.append(student)
       self.logger.info(f"{student} Студент був доданий ")
     def remove_student(self,student):
       self.students.remove(student)
       if student in self.students:
        self.logger.info(f"{student} Студент був повернений ")
       else:
        print("Студент не був знайдений у бізі даних ")
     def process_students(self,student):
         for student in self.students:
                self.logger.info()
dima = StudentProcessor()
dima.add_student("Андрій")
kolya = StudentProcessor()
kolya.add_student("Коля")
masha = StudentProcessor()
masha.add_student("Маша")
dima = StudentProcessor()
dima.remove_student("Діма")