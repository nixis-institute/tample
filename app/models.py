from django.db import models
from PIL import Image
from io import BytesIO
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.

class Temple(models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    block = models.CharField(max_length=20)
    address = models.TextField()
    latitude = models.CharField(max_length=15)
    logitute = models.CharField(max_length=15)

    def __str__(self):
        return self.name+" "+self.pincode

class ProductImages(models.Model):
    tample = models.ForeignKey(Temple,on_delete=models.CASCADE)
    original = models.ImageField(upload_to='photos/packages/original',null=True,blank=True)
    normal = models.ImageField(upload_to='photos/packages/thumbs',null=True,blank=True)
    thumbnail = models.ImageField(upload_to='photos/packages/thumbs',null=True,blank=True)
    alt = models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return "{} : {}".format(self.tample.name,self.alt)
    def save(self,force_insert=False,force_update=False,using=None):
        im = Image.open(self.original)
        output = BytesIO()
        basewidth = 600
        wpercent = (basewidth/float(im.size[0]))
        hsize = int((float(im.size[1])*float(wpercent)))
        im = im.resize((basewidth,hsize), Image.ANTIALIAS)
        im = im.convert("RGB")
        im.save(output, format='JPEG', quality=40)
        self.normal = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.original.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)


        weight,height=im.size
        if weight > height:
            r=(weight-height)/2
            imc=im.crop((r,0,height+r,height))
        else:
            r=(height-weight)/2
            imc=im.crop((0,r,weight,height-r))
        imc = imc.convert("RGB") 
        imc=imc.resize((300,300),Image.ANTIALIAS)
        output = BytesIO()
        imc.save(output, format='JPEG', quality=70)
        output.seek(0)
        self.thumbnail = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.original.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
        super(ProductImages,self).save()
