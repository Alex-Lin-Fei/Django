from django.test import TestCase
from .models import Student
# Create your tests here.

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name='Jone',
            sex=1,
            email='jone@qq.com',
            profession='boxer',
            qq='103',
            phone='103'
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='floyd',
            sex=1,
            email='floydd@qq.com',
            profession='actor',
            qq='104',
            phone='104'
        )
        self.assertEqual(student.sex_show, 'male', 'sex content is different')

    def test_filter(self):
        student = Student.objects.create(
            name='floyd',
            sex=1,
            email='floydd@qq.com',
            profession='actor',
            qq='104',
            phone='104'
        )
        name = 'Jone'
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(), 1, 'should have one {}'.format(name))


