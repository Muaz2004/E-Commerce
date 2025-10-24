from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bids(models.Model):
    placed_bid=models.FloatField(default=0)
    bider=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name="bider")
   

    def __str__(self):
        return f"{self.placed_bid}"

class Catagory(models.Model):
    name=models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class listing(models.Model):
    title=models.CharField(max_length=64)
    description=models.CharField(max_length=500)
    starting_bid=models.ForeignKey(Bids,on_delete=models.CASCADE,null=True,blank=True,related_name="bided_listings")
    creator=models.ForeignKey(User,on_delete=models.CASCADE,related_name="creators_listing",default=1)
    image_url=models.URLField(null=True,blank=True)
    is_active=models.BooleanField(default=True)
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE,null=True,blank=True,related_name="catagory")
    watchlist=models.ManyToManyField(User,null=True,blank=True,related_name="watchlists")



    def __str__(self):
        return f"all listings:{self.id}:{self.title} "
    


class Comment(models.Model):
    comment=models.CharField(max_length=250)
    commentator=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name="comentator")
    commented_listing=models.ForeignKey(listing,on_delete=models.CASCADE,null=True,blank=True,related_name="commented_listings")

    def __str__(self):
        return f"{self.commentator} comment on {self.commented_listing}"
    

    