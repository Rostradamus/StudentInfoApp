from django.db import models
from django.utils import timezone

# Create your models here.

YEAR_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
)
TEST_COURSE = (
    ('cpsc', 'Computer Science'),
    ('phys', 'Physics'),
)


class Info(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=1, choices=YEAR_CHOICES, default='1')
    major = models.CharField(max_length=50, choices=TEST_COURSE, default='cpsc')
    available_date = models.DateField(default=timezone.now)
    tutor_course = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return "Date: " + str(self.created_date.date()) + " " + self.name + " Year:" + str(self.year)


