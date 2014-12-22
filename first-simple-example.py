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

    """

    :param request:
    :return:
    """
    return HttpResponse('Hello World')


def new(request):
    """

    :param request:
    :return:
    """

    return HttpResponse('New View')

def placeholder(request, width, height):
    content = 'Placeholder: {0} x {1}'.format(width, height)
    return HttpResponse(content)

# Define lai router, co suc manh giong Zend khong?
# Su dung dc cai bien global nay lun ha ta?
#
urlpatterns = (
    url(r'^$', index),
    url('new', new),
    url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$', placeholder, name='placeholder'),
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
