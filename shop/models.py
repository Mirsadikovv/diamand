from django.db import models


# class User(models.Model):
#     name = models.CharField(max_length=30,blank=False)
#     second_name = models.CharField(max_length=30,blank=False)


#     def __str__(self):
#         return f"{self.second_name} {self.name}"

# class Tovar(models.Model):
#     name = models.CharField(max_length=25,blank=False)
#     second_name = models.CharField(max_length =30,blank = False)    
#     costs = models.IntegerField(default = 0)
#     definition = models.CharField(max_length=70,blank=False)

#     def __str__(self):
#         return f"{self.second_name} {self.name}"
    
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    phone = models.IntegerField()

    def __str__(self):
        return f"{self.name},{self.id}"

class Tovar(models.Model):
    name    = models.CharField(max_length=25)
    amount  = models.IntegerField(default=0)
    cost    = models.IntegerField(default=0)
    made_by = models.CharField(max_length=20)
    description = models.CharField(max_length = 60)

    def __str__(self):
        return f"{self.name},{self.id}"

