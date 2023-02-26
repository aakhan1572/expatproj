import json
from .forms import ExpatadForm,ContactmeForm,InterestedForm
from django.shortcuts import render, redirect,get_object_or_404,redirect,HttpResponseRedirect
from .models import Expatad, Category,ExpatImage,Contactme,Interested,Purpose #ReviewRating, ProductGallery
from django.contrib.auth.models import User
from main.filters import Expatadfilter

from django.db.models import Q


from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.contrib import messages

from accounts.utils import send_mail


from main.filters import Expatadfilter
def expads(request, slug=None):
    categories = None
    expatads = None
    if slug != None:
        categories = get_object_or_404(Category, slug=slug)
        #print(categories)
        #expatads = Expatad.objects.filter(category=categories, is_active=True)
        expatad_filter = Expatadfilter(request.GET, queryset=Expatad.objects.all().filter(category=categories,is_active=True))
        expatads = expatad_filter.qs
        paginator = Paginator(expatads, 5)
        page = request.GET.get('page')
        paged_expatads = paginator.get_page(page)
        expatad_count = expatads.count()
        print(paginator.num_pages)
    else:
        expatad_filter = Expatadfilter(request.GET, queryset=Expatad.objects.all().filter(is_active=True))
        expatads = expatad_filter.qs
        paginator = Paginator(expatads, 5)
        page = request.GET.get('page')
        paged_expatads = paginator.get_page(page)
        expatad_count = expatads.count()
        print(paginator.count)

    context = {
        'expatads': paged_expatads,
        'expatad_count': expatad_count,
        'form' : expatad_filter.form,
        'expatads_list': expatad_filter.qs,
    }
    return render(request, 'home.html', context)

def expataddetail(request,id):
    expatads = get_object_or_404(Expatad,id=id) 
    expatImage_list =ExpatImage.objects.filter(expatads=expatads).prefetch_related('expatads')
    #ExpatImage.objects.filter(ExpatImage=Expatad)
    #ExpatImage.objects.filter(ExpatImage=Expatad).prefetch_related('vehiclepart_set')
    #expatImage_list = ExpatImage.objects.filter(id=expatads.id)
    #print(expatImage_list.images)
    #print(expatads.id)
    #print(expatads)
    context = {'expatads':expatads,'expatImage_list': expatImage_list}
    return render(request, 'expads/expataddetail.html',context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            expads = Expatad.objects.order_by('-created').filter(Q(Description__icontains=keyword) | Q(fullname__icontains=keyword))
            expad_count = expads.count()
            print("Found")
    context = {
        'expatads': expads,
        'expatad_count': expad_count,
    }
    return render(request, 'home.html', context)


def contactme(request):
    context = {

        }
    return render(request, 'expads/contactme.html', context)

def contactyou(request):
    context = {

        }    
    return render(request, 'expads/contactyou.html', context)

def contactmes(request):
#    obj = get_object_or_404(Contactme, id = id)
    form = ContactmeForm()
    if request.method == 'POST' and request.user.is_authenticated:
        form = ContactmeForm(request.POST)
        email = form.data['email']
        request.POST._mutable = True
        #user = User.objects.get(id=request.data['user']) # that is if you are sending the use Id from the frontend
        form.data['user']=request.user
        #form.data['user_id']
        form.data['is_followed']=False
        if form.is_valid():
            form.save()
            mail_subject = 'We have received your Email'
            email_template = 'accounts/emails/contactusconfirm.html'
            #send_confirm_email(request, contactus, mail_subject, email_template)
            print(Contactme)
            send_mail(mail_subject,'We received Your message Here is acknowledgment Thanks','aakhan1572@gmail.com',[email],fail_silently=False,)
            messages.success(request, 'We have received your message sucessfully!')
            return redirect('contactmes')

    if not request.user.is_authenticated:
        messages.success(request, 'Please login')
        return render(request, 'accounts/login.html')
    context = {'form': form}
    return render(request, 'expads/contactmes.html', context)

def interested(request):
#    print(id)
#    obj = get_object_or_404(Interested)
    form = InterestedForm()
    if request.method == 'POST' and request.user.is_authenticated:
        form = InterestedForm(request.POST)
        email = form.data['email']
        request.POST._mutable = True
        form.data['user']=request.user
        form.data['is_followed']=False
        if form.is_valid():
            form.save()
            mail_subject = 'We have received your Email'
            email_template = 'accounts/emails/contactusconfirm.html'
            send_mail(mail_subject,'We received Your message Here is acknowledgment Thanks','aakhan1572@gmail.com',[email],fail_silently=False,)
            messages.success(request, 'We have received your message sucessfully!')
            return redirect('interested')

    if not request.user.is_authenticated:
        messages.success(request, 'Please login')
        return render(request, 'accounts/login.html')
    context = {'form': form}
    print(form)
    return render(request, 'expads/interested.html', context)


def addads(request):
    form=ExpatadForm()
    if request.method == "POST":
        form= ExpatadForm(request.POST,request.FILES,initial={'user':request.user,'is_active':True,'cover_photo':request.FILES['cover_photo']})
        images_list = request.FILES.getlist('images')
        request.POST._mutable = True
        form.data['user']=request.user
        form.data['is_active']=True
        if form.is_valid():
            newform=form.save()
            expatad = Expatad.objects.get(id=newform.id)
            for image in images_list:
                Expatad_images = ExpatImage.objects.create(
                    expatads= expatad,
                    images = image
                )
            messages.success(request, 'Your Ad added successfully.')
            return redirect('home')
        else:
            print(form.errors)
            return HttpResponse('Form Not Valid')
    else:
        form = ExpatadForm()

    context = {'form':form}
    return render(request, 'expads/addads.html',context)



""" def home(request):
    expatad_filter = Expatadfilter(request.GET, queryset=Expatad.objects.all().filter(is_active=True))
    context = {
        'form' : expatad_filter.form,
        'expatads': expatad_filter.qs
    } 
    print(context)
    return render(request, 'home.html', context)

ef expads(request, slug=None):
    categories = None
    expatads = None

    if slug != None:
        categories = get_object_or_404(Category, slug=slug)
        print(categories)
        expatads = Expatad.objects.filter(category=categories, is_active=True)
        paginator = Paginator(expatads, 3)
        page = request.GET.get('page')
        paged_expatads = paginator.get_page(page)
        expatad_count = expatads.count()
    else:
        expatads = Expatad.objects.all().filter(is_active=True).order_by('id')
        paginator = Paginator(expatads, 3)
        page = request.GET.get('page')
        paged_expatads = paginator.get_page(page)
        expatad_count = expatads.count()

    context = {
        'expatads': paged_expatads,
        'expatad_count': expatad_count,
    }
    return render(request, 'home.html', context)

 def addads(request):
    form=ExpatadForm()
    if request.method == "POST":
        form= ExpatadForm(request.POST or None, request.FILES or None)
        images_list = request.FILES.getlist('images')
        request.POST._mutable = True
        form.data['user']=request.user
        form.data['is_active']=True
        print(form)
        if form.is_valid():
            user = form.cleaned_data['user']
            is_active = form.cleaned_data['is_active']
            category = form.cleaned_data['category']
            fullname = form.cleaned_data['fullname']
            countrycode = form.cleaned_data['countrycode']
            purpose = form.cleaned_data['purpose']
            citycode = form.cleaned_data['citycode']
            locationcode = form.cleaned_data['locationcode']
            landmark = form.cleaned_data['landmark']
            area = form.cleaned_data['area']
            areameasurement  = form.cleaned_data['areameasurement']
            contactno = form.cleaned_data['contactno']
            zipcode = form.cleaned_data['zipcode']
            price = form.cleaned_data['price']
            Description = form.cleaned_data['Description']
            cover_photo = form.cleaned_data['cover_photo']

            expatad_obj = Expatad.objects.create(user=user,category=category,fullname=fullname,countrycode=countrycode,purpose=purpose,citycode=citycode,
            locationcode=locationcode,landmark=landmark,area=area,areameasurement=areameasurement,contactno=contactno,zipcode=zipcode,price=price,
            Description=Description,is_active=is_active,cover_photo=cover_photo)
            print(images_list)
            for i in images_list:
                ExpatImage.objects.create(expatads=expatad_obj,images=i)
            messages.success(request, 'Your Ad added successfully.')
            return redirect('home')
        else:
            print(form.errors)
            return HttpResponse('Form Not Valid')
    else:
        form = ExpatadForm()

    context = {'form':form}
    return render(request, 'expads/addads.html',context)
 """