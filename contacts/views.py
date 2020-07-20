from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

def contact(request):
    if request.method=="POST":
        listing_id=request.POST['listing_id']
        listing=request.POST['listing']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        user_id=request.POST['user_id']
        realtor_email=request.POST['realtor_email']

    #Check if the user has already made an enquiry
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted=Contact.objects.all().filter(user_id=user_id,listing_id=listing_id)
            if has_contacted:
                messages.error(request,'You have already made an enquiry')
                return redirect('/listings/'+listing_id)


        contact=Contact(listing_id=listing_id,listing=listing,name=name,email=email,phone=phone,message=message,user_id=user_id)
        contact.save()
        send_mail=(
            'Property Listing Enquiry',
            'There has been an enquiry for'+listing+'.Sign into the admin panel for more details',
            'gsuraj1111@gmail.com',
            realtor_email,
        )

        messages.success(request,'You have successfully made an enquiry')
        return redirect('/listings/'+listing_id)
