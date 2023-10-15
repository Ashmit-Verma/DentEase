from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})   