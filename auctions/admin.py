from django.contrib import admin
from .models import listing,Catagory,Comment ,Bids


admin.site.register(listing)
admin.site.register(Catagory)
admin.site.register(Comment)
admin.site.register(Bids)
