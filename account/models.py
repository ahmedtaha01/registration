from asyncio.windows_events import NULL
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from urllib.request import urlopen
from django.core.files import File 
from django.core.files.temp import NamedTemporaryFile
from django_countries.fields import CountryField
import datetime

# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='account/image',null=True)
    phone = models.CharField(max_length=11)
    is_active = models.BooleanField(null=True)
    birthday = models.DateField(null=True)
    country = CountryField(default='EG')



    def get_image_from_url(self, url):
        img_temp = NamedTemporaryFile()
        img_temp.write(urlopen(url).read())
        img_temp.flush()
        self.image.save("image_%s" % self.pk +'.jpg', File(img_temp))
        self.is_active = True
        self.save()