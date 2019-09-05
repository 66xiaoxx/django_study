from django.shortcuts import render,redirect

def main(request):
    pass
    return  render(request,'login1/main.html')


def login(request):
    pass
    return  render(request,'login/login.html')


def register(request):
    pass
    return  render(request,'login/register.html')


def logout(request):
    pass
    return  render(request,'login/index.html')
