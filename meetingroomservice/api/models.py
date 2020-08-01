from django.db import models



class Room(models.Model):
    Name = models.CharField(max_length=100)
    Capacity = models.IntegerField(default=0)

    def __str__(self):
        return self.Name


class BookingHistory(models.Model):
    Room = models.ForeignKey(Room,on_delete=models.CASCADE)
    StartDate = models.DateTimeField()
    EndDate = models.DateTimeField()
    NumberOfPeople = models.IntegerField()

    def __str__(self):
        return self.Room.Name + str(self.StartDate) + " " + str(self.EndDate)
    
    class Meta:
        verbose_name_plural = "Booking History"

