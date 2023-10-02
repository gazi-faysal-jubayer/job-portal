"""JobPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from job.views import *
from django.conf import settings
from django.conf.urls.static import static
from django_email_verification import urls as email_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('user_home', user_home, name='user_home'),
    path('recruiter_home', recruiter_home, name='recruiter_home'),
    
    # about start
    path('about',about, name='about'),
    path('aboutU',aboutU, name='aboutU'),
    path('aboutR',aboutR, name='aboutR'),
    # about end
    
    # blog start 
    path('blog',blog, name='blog'),
    path('admBlog',admBlog, name='admBlog'),
    path('rec_blog',rec_blog, name='rec_blog'),
    path('user_blog',user_blog, name='user_blog'),
    path('blog/<str:slug>',blogPost, name='blogPost'),
    path('rec_blog/<str:slug>',blogPost_rec, name='blogPost_rec'),
    path('user_blog/<str:slug>',blogPost_user, name='blogPost_user'),
    path('admBlog/<str:slug>',blogPost_admin, name='blogPost_admin'),
    path('creatBlog',creatBlog, name='creatBlog'),
    path('creatBlog_rec',creatBlog_rec, name='creatBlog_rec'),
    path('delete_post/<str:slug>',delete_post, name='delete_post'),
    # blog start 
    
    # login, logout and others start 
    path('admin_login', admin_login, name='admin_login'),
    path('user_login/', user_login, name='user_login'),
    path('recruiter_login', recruiter_login, name='recruiter_login'),
    path('user_signup', user_signup, name='user_signup'),
    path('recruiter_signup',recruiter_signup, name='recruiter_signup'),
    path('Logout', Logout, name='Logout'),
    path('change_passwordadmin',change_passwordadmin, name='change_passwordadmin'),
    path('change_passworduser',change_passworduser, name='change_passworduser'),
    path('change_passwordrecruiter',change_passwordrecruiter, name='change_passwordrecruiter'),
    # login, logout and others end
    
    # filter job start
    path('job_DesignCreative', job_DesignCreative, name='job_DesignCreative'),
    path('job_DesignDevelopment', job_DesignDevelopment, name='job_DesignDevelopment'),
    path('job_MobileApplication', job_MobileApplication, name='job_MobileApplication'),
    path('job_SalesMarketing', job_SalesMarketing, name='job_SalesMarketing'),
    path('job_Construction', job_Construction, name='job_Construction'),
    path('job_InformationTechnology', job_InformationTechnology, name='job_InformationTechnology'),
    path('job_RealEstate', job_RealEstate, name='job_RealEstate'),
    path('job_ContentWriter', job_ContentWriter, name='job_ContentWriter'),
    # filter job end
    
    path('view_users', view_users, name='view_users'),
    path('delete_user/<int:pid>',delete_user, name='delete_user'),
    path('recruiter_pending', recruiter_pending, name='recruiter_pending'),
    path('change_status/<int:pid>',change_status, name='change_status'),
    path('selected/<int:pid>',selected, name='selected'),
    path('download_resume/<int:pid>', download_resume, name='download_resume'),
    path('recruiter_accepted',recruiter_accepted, name='recruiter_accepted'),
    path('recruiter_rejected',recruiter_rejected, name='recruiter_rejected'),
    path('recruiter_all',recruiter_all, name='recruiter_all'),
    path('delete_recruiter/<int:pid>',delete_recruiter, name='delete_recruiter'),

    path('add_job', add_job, name='add_job'),
    path('job_list', job_list, name='job_list'),
    path('all_jobs', all_jobs, name='all_jobs'),
    path('admin_jobs', admin_jobs, name='admin_jobs'),
    
    path('edit_jobdetail/<int:pid>',edit_jobdetail, name='edit_jobdetail'),
    path('change_companylogo/<int:pid>',change_companylogo, name='change_companylogo'),
    path('edit_rhome', edit_rhome, name='edit_rhome'),
    path('edit_rdp', edit_rdp, name='edit_rdp'),
    path('edit_udp', edit_udp, name='edit_udp'),
    path('edit_uhome', edit_uhome, name='edit_uhome'),
    path('latest_job', latest_job, name='latest_job'),
    path('user_latestjobs',user_latestjobs, name='user_latestjobs'),
    path('job_detail/<int:pid>',job_detail, name='job_detail'),
    path('delete_job/<int:pid>',delete_job, name='delete_job'),
    path('delete_jobADM/<int:pid>',delete_jobADM, name='delete_jobADM'),
    path('applyfor_job/<int:pid>',applyfor_job, name='applyfor_job'),
    path('applied_candidatelist',applied_candidatelist, name='applied_candidatelist'),
    
    # path('u_search', u_search, name='u_search'),
    # path('search', search, name='search'),
    # path('activate/<uidb64>/<token>',activate,name='activate'),
    # path('verify/<token>',verify, name='verify'),
    # path('email/<str:token>/', confirm),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
