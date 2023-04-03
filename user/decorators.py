from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

def manager_required(function =None, redirect_field_name =REDIRECT_FIELD_NAME,login_url='login'):
    #actual_decorator user defined function
    actual_decorator = user_passes_test(lambda user:user.is_active and user.is_manager1,login_url=login_url,redirect_field_name=redirect_field_name)
    if function:
        return actual_decorator(function)
    return actual_decorator

def developer_required(function =None, redirect_field_name =REDIRECT_FIELD_NAME,login_url='login'):
    #actual_decorator user defined function
    actual_decorator = user_passes_test(lambda user:user.is_active and user.is_devleopr,login_url=login_url,redirect_field_name=redirect_field_name)
    if function:
        return actual_decorator(function)
    return actual_decorator

    