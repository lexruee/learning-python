#!/usr/bin/env python3

class Person:
    
    def __init__(self, first_name, last_name, job):
        self._first_name = first_name
        self._last_name = last_name
        self._job = job


    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def job(self):
        return self._job
    
    @job.setter
    def job(self, value):
        self._job = value

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.job}"


    def __repr__(self):
        return f"<Person({str(self)})>"


    def as_tuple(self):
        return tuple(str(self).split(', '))

    def as_list(self):
        return list(str(self).split(', '))


class Student(Person):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def as_list(self):
        as_list = super().as_list()
        return ['Student'] + as_list 

    def as_tuple(self):
        as_list = self.as_list()
        return tuple(['Student'] + as_list)



p = Student('Hans', 'Peter', 'Code Monkey')
print(p)
print(repr(p))

print(p.first_name)
print(p.last_name)
print(p.job)

p.job = 'Student'
print(p.job)

print(p.as_tuple())
print(p.as_list())
