from django.shortcuts import render, redirect, reverse, HttpResponse
from MyGit01 import models
from MyGit01.forms import CustomerForm


def customer_list(request):
    if request.path_info == reverse('customer_list'):
        all_customer = models.Customer.objects.all()

    return render(request, 'customer_list.html', {"all_customer": all_customer})


def customer_add(request):
    # 不包含数据的form
    form_obj = CustomerForm()

    if request.method == 'POST':
        # 包含用户提交数据的form
        form_obj = CustomerForm(request.POST)
        # 对数据进行校验
        if form_obj.is_valid():
            form_obj.save()  # 创建对象
            # 跳转到展示页面
            return redirect(reverse('customer_list'))

    return render(request, 'customer_add.html', {'form_obj': form_obj})


def customer_edit(request, edit_id):
    obj = models.Customer.objects.filter(pk=edit_id).first()

    # 处理POST
    if request.method == 'POST':
        # 包含提交的数据 原始数据
        form_obj = CustomerForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()  # 保存修改
            # 跳转到展示页面
            return redirect(reverse('customer_list'))
    else:
        # 包含原始数据的form表单
        form_obj = CustomerForm(instance=obj)

    return render(request, 'customer_edit.html', {'form_obj': form_obj})


def customer_change(request, edit_id=None):
    obj = models.Customer.objects.filter(pk=edit_id).first()

    # 处理POST
    if request.method == 'POST':
        # 包含提交的数据 原始数据
        form_obj = CustomerForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            # 跳转到展示页面

            next = request.GET.get('next')

            return redirect(next)
    else:
        form_obj = CustomerForm(instance=obj)

    title = '编辑客户' if edit_id else '添加客户'

    return render(request, 'customer_change.html', {'title': title, 'form_obj': form_obj})


# def customer_del(request, del_id):
#     obj = models.Customer.objects.filter(pk=del_id)
#
#     return render(request,'customer_edit.html', {'form_obj': form_obj})
