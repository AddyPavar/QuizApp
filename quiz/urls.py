"""Quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^addQuiz/',views.first),
    url(r'^dbQuiz/',views.addQuiz),
    url(r'^dbQue/',views.addQ),
    url(r'^showQuiz/',views.showQuiz),
    url(r'^QuizPage/([0-9]{1,2})/$',views.test),
    url(r'^Caught/([0-9]{1,3})/$',views.getAns),
    url(r'^login/',views.login),
    url(r'^signup/',views.signup),
    url(r'^validate/',views.auth),
    url(r'^register/',views.register),
    url(r'^check/',views.marking),
    url(r'^signout/',views.signout),
    url(r'^reporting/',views.reporting)
]+ staticfiles_urlpatterns()
