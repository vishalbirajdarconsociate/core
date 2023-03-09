from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import logout
from useradmin.models import *
from core.models import *
from django.db.models import Avg,Q
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from deep_translator import GoogleTranslator
# from indic_transliteration.sanscript import transliterate
# from indic_transliteration import sanscript  
def trans(txt,lang):
    return GoogleTranslator(source='auto', target=lang).translate(txt)

def index(request):
    if request.session.get('user_id') is None:
        text="judge not thou me , as i jugde not thee. betwixt the stirrup and the ground,mercy i sought ,and mercy found"
        # pr=(transliterate(text, sanscript.ITRANS,sanscript.DEVANAGARI))
        p=trans(text,"mr")
        return JsonResponse({"text":text,"script":'pr',"translation":p})
    return JsonResponse({"kiosk":"app"})


@api_view(["POST"])
def login(request):
    data = JSONParser().parse(request)
    try:
        user=VendorLog.objects.get(Q(password=data['password'])&(Q(userName= data['username'])|Q(email= data['username'])))
        request.session['user_id'] = user.pk
        # if request.session.test_cookie_worked():
        #     request.session.delete_test_cookie()
        #     return Response({"A":"You're logged in"})
        # else:
        #     return Response("Please enable cookies and try again.")
        return Response({"msg":"user found","userid":user.pk})
    except VendorLog.DoesNotExist:
        return Response({"err":"user not found"})


def logout_view(request):
    id=request.session.get('user_id')
    if id:
        logout(request)
        return JsonResponse({"msg":'user logged out'})
    return JsonResponse({"msg":'not logged in '})


@api_view(['GET'])
def allCategory(request,id=0):
    # if request.session.get('user_id') is None:
    #     return JsonResponse({"kiosk":"session not found"})
    data=[]
    if id!=0:
        i = Category.objects.get(pk=id)
        data.append({
      "categoryId": i.pk,
      "name": i.categoryName,
      "vendorId": i.vendorId.pk,
      "description": i.categoryDescription,
      "image":str(i.categoryImgage)
        })
        return Response({"Category":data})
           
    for i in Category.objects.all():
        data.append({
      "categoryId": i.pk,
      "name": i.categoryName,
      "vendorId": i.vendorId.pk,
      "description": i.categoryDescription,
      "image":str(i.categoryImgage)
        })
    banner=[
    {
      "image":
          "https://theweekendedition.com.au/wp-content/uploads/sites/6/2017/05/TWE-main-street-burger-bar-08-1100x550-c-center.jpg"
    },
    {
      "image":
          "https://cdn.bfldr.com/97UXF3S6/at/58qmhsfnxjfffhp2jsmv4x/CraveBurger_Combo.jpg?auto=webp&format=png"
    },
    {
      "image":
          "https://images.deliveryhero.io/image/fd-pk/LH/v4ce-hero.jpg"
    },
    {
      "image":
          "https://b.zmtcdn.com/data/pictures/chains/2/18796372/7d4e1122bb98065689b46e87753887aa.jpg?fit=around|771.75:416.25&crop=771.75:416.25;*,*"
    },
    {
      "image":
          "https://images.squarespace-cdn.com/content/v1/5db7063530eb0e7c27e50381/1573227775511-PMQ13KETDCD0D6H4DNAK/Banner+Image.png?format=2500w"
    },
    {
      "image":
          "https://www.crazymasalafood.com/wp-content/images/1-37.jpg"
    }
  ]
    return Response({"Category":data,'banner':banner})


@api_view(["GET"])
def productByCategory(request,id=0):
    if request.session.get('user_id') is None:
        return Response({"kiosk":"session not found"})
    products={}
    if id!=0:
        i=Category.objects.get(pk=id)
        li=[]
        for j in Product.objects.filter(pk__in=(ProductCategory.objects.filter(category=i.pk).values('product'))):
            images=[]
            for k in ProductImages.objects.filter(product=j.pk):
                images.append(str(k.image))
            mod=[]
            for m in Modifier.objects.filter(pk__in=(ModifierModGroup.objects.values('modifier').filter(modifierGroup__in=(ModifierGroup.objects.filter(pk__in=(ProductModGroup.objects.filter(product=j.pk).values('modifierGroup'))))))):
                mod.append(
                    {
                        "cost":m.modifierPrice,
                        "modifierId": m.pk,
                        "description": m.modifierDesc,
                        "quantity": m.modifierQty,
                        "sku": m.modifierSKU,
                        "status":m.modifierStatus,
                        "image":str(m.modifierImg)
                    }                    
                )
            li.append({
                "categoryId": i.pk,
                "categoryName":i.categoryName,
                "prdouctId": j.pk,
                "text": j.productName,
                "imagePath": str(j.productThumb),
                "images":images,
                "quantity": j.productQty,
                "cost": j.productPrice,
                "description": j.productDesc,
                "allowCustomerNotes": True,
                "vendorId": j.vendorId.pk,
                "modifier":mod
            })
        products[i.pk]=li       
        return Response({"products":products})
        
    for i in Category.objects.all():
        li=[]
        for j in Product.objects.filter(pk__in=(ProductCategory.objects.filter(category=i.pk).values('product'))):
            images=[]
            for k in ProductImages.objects.filter(product=j.pk):
                images.append(str(k.image))
            mod=[]
            for m in Modifier.objects.filter(pk__in=(ModifierModGroup.objects.values('modifier').filter(modifierGroup__in=(ModifierGroup.objects.filter(pk__in=(ProductModGroup.objects.filter(product=j.pk).values('modifierGroup'))))))):
                mod.append(
                    {
                        "cost":m.modifierPrice,
                        "modifierId": m.pk,
                        "description": m.modifierDesc,
                        "quantity": m.modifierQty,
                        "sku": m.modifierSKU,
                        "status":m.modifierStatus,
                        "image":str(m.modifierImg)
                    }                    
                )
            li.append({
                "categoryId": i.pk,
                "categoryName":i.categoryName,
                "prdouctId": j.pk,
                "text": j.productName,
                "imagePath": str(j.productThumb),
                "images":images,
                "quantity": j.productQty,
                "cost": j.productPrice,
                "description": j.productDesc,
                "allowCustomerNotes": True,
                "vendorId": j.vendorId.pk,
                "modifier":mod
            })
        products[i.pk]=li
    return Response({"products":products})


@api_view(["GET"])
def productDetails(request,id=0,search=''):
    if request.session.get('user_id') is None:
        return JsonResponse({"kiosk":"session not found"})
    data=Product.objects.all()
    li=[]
    if id!=0:
        data=Product.objects.filter(pk=id)
    if len(search)!=0:
        data=Product.objects.filter(Q(productName__icontains=search)
                                    |Q(productDesc__icontains=search)
                                    |Q(pk__in=(ProductCategory.objects.filter(category__in=(
                                        Category.objects.filter(categoryName__icontains=search)
                                    ))))).distinct()
    for j in data:
            images=[]
            for k in ProductImages.objects.filter(product=j.pk):
                images.append(str(k.image))
            mod=[]
            for m in Modifier.objects.filter(pk__in=(ModifierModGroup.objects.values('modifier').filter(modifierGroup__in=(ModifierGroup.objects.filter(pk__in=(ProductModGroup.objects.filter(product=j.pk).values('modifierGroup'))))))):
                mod.append(
                    {
                        "cost":m.modifierPrice,
                        "modifierId": m.pk,
                        "description": m.modifierDesc,
                        "quantity": m.modifierQty,
                        "sku": m.modifierSKU,
                        "status":m.modifierStatus,
                        "image":str(m.modifierImg)
                    }                    
                )
            # i=ProductCategory.objects.get(product=id)
            li.append({
                # "categoryId": i.category.pk,
                # "categoryName":i.category.categoryName,
                "prdouctId": j.pk,
                "text": j.productName,
                "imagePath": str(j.productThumb),
                "images":images,
                "quantity": j.productQty,
                "cost": j.productPrice,
                "description": j.productDesc,
                "allowCustomerNotes": True,
                "vendorId": j.vendorId.pk,
                "modifier":mod
            })
    return Response({'product':li})


@api_view((["GET","POST"]))
def addToCart(request):
    data = JSONParser().parse(request)
    for v in data:
        # print(data[v])
        if isinstance(data[v],list):
            for ind,i in enumerate( data[v]):
                for a in i:
                    print(data[v][ind][a])
    return Response({"POST":data})