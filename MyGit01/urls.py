from django.conf.urls import url
from MyGit01.views import auth, customer

urlpatterns = [
    url(r'^login/$', auth.login, name='login'),
    url(r'^reg/$', auth.reg, name='reg'),
    url(r'^index/$', auth.index, name='index'),
    url(r'^customer_list/$', customer.customer_list, name='customer_list'),
    url(r'^customer_add/$', customer.customer_add, name='customer_add'),
    url(r'^customer_edit/(\d+)/$', customer.customer_edit, name='customer_edit'),
]
