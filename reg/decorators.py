from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

def user_required(function=None, name=REDIRECT_FIELD_NAME, login_url='sgin_user'):
    actual_decorator = user_passes_test(lambda u: u.is_active and u.is_user, login_url=login_url)
    if function:
        return actual_decorator(function)
    return actual_decorator

def hospital_required(function=None, name=REDIRECT_FIELD_NAME, login_url='sgin_hsp'):
    actual_decorator = user_passes_test(lambda u: u.is_active and u.is_hospital, login_url=login_url)
    if function:
        return actual_decorator(function)
    return actual_decorator