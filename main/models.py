from django.db import models
from main.abstract import BaseModel, OrderModel, ActiveModel
from django.utils.translation import gettext_lazy as _


class Home(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    sub_title = models.CharField(max_length=255, verbose_name=_('sub_title'))   
    icon = models.ImageField(upload_to='Home/%Y/%m/%d', verbose_name=_('icon'))

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Homes'


