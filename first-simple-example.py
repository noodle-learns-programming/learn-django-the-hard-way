import sys
from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY='thisisthesecretkey',
    ROOT_URLCONF=__name__,#Cai nay nghia la sao ta?
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)
from django.conf.urls import url
from django.http import HttpResponse

# Cho nay thi minh hieu, giong nhu micro framework thui
def index(request):
    return HttpResponse('Hello World')

# Define lai router, co suc manh giong Zend khong?
urlpatterns = (
    url(r'^$', index),
)
#
#--------------------------------------------------------------------------------
# 1. Mo ra port va listen tren port do
# 2. Va giong nhu mot web server lun
#--------------------------------------------------------------------------------
#
if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
