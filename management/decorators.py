from django.shortcuts import render , redirect

def notLoggedUser(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

def allowedUser(allowedGroups=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowedGroups:
                return view_func(request,*args,**kwargs)
            else:
                return render(request, 'dashboard/accesserror.html')
        return wrapper_func
    return decorator