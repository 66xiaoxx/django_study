# import sys
# import os
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import models
from django import forms
from django.forms import  fields
from django.db import connection


class LoginFm(forms.Form):
    username = fields.CharField( error_messages={'required': '用户名不能为空.'},)
    password = fields.CharField(error_messages={'required': '密码不能为空.'},)


def login(request):
    if request.method=='GET':
        obj=LoginFm(request)
        # print("是这里-1")
        return  render(request,'login.html')
    else:
        obj=LoginFm(request.POST)
        r1 = obj.is_valid()
        if r1:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = models.SysUser.objects.filter(username=username)
            # print(user)
            # print("是这里0")
            if user:
                psw = user[0].password
                if password==psw:
                    request.session['is_login'] = '1'
                    # print(user[0].id )
                    request.session.setdefault('user_id',user[0].id)
                    # request.session.set_expiry(10)
                    # request.session['user_id'] = user[0].id
                    # print("是这里1")
                    # users_list = {'name': 1, 'account': 1, 'sex': 1, 'phone': 1}
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
            # print("是这里3")
            # print(obj.errors)
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
    print('是这样main页面')
    id1=request.session.get('user_id', None)
    print(id1)
    # username1 = request.POST.get('username')
    # print(username1)
    users=models.SysUser.objects.get(id=id1)
    user_name = users.name

    # user_name = models.SysUser.objects.only('name').get(id=1)
    user_account =users.username
    user_sex =users.sex
    user_phone=users.phone
    users_list={'name':user_name,'account':user_account,'sex':user_sex,'phone':user_phone}
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
    SQL_str = "select * from sys_user order by id desc"
    cursor = connection.cursor()
    cursor.execute(SQL_str)
    users = cursor.fetchall()
    # print(users)

    # users=models.SysUser.objects.all().order_by("id")
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
        # print('这是contacts')
        # print(type(contacts),contacts)

    # for user in users:
    #     user_list2= model_to_dict(user)
    #     user_items.append(user_list2)

    for p in contacts:
        # b=model_to_dict(p)
        # print(b)
        # print(type(p),p)
        user_items.append(list(p))
        # print('这是user_items')
        # print(type(user_items),user_items)
    print(user_items)
    return  render(request,'系统管理_用户管理.html',{'user_items':user_items, 'contacts': contacts})

class AddUserFm(forms.Form):
    name = forms.CharField(error_messages={'required': '姓名不能为空.'}, )
    account = forms.CharField(error_messages={'required': '用户名不能为空.'}, )
    staff = forms.CharField(error_messages={'required': '职务不能为空.'}, )
    password1 = forms.CharField(error_messages={'required': '密码不能为空.'}, )
    password2 = forms.CharField(error_messages={'required': '确认密码不能为空.'}, )
    phone = forms.CharField(error_messages={'required': '手机号不能为空.'}, )
    radio3 = forms.CharField(required=False)
    org = forms.CharField(required=False)
    radio2 = forms.CharField(required=False)

    def clean(self):
        if self.cleaned_data.get('password1') != self.cleaned_data.get('password2'):
            raise ValidationError('密码不一致')
        else:
            return self.cleaned_data


def adduser(request):
    if request.method=='GET':
        obj=AddUserFm(request)
        print("是这里-1")
        return  render(request,'系统管理_用户管理_新增.html')
    else:
        obj = AddUserFm(request.POST)
        print("是这里2")
        print(obj.changed_data)
        if obj.is_valid():
            # obj.changed_data.remove('password2')
            add_user = models.SysUser()
            add_user.name= request.POST.get("name")
            add_user.phone=request.POST.get("phone")
            add_user.sex=request.POST.get("radio3")
            add_user.account=request.POST.get("account")
            add_user.password=request.POST.get("password1")
            add_user.status=request.POST.get("radio2")
            add_user.staff=request.POST.get("staff")
            add_user.save()
            # models.SysUser.objects.create(**obj.cleaned_data)
            print("是这里3")
            return redirect('/系统管理_用户管理/')
        else:
            print("是这里4")
            print(obj.errors)
            return render(request,'系统管理_用户管理_新增.html',{'obj':obj})


    # print(type(obj.changed_data),obj.changed_data)
    # print(
    #     obj.errors)
    # username = obj.cleaned_data.get('name')
    # print(username)
    #     return  HttpResponse('超棒')
    # else:return  HttpResponse('超棒2')
    #     name=request.POST.get("name")
    #     account=request.POST.get("account")
    #     org=request.POST.get("org")
    #     staff=request.POST.get("staff")
    #     password1=request.POST.get("password1")
    #     password2=request.POST.get("password2")
    #     state=request.POST.get("radio2")
    #     sex=request.POST.get("radio3")
    #     phone=request.POST.get("phone")
    #     print(name,account,org,staff,password1,password2,state,sex,phone)
    # if password1==password2:
    #     add_user=models.SysUser()
    #     add_user.name=name
    #     add_user.phone=phone
    #     add_user.sex=sex
    #     add_user.username=account
    #     add_user.password=password1
    #     add_user.status=state
    #     add_user.staff=staff
    #     add_user.save()
    # else:
    #     error="两次输入的密码不一致"
    #     return render(request,)



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
