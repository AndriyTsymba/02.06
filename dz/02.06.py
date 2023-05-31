import logging
class StudentProcessor:
     def __init__(self):
      self.students = []
      self.logger = logging.getLogger()
      self.logger.setLevel(logging.INFO)
      self.logger.addHandler(logging.StreamHandler())
     def add_student(self,student):
       self.students.append(student)
       self.logger.info(f"{student} студент був доданий")
     def remove_student(self,student):
       self.students.remove(student)
       if student in self.students:
        self.logger.info(f"{student} стедент бка повернений ")
       else:
        print("Студент не був знайдений у біза даних")
     def process_students(self,student):
         for student in self.students:
                self.logger.info()