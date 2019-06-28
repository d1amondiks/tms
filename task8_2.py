class Student:  # схема класса
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks
        self.full_name = name + ' ' + surname

    def _check_subject(self, subject):
        if subject is None:
            return subject
        elif self.marks.get(subject) is not None:
            return subject
        else:
            return ValueError

    def get_average_mark(self, subject=None):
        num_mark = 0
        sum_mark = 0
        check_subject = self._check_subject(subject)
        if check_subject is None:
            for mark in self.marks.values():
                for mark_i in mark:
                    num_mark += 1
                    sum_mark += mark_i
            average_mark = float(sum_mark)/num_mark
            print ('_av_mark=' + str(average_mark))
            return average_mark
        else:
            for mark in self.marks[subject]:
                num_mark += 1
                sum_mark += mark
            average_mark = float(sum_mark)/num_mark
            print ('_av_mark=' + str(average_mark))
            return average_mark

    @property
    def subjects(self):
        subject_list = []
        for subject in self.marks.keys():
            subject_list.append(subject)
        print subject_list

    def change_mark(self, subject, position, value):
        check_subject = self._check_subject(subject)
        if check_subject is None:
            print 'Nothing to change'
        else:
            self.marks[subject][position] = value
            print self.marks[subject][position]

    @staticmethod
    def compare_students(student1, student2, subject=None):
        av_mark_st1 = student1.get_average_mark(subject)
        av_mark_st2 = student2.get_average_mark(subject)
        if av_mark_st1 > av_mark_st2:
            print 1
        elif av_mark_st1 < av_mark_st2:
            print 2
        else:
            print 0


Petrov = Student('Petya', 'Petrov',
                 {'Math': [6, 7, 8, 9],
                  'Fiz': [4, 9, 5, 6, 7], 'Biol': [4, 5, 3, 6, 5]})
Ivanov = Student('Ivan', 'Ivanov',
                 {'Math': [8, 8, 10], 'Fiz': [8, 9, 9, 6], 'Biol': [9, 6, 9]})
