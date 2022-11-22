from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Person(models.Model):
    last_name = models.TextField(max_length=64)
    first_name = models.TextField(max_length=64)
    courses = models.ManyToManyField('Course', blank = True)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name_plural = 'People'
        ordering = ('last_name', 'first_name')

class Course(models.Model):
    name = models.TextField(max_length=200)
    year = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'year')

class Grade(models.Model):
    person = models.ForeignKey(Person, on_delete = models.CASCADE)
    grade = models.PositiveSmallIntegerField(
        validators= [MinValueValidator(0), MaxValueValidator(100)]
    )
    course = models.ForeignKey(Course, on_delete = models.CASCADE)

    def __str__(self):
        return self.person
