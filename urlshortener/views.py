from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from urlshortener.models import ShortUrl
from urlshortener.forms import ShortUrlForm

def redirect_to_url(request, url):
    print(url)
    qs = ShortUrl.objects.filter(short_name=url)
    if qs.exists():
        shortened_url = qs.first()
        return HttpResponseRedirect(shortened_url.url)
    raise Http404


def shorten_url(request):
    if request.method == 'GET':
        form = ShortUrlForm()
        return render(request, 'urlshortener/short_url.html', {'form' : form})
    if request.method == 'POST':
        short_url = ShortUrlForm(request.POST)

        shortened_url_obj = short_url.save(commit=False)
        shortened_url_obj.short_name = 'jihad'
        shortened_url_obj.save()
        # print(short_url.url)
    # short_url = ShortUrl(url = url, short_name='allah')
    # short_url.save()
        return HttpResponse(str(request.get_host() + '/' +  shortened_url_obj.short_name))

# Create your views here.
