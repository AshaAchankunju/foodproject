from django.shortcuts import render, redirect

from django.views.generic import View
from myapp.models import Food
from django import forms


class FoodForm(forms.Form):
    name=forms.CharField()
    country=forms.CharField()
    color=forms.CharField()
    type=forms.CharField()
    price=forms.IntegerField()


# Create your views here.
class FoodListView(View):
    def get(self,request,*args,**kwargs):
        qs=Food.objects.all()
        return render(request,"food_list.html",{"data":qs})

class FoodDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Food.objects.get(id=id)
        return render(request,"food_detail.html",{"data":qs})
    
class FoodDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Food.objects.get(id=id).delete()
        return redirect("food-all")

class FoodCreateView(View):
    def get(self,request,*args,**kwargs):
        form=FoodForm()
        return render(request,'food_add.html',{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=FoodForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            Food.objects.create(**data)
            return redirect('food-all')
        else:
            return render(request,'food_add.html',{"form":form})
class FoodUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        food_objects=Food.objects.get(id=id)
        data={
            "name":food_objects.name,
            "country":food_objects.country,
            "color":food_objects.color,
            "type":food_objects.type,
            "price":food_objects.price
        }
        form=FoodForm(initial=data)
        return render(request,'food_edit.html',{"form":form})
    def post(self,request,*args,**kwargs):
        form=FoodForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            id=kwargs.get("pk")
            Food.objects.filter(id=id).update(**data)
            return redirect('food-all')
        else:
            return redirect(request,'food_edit.html',{'form':form})