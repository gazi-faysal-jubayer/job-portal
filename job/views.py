from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date,datetime
from itertools import chain
import uuid
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail  import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str
from django.contrib.auth import get_user_model
from django_email_verification import send_email

from .utils import *
from .forms import *
from .models import *
from .tokens import *
from .filters import *

# Create your views here.

def index(request):
    d1 = Job.objects.filter(catagory='Design & Creative')
    d2 = Job.objects.filter(catagory='Design & Development')
    d3 = Job.objects.filter(catagory='Sales & Marketing')
    d4 = Job.objects.filter(catagory='Mobile Application')
    d5 = Job.objects.filter(catagory='Construction')
    d6 = Job.objects.filter(catagory='Information Technology')
    d7 = Job.objects.filter(catagory='Real Estate')
    d8 = Job.objects.filter(catagory='Content Writer')
    
    c1 = d1.count()
    c2 = d2.count()
    c3 = d3.count()
    c4 = d4.count()
    c5 = d5.count()
    c6 = d6.count()
    c7 = d7.count()
    c8 = d8.count()
    
    data = {
        'c1':c1,
        'c2':c2,
        'c3':c3,
        'c4':c4,
        'c5':c5,
        'c6':c6,
        'c7':c7,
        'c8':c8,
    }
    return render(request,"index.html",data)

def about(request):
    return render(request,"about.html")

def aboutU(request):
    return render(request,"aboutU.html")

def aboutR(request):
    return render(request,"aboutR.html")

def blog(request):
    text = request.GET.get('text')
    allPosts = Post.objects.all()
    if text:
        allPosts = allPosts.filter(title__icontains=text)
    context = {'allPosts' : allPosts}
    return render(request,"blog.html",context)

def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post' : post}
    return render(request,"blogPost.html",context)

def blogPost_admin(request,slug):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    post = Post.objects.filter(slug=slug).first()
    context = {'post' : post}
    return render(request,"blogPost_admin.html",context)

def blogPost_user(request,slug):
    if not request.user.is_authenticated:
        return redirect("user_login")
    post = Post.objects.filter(slug=slug).first()
    context = {'post' : post}
    return render(request,"blogPost_user.html",context)

def blogPost_rec(request,slug):
    if not request.user.is_authenticated:
        return redirect("recruiter_login")
    post = Post.objects.filter(slug=slug).first()
    context = {'post' : post}
    return render(request,"blogPost_rec.html",context)

def creatBlog(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    error=""
    if request.method =='POST':
        author = request.POST['author']
        title = request.POST['title']
        slug = request.POST['slug']
        tag = request.POST['tag']
        content = request.POST["content"]
        try:
            Post.objects.create(author=author,
                               title=title,
                               slug=slug,
                               tag=tag,
                               content=content,
                               timeStamp=datetime.now())
            error = 'no'
        except:
            error = "yes"
    d = {'error':error}
    return render(request,"creatBlog.html",d)

def creatBlog_rec(request):
    if not request.user.is_authenticated:
        return redirect("recruiter_login")
    error=""
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    fname = recruiter.user.first_name
    lname = recruiter.user.last_name
    if request.method =='POST':
        author = request.POST['author']
        title = request.POST['title']
        slug = request.POST['slug']
        tag = request.POST['tag']
        content = request.POST["content"]
        try:
            Post.objects.create(author=author,
                               title=title,
                               slug=slug,
                               tag=tag,
                               content=content,
                               timeStamp=datetime.now())
            error = 'no'
        except:
            error = "yes"
    d = {
        'error':error,
        'lname':lname,
        'fname':fname,
    }
    return render(request,"creatBlog_rec.html",d)

def admBlog(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    text = request.GET.get('text')
    allPosts = Post.objects.all()
    if text:
        allPosts = allPosts.filter(title__icontains=text)
    context = {'allPosts' : allPosts}
    return render(request,"admBlog.html",context)

def delete_post(request,slug):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    post = Post.objects.filter(slug=slug).first()
    post.delete()
    return redirect('admBlog')

def rec_blog(request):
    if not request.user.is_authenticated:
        return redirect("recruiter_login")
    text = request.GET.get('text')
    allPosts = Post.objects.all()
    if text:
        allPosts = allPosts.filter(title__icontains=text)
    context = {'allPosts' : allPosts}
    return render(request,"rec_blog.html",context)

def user_blog(request):
    if not request.user.is_authenticated:
        return redirect("user_login")
    allPosts = Post.objects.all()
    context = {'allPosts' : allPosts}
    return render(request,"user_blog.html",context)

def admin_login(request):
    error = ""
    if request.method =='POST':
        u = request.POST['email']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
               login(request,user)
               error="no"
            else:
                error="yes"
        except:
            error="yes"
    d ={'error':error}
    return render(request,"admin_login.html",d)

def user_login(request):
    error = ""
    if request.method =='POST':
        u = request.POST['email']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        if user:
            try:
                user1 = Jobseeker.objects.get(user=user)
                if user1.type == "Jobseeker":
                    login(request,user)
                    error="no"
            except:
                error="yes"
        else:
            error="yes"
    d = {'error':error}
    return render(request,"user_login.html",d)

def recruiter_login(request):
    error = ""
    if request.method =='POST':
        u = request.POST['email']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        if user:
            try:
                user1 = Recruiter.objects.get(user=user)
                if user1.type == "Recruiter" and user1.status!="pending":
                    login(request,user)
                    error="no"
                else:
                    error="not"
            except:
                error="yes"
        else:
            error="yes"
    d = {'error':error}
    return render(request,"recruiter_login.html",d)



def user_signup(request):
    messages.success(request, "You are welcome to create a user account.")
    error = ""
    if request.method =='POST':
        f = request.POST['fname']
        l = request.POST['lname']
        e = request.POST['email']
        i = request.FILES['file_nm']
        p = request.POST['password']
        con = request.POST["contactnum"]
        gen = request.POST["gender"]
        try:
            user = User.objects.create_user(
                first_name=f,
                last_name=l,
                username=e,
                password=p,
            )
            Jobseeker.objects.create(
                user=user,
                mobile=con,
                image=i,
                gender=gen,
                type="Jobseeker",
            )
            error = 'no'
            email_success(e,l)
        except:
            error = "yes"
    d = {'error':error}
    return render(request,"user_signup.html",d)

def recruiter_signup(request):
    error = ""
    if request.method =='POST':
        f = request.POST['fname']
        l = request.POST['lname']
        e = request.POST['email']
        i = request.FILES['file_nm']
        p = request.POST['password']
        con = request.POST["contactnum"]
        gen = request.POST["gender"]
        c = request.POST["cname"]
        try:
            user=User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
            Recruiter.objects.create(user=user,mobile=con,image=i,gender=gen,company=c,type="Recruiter",status="pending")
            error = 'no'
            email_success_r1(e,l)
        except:
            error = "yes"
    d = {'error':error}
    return render(request,"recruiter_signup.html",d)

def Logout(request):
    logout(request)
    return redirect('index')

def view_users(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    data = Jobseeker.objects.all()
    d = {'data':data}
    return render(request,"view_users.html",d)

def delete_user(request,pid):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    user = User.objects.get(id=pid)
    e = user.username
    l = user.last_name
    user.delete()
    email_delete(e,l)
    return redirect('view_users')

def recruiter_pending(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    data = Recruiter.objects.filter(status='pending')
    d = {'data':data}
    return render(request,"recruiter_pending.html",d)

def download_resume(request,pid):
    if not request.user.is_authenticated:
        return redirect("recruiter_login")
    apply = Apply.objects.get(id=pid)
    
    if apply and apply.resume:
        resume = apply.resume
        resume_name = resume.name
        response = HttpResponse(resume, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=' + str(resume_name)
        return response
    else:
        # Handle the case when no resume file is found
        return HttpResponse("No resume file available")

def selected(request,pid):
    if not request.user.is_authenticated:
        return redirect("recruiter_login")
    apply = Apply.objects.get(id=pid)
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    uEmail = apply.student.user.username
    com = recruiter.company
    fn = apply.student.user.first_name
    ln = apply.student.user.last_name
    rEmail = recruiter.user.username
    
    if request.method == "POST":
        subject = request.POST['subject']
        intromess = request.POST['intromess']
        mainmess = request.POST['mainmess']
        selectionMail(uEmail,rEmail,subject,intromess,mainmess,fn,ln,com)
    return render(request,'selected.html')

def change_status(request,pid):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    error = ""
    recruiter = Recruiter.objects.get(id=pid)
    e = recruiter.user.username
    l = recruiter.user.last_name
    if request.method == "POST":
        s = request.POST['status']
        recruiter.status = s
        try:
            recruiter.save()
            error = "no"
        except:
            error = "yes"
        if s == 'Accept':
            email_success_r2(e,l)
        elif s == 'Reject':
            email_success_r3(e,l)
    d = {'recruiter':recruiter,'error':error}
    return render(request,'change_status.html',d)

def recruiter_accepted(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    data = Recruiter.objects.filter(status='Accept')
    d = {'data':data}
    return render(request,"recruiter_accepted.html",d)

def recruiter_rejected(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    data = Recruiter.objects.filter(status='Reject')
    d = {'data':data}
    return render(request,"recruiter_rejected.html",d)

def recruiter_all(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    data = Recruiter.objects.all
    d = {'data':data}
    return render(request,"recruiter_all.html",d)

def delete_recruiter(request,pid):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    recruiter = User.objects.get(id=pid)
    e = recruiter.username
    l = recruiter.last_name
    recruiter.delete()
    email_delete_r(e,l)
    return redirect('recruiter_all')

def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    error = ""
    if request.method == "POST":
        o = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            U = User.objects.get(id=request.user.id)
            if U.check_password(o):
                U.set_password(n)
                U.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'change_passwordadmin.html',d)

def change_passworduser(request):
    if not request.user.is_authenticated:
        return redirect("user_login")
    error = ""
    if request.method == "POST":
        o = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            U = User.objects.get(id=request.user.id)
            if U.check_password(o):
                U.set_password(n)
                U.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'change_passworduser.html',d)

def change_passwordrecruiter(request):
    if not request.user.is_authenticated:
        return redirect("recruiter_login")
    error = ""
    if request.method == "POST":
        o = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            U = User.objects.get(id=request.user.id)
            if U.check_password(o):
                U.set_password(n)
                U.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'change_passwordrecruiter.html',d)

def add_job(request):
    if not request.user.is_authenticated:
        return redirect("recruiter_login")
    error=""
    if request.method =='POST':
        jt = request.POST['jobtitle']
        jc = request.POST['jobcatagory']
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        l = request.FILES['logo']
        sal = request.POST['salary']
        loc = request.POST["location"]
        exp = request.POST["experience"]
        skills = request.POST["skills"]
        ds = request.POST["discription"]
        user = request.user
        recruiter = Recruiter.objects.get(user=user)
        try:
            Job.objects.create(recruiter=recruiter,
                               start_date=sd,
                               end_date=ed,
                               title=jt,
                               catagory=jc,
                               salary=sal,
                               image=l,
                               description=ds,
                               experience=exp,
                               locations=loc,
                               skills=skills,
                               creationdate=date.today())
            error = 'no'
        except:
            error = "yes"
    d = {'error':error}
    return render(request,"add_job.html",d)

def job_DesignCreative(request):
    data = Job.objects.filter(catagory='Design & Creative')
    count = data.count()
    d = {'data':data,
         'count':count,}
    return render(request,"job_DesignCreative.html",d)

def job_DesignDevelopment(request):
    data = Job.objects.filter(catagory='Design & Development')
    count = data.count()
    d = {'data':data,
         'count':count,}
    return render(request,"job_DesignDevelopment.html",d)

def job_SalesMarketing(request):
    data = Job.objects.filter(catagory='Sales & Marketing')
    count = data.count()
    d = {'data':data,
         'count':count,}
    return render(request,"job_SalesMarketing.html",d)

def job_Construction(request):
    data = Job.objects.filter(catagory='Construction')
    count = data.count()
    d = {'data':data,
         'count':count,}
    return render(request,"job_Construction.html",d)

def job_InformationTechnology(request):
    data = Job.objects.filter(catagory='Information Technology')
    count = data.count()
    d = {'data':data,
         'count':count,}
    return render(request,"job_InformationTechnology.html",d)

def job_RealEstate(request):
    data = Job.objects.filter(catagory='Real Estate')
    count = data.count()
    d = {'data':data,
         'count':count,}
    return render(request,"job_RealEstate.html",d)

def job_ContentWriter(request):
    data = Job.objects.filter(catagory='Content Writer')
    count = data.count()
    d = {'data':data,
         'count':count,}
    return render(request,"job_ContentWriter.html",d)

def job_MobileApplication(request):
    data = Job.objects.filter(catagory='Mobile Application')
    count = data.count()
    d = {'data':data,
         'count':count,}
    return render(request,"job_MobileApplication.html",d)

def edit_jobdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect("recruiter_login")
    error=""
    job = Job.objects.get(id=pid)
    if request.method =='POST':
        jt = request.POST['jobtitle']
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        sal = request.POST['salary']
        loc = request.POST["location"]
        exp = request.POST["experience"]
        skills = request.POST["skills"]
        ds = request.POST["discription"]
        
        job.title = jt
        job.salary = sal
        job.experience = exp
        job.locations = loc
        job.skills = skills
        job.description = ds
        try:
            job.save()
            error = 'no'
        except:
            error = "yes"
        if sd:
            try:
                job.start_date=sd
                job.save()
            except:
                pass
        else:
            pass
        if ed:
            try:
                job.end_date=ed
                job.save()
            except:
                pass
        else:
            pass
    d = {'error':error,'job':job}
    return render(request,"edit_jobdetail.html",d)

def change_companylogo(request,pid):
    if not request.user.is_authenticated:
        return redirect("recruiter_login")
    error=""
    job = Job.objects.get(id=pid)
    if request.method =='POST':
        cl = request.FILES['logo']
        
        job.image=cl
        try:
            job.save()
            error = 'no'
        except:
            pass
    d = {'error':error,'job':job}
    return render(request,"change_companylogo.html",d)

def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect("recruiter_login")
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    d ={'recruiter':recruiter}
    return render(request,"recruiter_home.html",d)

def edit_rhome(request):
    if not request.user.is_authenticated:
        return redirect("recruiter_login")
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    error = ""
    if request.method =='POST':
        f = request.POST['fname']
        l = request.POST['lname']
        e = request.POST['email']
        con = request.POST["contactnum"]
        gen = request.POST["gender"]
        c = request.POST["cname"]
        
        recruiter.user.first_name = f
        recruiter.user.last_name = l
        recruiter.company = c
        recruiter.user.username = e
        recruiter.mobile = con
        recruiter.gender = gen
        
        try:
            recruiter.save()
            recruiter.user.save()
            error = 'no'
        except:
            error = "yes"
    d ={'recruiter':recruiter,'error':error}
    return render(request,"edit_rhome.html",d)

def edit_rdp(request):
    if not request.user.is_authenticated:
        return redirect("recruiter_login")
    error=""
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    if request.method =='POST':
        cl = request.FILES['logo']
        
        recruiter.image=cl
        try:
            recruiter.save()
            error = 'no'
        except:
            pass
    d = {'error':error,'recruiter':recruiter}
    return render(request,"edit_rdp.html",d) #rdp = recruiter dp

def user_home(request):
    if not request.user.is_authenticated:
        return redirect("user_login")
    user = request.user
    jobseeker = Jobseeker.objects.get(user=user)
    d ={'jobseeker':jobseeker}
    return render(request,"user_home.html",d)

def edit_udp(request):
    if not request.user.is_authenticated:
        return redirect("user_login")
    error=""
    user = request.user
    jobseeker = Jobseeker.objects.get(user=user)
    if request.method =='POST':
        cl = request.FILES['logo']
        
        jobseeker.image=cl
        try:
            jobseeker.save()
            error = 'no'
        except:
            pass
    d = {'error':error,'jobseeker':jobseeker}
    return render(request,"edit_udp.html",d) #udp = User dp

def edit_uhome(request):
    if not request.user.is_authenticated:
        return redirect("user_login")
    user = request.user
    jobseeker = Jobseeker.objects.get(user=user)
    error = ""
    if request.method =='POST':
        f = request.POST['fname']
        l = request.POST['lname']
        e = request.POST['email']
        con = request.POST["contactnum"]
        gen = request.POST["gender"]
        
        jobseeker.user.first_name = f
        jobseeker.user.last_name = l
        jobseeker.user.username = e
        jobseeker.mobile = con
        jobseeker.gender = gen
        
        try:
            jobseeker.save()
            jobseeker.user.save()
            error = 'no'
        except:
            error = "yes"
    d ={'jobseeker':jobseeker,'error':error}
    return render(request,"edit_uhome.html",d)

def delete_job(request,pid):
    if not request.user.is_authenticated:
        return redirect("recruiter_login")
    job = Job.objects.get(id=pid)
    job.delete()
    return redirect('all_jobs')

def delete_jobADM(request,pid):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    job = Job.objects.get(id=pid)
    job.delete()
    return redirect('admin_jobs')

def admin_jobs(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    job_filter = JobFilter(request.GET, queryset=Job.objects.all())
    d = {
        'form': job_filter.form,
        'data': job_filter.qs,
    }
    return render(request,"admin_jobs.html",d)

def job_list(request):
    if not request.user.is_authenticated:
        return redirect("recruiter_login")
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    job = Job.objects.filter(recruiter=recruiter)
    d = {'data':job}
    return render(request,"job_list.html",d)

def all_jobs(request):
    if not request.user.is_authenticated:
        return redirect("recruiter_login")
    job_filter = JobFilter(request.GET, queryset=Job.objects.all())
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    data1 = Job.objects.filter(recruiter=recruiter)
    li=[]
    for i in data1:
        li.append(i.id)
        
    d = {
        'form': job_filter.form,
        'data': job_filter.qs,
        'li':li,
    }
    return render(request,"all_jobs.html",d)

def latest_job(request):
    job_filter = JobFilter(request.GET, queryset=Job.objects.all())
    d = {
        'form': job_filter.form,
        'data': job_filter.qs,
    }
    return render(request,"latest_job.html",d)

def user_latestjobs(request):
    job_filter = JobFilter(request.GET, queryset=Job.objects.all())
    user = request.user
    student = Jobseeker.objects.get(user=user)
    data1 = Apply.objects.filter(student = student)
    li=[]
    for i in data1:
        li.append(i.job.id)
        
    d = {
        'form': job_filter.form,
        'data': job_filter.qs,
        'li':li,
    }
    return render(request,"user_latestjobs.html",d)

def job_detail(request,pid):
    data = Job.objects.get(id=pid)
    d = {'data':data}
    return render(request,"job_detail.html",d)

def applyfor_job(request,pid):
    if not request.user.is_authenticated:
        return redirect("user_login")
    error=""
    user = request.user
    student = Jobseeker.objects.get(user=user)
    job = Job.objects.get(id=pid)
    Uemail = student.user.username
    U_firstName = student.user.first_name
    U_lastName = student.user.last_name
    Remail = job.recruiter.user.username
    title = job.title
    date1 = date.today()
    if job.end_date < date1:
        error = 'close'
    elif job.start_date > date1:
        error = 'notopen'
    else:
        if request.method =='POST':
            r = request.FILES['resume']
            Apply.objects.create(job=job,
                                 student=student,
                                 resume=r,
                                 applydate=date.today())
            job_apply_mail(Uemail,Remail,U_firstName,U_lastName,title)
            error="done"
    d = {'error':error}
    return render(request,"applyfor_job.html",d)

def applied_candidatelist(request):
    if not request.user.is_authenticated:
        return redirect("recruiter_login")
    data = Apply.objects.all()
    d = {'data':data}
    return render(request,"applied_candidatelist.html",d)









# def search(request):
#     location = request.GET.get('location')
#     jobcatagory = request.GET.get('jobcatagory')
    
#     queryset = Job.objects.all()
    
#     if location:
#         queryset = Job.objects.filter(locations__icontains=location)
#     if jobcatagory:
#         queryset = Job.objects.filter(catagory=jobcatagory)
    
#     d = {
#         'products': queryset,
#     }
#     return render(request,"search.html",d)

# def u_search(request):
#     if not request.user.is_authenticated:
#         return redirect("user_login")
#     query = request.GET['search']
#     data3 = Job.objects.filter(title__icontains=query)
#     data1 = Job.objects.filter(skills__icontains=query)
#     data2 = Job.objects.filter(locations__icontains=query)
#     data4 = Job.objects.filter(salary__icontains=query)
#     data5 = Recruiter.objects.filter(company__icontains=query)
    
#     data = list(chain(data1,data3,data2,data4,data5))
#     d = {'data':data,}
#     return render(request,"u_search.html",d)

# def search(request):
#     q = request.GET.get('search')
#     if q is not None and q != u"":
#         q = request.GET.get('search')
#         queryset=Job.objects.filter(title__icontains=q)
#     else: 
#         queryset=Job.objects.all()
    
#     d = {
#         'products': queryset,
#     }
#     return render(request,"search.html",d)
