from django.db import models

# CREATE TABLE `location` (
#   `location_id` int NOT NULL AUTO_INCREMENT,
#   `latitude` decimal(8,6) NOT NULL,
#   `longitude` decimal(8,6) NOT NULL,
#   `address` varchar(120) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
#   PRIMARY KEY (`location_id`)
# ) 

# Create your models here.
class Location(models.Model):
    location_id = models.IntegerField(primary_key=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=8, decimal_places=6)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.location_id} - {self.address}"
