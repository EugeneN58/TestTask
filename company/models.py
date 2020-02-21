from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    birthday = models.DateField(verbose_name='Дата рождения')
    email = models.EmailField('e-mail')
    phone = models.CharField(max_length=11, verbose_name='Телефон')
    start_work_date = models.DateField(verbose_name='Дата начала работы')
    end_work_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания работы')
    post = models.CharField(max_length=30, verbose_name='Должность')
    department = models.ForeignKey('Department', on_delete=models.CASCADE, verbose_name='Отдел')

    def __str__(self):
        return f'{self.last_name} {self.name} {self.patronymic}'

class Department(models.Model):
    department_tittle = models.CharField(max_length=50)

    def __str__(self):
        return self.department_tittle