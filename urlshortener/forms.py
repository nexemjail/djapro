from django.forms import ModelForm
from urlshortener.models import ShortUrl

class ShortUrlForm(ModelForm):
    class Meta:
        model = ShortUrl
        fields = ['url']
        # visible = ['url']
