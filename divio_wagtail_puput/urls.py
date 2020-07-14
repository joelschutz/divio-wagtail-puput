# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from puput import urls as puput_urls

urlpatterns = [
    url(r'', include(puput_urls)),
]
