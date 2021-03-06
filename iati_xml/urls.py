"""iati_xml URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
import codelists.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', codelists.views.home, name='home'),
    path('gazetteeragency/', codelists.views.gazetteerAgency, name='gazetteeragency'),
    path('documentcategory/', codelists.views.documentCategory, name='documentcategory'),
    path('activitydatetype/', codelists.views.activityDateType, name='activitydatetype'),
    path('budgetstatus/', codelists.views.budgetStatus, name='budgetstatus'),
    path('budgettype/', codelists.views.budgetType, name='budgettype'),
    path('organisationrole/', codelists.views.organisationRole, name='organisationrole'),
    path('relatedactivitytype/', codelists.views.relatedActivityType, name='relatedactivitytype'),
    path('transactiontype/', codelists.views.transactionType, name='transactiontype'),
    path('activitystatus/', codelists.views.activityStatus, name='activitystatus'),



]
