from django.db import models

# CREATE TABLE `location` (
#   `location_id` int NOT NULL AUTO_INCREMENT,
#   `latitude` decimal(8,6) NOT NULL,
#   `longitude` decimal(8,6) NOT NULL,
#   `address` varchar(120)  DEFAULT NULL,
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

# CREATE TABLE `owner` (
#   `owner_id` int NOT NULL AUTO_INCREMENT,
#   `name` varchar(30)  NOT NULL,
#   `phone` varchar(15)  DEFAULT NULL,
#   `email` varchar(50)  DEFAULT NULL,
#   `photo` varchar(100)  DEFAULT NULL,
#   PRIMARY KEY (`owner_id`)
# ) 

class Owner(models.Model):
    owner_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    def upload_photo(self, filename):
        path = "tradefair/owner_img/{}".format(filename)
        return path

    photo = models.ImageField(upload_to=upload_photo, null=True, blank=True)

    def __str__(self):
        return f"{self.owner_id} - {self.name}"

# CREATE TABLE `store` (
#   `store_id` int NOT NULL AUTO_INCREMENT,
#   `name` varchar(130) NOT NULL,
#   `image_url` varchar(100) DEFAULT NULL,
#   `location_id` int NOT NULL,
#   `category` varchar(50) DEFAULT NULL,
#   `description` text,
#   `votes_count` int DEFAULT NULL,
#   `rating` int DEFAULT NULL,
#   `owner_id` int NOT NULL,
#   PRIMARY KEY (`store_id`),
#   KEY `fkStoreLocation` (`location_id`),
#   KEY `fkStoreOwner` (`owner_id`),
#   CONSTRAINT `fkStoreLocation` FOREIGN KEY (`location_id`) REFERENCES `location` (`location_id`),
#   CONSTRAINT `fkStoreOwner` FOREIGN KEY (`owner_id`) REFERENCES `owner` (`owner_id`)
# ) 


class Store(models.Model):
    store_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=130)
    location = models.ForeignKey(Location, on_delete=models.CASCADE) #_id is added by default which makes it location_id
    category = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    vote_count = models.IntegerField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE) #_id is added by default which makes it owner_id

    def upload_img(self, filename):
        path = "tradefair/store_img/{}".format(filename)
        return path

    image_url = models.ImageField(upload_to=upload_img, null=True, blank=True) ###

    def __str__(self):
        return f'id: {self.store_id} | name: {self.name} | loc_id : {self.location_id} | owner_id: {self.owner_id}'