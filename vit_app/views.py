from django.shortcuts import render, HttpResponse

# Create your views here.
def login(request):
    if request.method == 'POST':
        Fname = request.POST.get('firstName')
    #    Lname =  request.POST.get('lastName')
    #     password = request.POST.get('password')
    #     designation = request.POST.get('designation')
    #     posting = request.POST.get('posting')
    #     postHeld = request.POST.get('postHeld')
    #     reportingOfficer = request.POST.get('reportingOfficer')
    #     event = request.POST.get('event')
    #     theme = request.POST.get('Theme')
    #     title = request.POST.get('title')
    #     email = request.POST.get('email')
    #     streetAddress = request.POST.get('streetAddress')
    #     streetAddress2 = request.POST.get('streetAddress2')
    #    city = request.POST.get('city')
    #    street = request.POST.get('street')
    #    postal = request.POST.get('Postal')
        register_forms = register_form(Fname = firstName)
        register_forms.save()
        message.success("data saved")
    
    return render(request,'login.html')




def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')