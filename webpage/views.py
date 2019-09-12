# import sys
# import os
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms import model_to_dict
from functools import wraps

from django.http import HttpResponse
from django.shortcuts import render,redirect
# sys.path.insert(0, os.path.abspath(".."))
from . import models
# from . import models
from django import forms
from django.forms import  fields

class FM(forms.Form):
    username = fields.CharField( error_messages={'required': '用户名不能为空.'},)
    password = fields.CharField(error_messages={'required': '密码不能为空.'},)


def login(request):
    if request.method=='GET':
        obj=FM(request)
        print("是这里-1")
        return  render(request,'login.html')
    else:
        obj=FM(request.POST)
        r1 = obj.is_valid()
        if r1:
            username = request.POST.get('username')
            password = request.POST.get('password')
            # user = models.SysUser.objects.get(account=username)
            # print(user)
            print("是这里0")
            if models.SysUser.objects.get(account=username):
                psw = models.SysUser.objects.get(account=username).password
                if password==psw:
                    request.session['is_login'] = '1'
                    # print(user[0].id )
                    request.session.setdefault('user_id',user[0].id)
                    request.session.set_expiry(10)
                    # request.session['user_id'] = user[0].id
                    print("是这里1")
                    users_list = {'name': 1, 'account': 1, 'sex': 1, 'phone': 1}
                    res= redirect('/main/')
                    # res.set_cookie("username",username,max_age=10,httponly=True)
                    # print("cookie失效时间")
                    return  res
                    # return redirect('/login/main')
                else:
                    error="用户名或密码不对"
                    return render(request, 'login.html', {'error': error})
            else:
                error = "用户名或密码不对"
                return render(request, 'login.html',{'error':error})
        else:
            # print(obj.errors.as_json)
            print("是这里3")
            print(obj.errors)
            return render(request, 'login.html',{'obj':obj})


def check_login(f):
    # @wraps(f)
    def inner(request,*arg,**kwargs):
        if request.session.get('is_login',None):
        # if request.COOKIES.get('username'):
            return f(request,*arg,**kwargs)
        else:
            return redirect(login)
    return inner


@check_login
def main(request):
    users=models.SysUser.objects.get(id=1)
    user_name = users.name

    # user_name = models.SysUser.objects.only('name').get(id=1)
    user_account =models.SysUser.objects.only('account').get(id=1)
    user_sex =models.SysUser.objects.only('sex').get(id=1)
    user_phone=models.SysUser.objects.only('phone').get(id=1)
    users_list={'name':user_name,'account':1,'sex':user_name,'phone':user_sex}
    print(users_list)
    return  render(request,'main.html',{'users_list':users_list})
    # return  render(request,'login1/系统管理_用户管理.html')


def register(request):
    pass
    return  render(request,'register.html')


def logout(request):
    key=request.session.session_key
    print(key)
    request.session.flush()
    print("清楚session")
    print(request.session.get(key,None))
    return redirect('/login/')


def sysuser(request):
    user_items = []
    users=models.SysUser.objects.all().order_by("id")
    paginator = Paginator(users, 2)  # 每页显示 10 个联系人
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果用户请求的页码号不是整数，显示第一页
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果用户请求的页码号超过了最大页码号，显示最后一页
        contacts = paginator.page(paginator.num_pages)

    # for user in users:
    #     user_list2= model_to_dict(user)
    #     user_items.append(user_list2)

    for p in contacts:
        b=model_to_dict(p)
        user_items.append(b)
    return  render(request,'系统管理_用户管理.html',{'user_items':user_items, 'contacts': contacts})


def sysbottom(request):
    return render(request, '系统管理_按钮管理.html')


def sysmenu(request):
    return render(request, '系统管理_菜单管理.html')


def sysorg(request):
    return render(request, '系统管理_机构管理.html')


def sysrole(request):
    return render(request, '系统管理_角色管理.html')


def param(request):
    return render(request, '系统管理_数据字典.html')


