from django.db import models
from django.contrib.auth.models import User

from posts.models import Post



class BorrowingDataModel(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    book_name = models.CharField(max_length=100)
    book_price = models.DecimalField( decimal_places=1, max_digits=10)
    balance = models.DecimalField(max_digits=10, decimal_places=1,)
    user = models.ForeignKey(User, related_name = 'borrowing_data' , on_delete= models.CASCADE)
    post = models.ForeignKey(Post, related_name = 'borrowing_data' , on_delete= models.CASCADE,  blank=True, null=True)
    
    
    
class UserAccount(models.Model):
    balance = models.DecimalField(max_digits=10, decimal_places=1)
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name = 'user_account',  blank=True, null=True, )