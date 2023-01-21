import functools
from django.shortcuts import redirect
from django.contrib import messages

def user_required(view_func, redirect_url="index"):

    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        print(request)
        print("############ ATTEMPTING ########")
        print(request.user)
        if request.user:
            return view_func(request, *args, **kwargs)
        messages.info(request, "Please sign in")
        return redirect(redirect_url)
    return wrapper