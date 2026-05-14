from django.db import models



class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TourCompany(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    services = models.ManyToManyField(Service, blank=True)
    def avg_rating(self):
        reviews = self.reviews.all()
        if reviews:
            return round(sum(i.marks for i in reviews) / reviews.count(), 2)
        else:
            return 0

    def __str__(self):
        return self.name



class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Horse(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Review(models.Model):
    class Marks(models.IntegerChoices):
        ONE = 1, '1'
        TWO = 2, '2'
        THREE = 3, '3'
        FOUR = 4, '4'
        FIVE = 5, '5'

    company = models.ForeignKey('TourCompany', on_delete=models.CASCADE, related_name='reviews')
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    marks = models.IntegerField(choices=Marks.choices, default=Marks.FIVE)
    horse = models.OneToOneField(Horse, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.company} - {self.marks}"



class Booking(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='bookings')
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE, related_name='bookings')
    company = models.ForeignKey(TourCompany, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.person} - {self.horse} - {self.company}"