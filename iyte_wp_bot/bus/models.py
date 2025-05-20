from django.db import models

WEEKEND_DAYS = (
    ('Weekday', 'Hafta İçi'),
    ('Saturday', 'Cumartesi'),
    ('Sunday', 'Pazar'),
)

class Bus(models.Model):
    number = models.CharField(max_length=10, unique=True, verbose_name="Bus Number")
    def __str__(self):
        return f"Bus {self.number}"

class Trip(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name="trips")
    trip_day = models.CharField(max_length=9, choices=WEEKEND_DAYS, verbose_name="Trip Day")
    is_start_from_iyte = models.BooleanField(default=False, verbose_name="Starts from IYTE")
    departure_station = models.CharField(max_length=100, verbose_name="Departure Station")
    arrival_station = models.CharField(max_length=100, verbose_name="Arrival Station")
    departure_time = models.TimeField()

    def __str__(self):
        return (f"{self.bus.number}: {self.departure_station} ➔ {self.arrival_station} "
                f"({self.departure_time})")
