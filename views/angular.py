from django import forms
import hashlib
from django.http import HttpResponse
from PIL import Image, ImageDraw
from io import BytesIO
from django.views.decorators.http import etag
from django.core.urlresolvers import reverse
from django.shortcuts import render

class ImageForm(forms.Form):
    """Form to validate requested placeholder image."""
    height = forms.IntegerField(min_value=1, max_value=2000)
    width = forms.IntegerField(min_value=1, max_value=2000)

    def generate(self, image_format='PNG'):
        """Generate an image of the given type and return as raw bytes."""
        height = self.cleaned_data['height']
        width = self.cleaned_data['width']
        image = Image.new('RGB', (width, height))
        draw = ImageDraw.Draw(image)
        text = '{} X {}'.format(width, height)
        textwidth, textheight = draw.textsize(text)
        if textwidth < width and textheight < height:
            texttop = (height - textheight) // 2
            textleft = (width - textwidth) // 2
            draw.text((textleft, texttop), text, fill=(255, 255, 255))
        content = BytesIO()
        image.save(content, image_format)
        content.seek(0)
        return content

def generate_etag(request, width, height):
    content = 'Placeholder: {0} x {1}'.format(width, height)
    return hashlib.sha1(content.encode('utf-8')).hexdigest()

#Thu key moi
def add(req, n1, n2):
    content = 'Add: {0} + {1}'.format(n1, n2)
    return HttpResponse(content)

#Tu duy cho nay cua Python la rat hay
#Cho etag nay khong thay work voi Chrome gi het
@etag(generate_etag)
def placeholder(req, width, height):
    from pprint import pprint
    form = ImageForm({'height': height, 'width': width})
    pprint(vars(form))
    if form.is_valid():
        height = form.cleaned_data['height']
        width = form.cleaned_data['width']
        # TODO: Generate image of requested size
        image = form.generate()
        response = HttpResponse(image, content_type='image/png')
        # response['Cache-Control'] = 'private, no-cache, no-store'
        response['Max-Age'] = 86400
        return response
    else:
        return HttpResponseBadRequest('Invalid Image Request')


def home(request):
    example = reverse('placeholder', kwargs={'width': 50, 'height':50})
    context = {
        'example': request.build_absolute_uri(example)
    }
    return render(request, 'home.html', context)