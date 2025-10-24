from django.shortcuts import render
from .models import *
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def index(request):
    catagory=Catagory.objects.all()
    query=listing.objects.filter(is_active=True)
    return render(request,"auctions/index.html",{
        "query":query,"catagory":catagory
        })

def add(request):
    catagory=Catagory.objects.all()
    if not request.user.is_authenticated:
        return render(request,"auctions/login.html",{
            "message":"you are not Eligable"
        })
    elif request.user.is_authenticated and request.method=="POST":
        Title=request.POST.get("title")
        Creator=request.user
        Description=request.POST.get("description")
        Starting_bid=request.POST.get("starting_bid")
        Image_url=request.POST.get("image_url")
        catname=request.POST.get("cat")
        cat=Catagory.objects.get(name=catname)
        user=request.user
        bid=Bids(placed_bid=float(Starting_bid),bider=user)
        bid.save()

        listing.objects.create(title=Title,description=Description,starting_bid=bid,image_url=Image_url,catagory=cat,creator=Creator)
        return HttpResponseRedirect(reverse('index'))
    
    return render(request,"auctions/add.html",{"catagory":catagory})

def display(request,list_id):
    query=listing.objects.get(pk=list_id)
    user=request.user
    com=Comment.objects.filter(commented_listing=query)
    flag=request.user in query.watchlist.all()
    isowner=request.user.username==query.creator.username
    return render(request,"auctions/listings.html",{
        "query":query,"flag":flag,"list_id":list_id,"comment":com,"isowner":isowner,"user":user
    })
def cat_display(request):
    if request.method=='POST':
        cat=request.POST.get("catagory")
        allcat=Catagory.objects.get(name=cat)
        catagory=Catagory.objects.all()
        query=listing.objects.filter(catagory=allcat)
        return render(request,"auctions/index.html",{
        "query":query,"catagory":catagory
        })
    else:
        return render(request, 'auctions/index.html', {'message': 'NO Listing found'})
    

def wat_display(request):
    user=request.user
    watchlist=user.watchlists.all()
    return render(request,"auctions/watchlist.html",{"query":watchlist})
    


def remove(request,list_id):
    if request.method=="POST":
        removed=listing.objects.get(pk=list_id)
        user=request.user
        removed.watchlist.remove(user)
    return HttpResponseRedirect(reverse(display,args=[list_id]))


def add_to_watchlist(request,list_id):
    if request.method=="POST":
        data=listing.objects.get(pk=list_id)
        user=request.user
        data.watchlist.add(user)
    return HttpResponseRedirect(reverse(display,args=[list_id]))

def add_comment(request,list_id):
    if request.method=="POST":
        com=request.POST.get("comment")
        user=request.user
        com_listing=listing.objects.get(pk=list_id)
        newcomment=Comment(comment=com,commentator=user,commented_listing=com_listing)
        newcomment.save()
        return HttpResponseRedirect(reverse(display,args=[list_id]))
    return render("auction/listings.html")


def place_bid(request, list_id):
    query = listing.objects.get(pk=list_id)
    user = request.user
    newbid = float(request.POST.get("bid"))
    com = Comment.objects.filter(commented_listing=query)
    flag = request.user in query.watchlist.all()
    isowner=request.user.username==query.creator.username
    
    # Check if the new bid is higher than the current bid
    if newbid > query.starting_bid.placed_bid:
        # Create and save a new bid
        updated = Bids(placed_bid=newbid, bider=user)
        updated.save()
        
        # Update the listing's starting_bid to reference the new bid
        query.starting_bid = updated
        query.save()
        
        return render(request, "auctions/listings.html", {
            "query": query, 
            "list_id": list_id, 
            "message": "Bid updated successfully.", 
            "updated": True, 
            "flag": flag, 
            "comment": com,
            "isowner":isowner
        })
    else:
        return render(request, "auctions/listings.html", {
            "query": query, 
            "list_id": list_id, 
            "message": "Bid not updated. Please enter a higher bid.", 
            "updated": False, 
            "flag": flag, 
            "comment": com,
            "isowner":isowner
        })


def close_bid(request, list_id):
    query = listing.objects.get(pk=list_id)
    query.is_active = False  # Close the auction
    query.save()

    # Get the highest bid and check if the current user is the winning bidder
    winning_bid = query.starting_bid.bider  # This should be the highest bidder
    com = Comment.objects.filter(commented_listing=query)
    isowner = request.user.username == query.creator.username
    flag = request.user in query.watchlist.all()

    return render(request, "auctions/listings.html", {
        "query": query,
        "list_id": list_id,
        "message": "congra the bid has closed.",
        "updated": True,
        "comment": com,
        "isowner": isowner,
        "flag": flag,
        "winning_bidder": winning_bid  # Pass the winning bidder to the template
    })



    


    
    





from django.contrib import messages  # import messages at the top

def login_request(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")  # success message
            return HttpResponseRedirect(reverse('index'))  # redirect to index
        else:
            messages.error(request, "Invalid username or password. Please try again.")  # error message
            return render(request, "auctions/login.html")
    
    return render(request, "auctions/login.html")

def logout_request(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")  # logout message
    return HttpResponseRedirect(reverse('login'))  # redirect to login page


