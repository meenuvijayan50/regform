# views.py
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import User
from .models import UserProfile

def register_user(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        password = request.POST['password']
        email = request.POST['email']
        phone = request.POST['phone']

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'registration.html', {'error_message': 'Email already exists'})

        # Save user to PostgreSQL
        new_user = User.objects.create(first_name=first_name, password=password, email=email, phone=phone)

        # Save user profile picture to MongoDB
        profile_picture = request.FILES.get('profile_picture')
        UserProfile.objects.create(user=new_user, profile_picture=profile_picture)

        # return redirect('success_page')  # Redirect to a success page

    return render(request, 'registration.html')

def get_user_details(request, user_id):
    user = User.objects.get(pk=user_id)
    user_profile = UserProfile.objects.get(user=user_id)

    user_data = {
        'first_name': user.first_name,
        'email': user.email,
        'phone': user.phone,
        'profile_picture_url': user_profile.profile_picture.url,
    }

    return JsonResponse(user_data)