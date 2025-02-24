from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm, CreateRecordForm, UpdateRecordForm

from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Record

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Home 
def home(request):
    return render(request, 'webapp/index.html')

# Register a user
def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User registered successfully 👏🥳")
            return redirect("userlogin")
    
    context = {'form': form}
    return render(request, 'webapp/register.html', context = context)

# Login a user
def userlogin(request):
    
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)  
            if user is not None:
                auth.login(request, user)
                return redirect("")
            else:
                messages.error(request, "Invalid username or password 😢")
    
    context = {'form': form}
    return render(request, 'webapp/login.html', context)


# Logout a user
def logout(request):
    auth.logout(request)
    messages.success(request, "Logged Out!")
    return redirect('userlogin')

# Dashboard
@login_required(login_url='userlogin')
def dashboard(request):
    my_records = Record.objects.all()
    context = {'records': my_records}
    return render(request, 'webapp/dashboard.html', context=context)

# Add a record
@login_required(login_url='userlogin')
def create_record(request):
    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record creation successfull 👏🥳")
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'webapp/create-record.html', context=context)

# Update a record
@login_required(login_url='userlogin')
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfull 👏🥳")
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'webapp/update-record.html', context=context) 

# View a record
@login_required(login_url='userlogin')
def view_record(request, pk):
    record = Record.objects.get(id=pk)
    context = {'record': record}
    return render(request, 'webapp/view-record.html', context=context)

# Delete a record
@login_required(login_url='userlogin')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request, "Record deletion successfull 👏🥳")
    return redirect('dashboard')

# Chatbot
@csrf_exempt
def chatbot(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "").strip()

        # Check if user is authenticated
        if not request.user.is_authenticated:
            return JsonResponse({"reply": "You need to log in first.", "redirect": "/userlogin/"})

        # Process the user input
        if user_message == "1":
            return JsonResponse({"reply": "Redirecting to Dashboard...", "redirect": "/dashboard/"})
        elif user_message == "2":
            return JsonResponse({"reply": "Redirecting to Add Record page...", "redirect": "/create_record/"})
        elif user_message == "3":
            return JsonResponse({"reply": "Type the name or email of the record you want to search."})
        elif user_message == "4":
            logout(request)
            return JsonResponse({"reply": "You have been logged out.", "redirect": "/userlogin/"})

        search_results = Record.objects.filter(first_name__icontains=user_message) | Record.objects.filter(last_name__icontains=user_message)
        print(search_results)
        # Convert QuerySet to JSON serializable format
        records_list = [
            {
                "id": r.id,
                "first_name": r.first_name,
                "last_name": r.last_name,
                "email": r.email,
                "phone": r.phone,
                "address": r.address,
                "city": r.city,
                "state": r.state,
                "country": r.country,
                "created_at": r.created_at.strftime("%Y-%m-%d %H:%M:%S"),  # Convert datetime to string
            }
            for r in search_results
        ]

        print(records_list)
        # Store search results in session
        request.session["search_results"] = records_list

        # Redirect to dashboard with search results
        return JsonResponse({"reply": "Displaying matching records in the dashboard...", "redirect": "/dashboard/?search=1"})

    return JsonResponse({"reply": "Invalid request."})