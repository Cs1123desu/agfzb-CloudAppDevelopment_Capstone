from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=30)
    
    def __str__(self):
        return "name" + self.name + "," + \
                "description" + self.description + ","




# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    CarMake = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    DealerID = models.IntegerField()
    name = models.CharField(null=False, max_length=30)
    SUV = "SUV"
    SEDAN = "Sedan"
    WAGON = "Wagon"
    TYPE_CHOICES = [
        (SUV, "SUV"),
        (SEDAN, "Sedan"),
        (WAGON, "Wagon")

    ]
    Type = models.CharField(choices=TYPE_CHOICES, max_length=10, default='')
    Year = models.DateField('%Y')


    def __str__(self):
        return "Car Make" + self.CarMake + "," + \
                "Dealer ID" + self.DealerID + +"," + \
                "Name" + self.name + "," + \
                "Type" + self.Type + "," + \
                "Year" + self.Year + ","
            
            


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
