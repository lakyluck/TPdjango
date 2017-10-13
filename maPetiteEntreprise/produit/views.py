# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from produit.models import *

def un_produit(request,id)
	nom_monproduit=Produit.object.get(id=id)
	return render(request,"un_produit.html",{"toto":nom_monproduit})# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
