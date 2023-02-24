from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from datetime import *

@api_view(["POST"])
def chartApi(request):
    dates= JSONParser().parse(request)
    {
        "start":"2023-01-01",
        "end":"2023-01-01"
    }  
    data=requests.get("http://127.0.0.1:8080/chart_api/"+dates['start']+"/"+dates['end'])
    print(data)
    return Response(data.json())


@api_view(["POST","PUT"])
def updateOrderStatus(request):
    data=dict(JSONParser().parse(request))
    sent=requests.post("http://127.0.0.1:8080/updateOrderStatus/",json=data)
    return Response(sent.json())

@api_view(["POST"])
def saveOrder(request):
    requestdata=JSONParser().parse(request)
    sent=requests.post("http://127.0.0.1:8080/saveOrder/",json=dict(requestdata))
    return Response(sent.json())

@api_view(["POST"])
def searchOrder(requset):
    data=JSONParser().parse(requset)
    sent=requests.post("http://127.0.0.1:8080/orderSearch/",json=dict(data))
    return Response(sent.json())

@api_view(["GET","POST"])
def testjson(request):
    todaydate=datetime.today().date()
    print(str(todaydate))
    jsonData=dict(JSONParser().parse(request))
    apidist={
    "orderId": "6246",
    "orderType": 1,
    "pickupTime": "2022-02-02T10:40:00",
    "arrivalTime": str(todaydate)+"T10:30:00",
    "deliveryIsAsap": True,
    "note": "Make it fast",
    "items": '',
    "remake": False,
    "customerName": "MD1",
    "status": "pending",
    "orderPointId": 1
    }
    print(apidist)
    res={}
    itemslist=[]
    for hotelName in jsonData:
        d={}
        for categories in jsonData[hotelName]['items'][0]['entries']['items']:
            li=[]
            for itemDetail in categories['entries']['items']:
                custdict={
                "plu": "CMB-02",
                "name": itemDetail['name'],
                "quantity": 10,
                "tag": 1,
                "subItems": [],
                "itemRemark": itemDetail['description'],
                "unit":"qty"
                }
                li.append(custdict)
            d[categories['name']]=li
        itemslist.append(d)
    res['items']=itemslist
    newRecords=[]
    for categories in res["items"]:
        apidist["items"]=categories
        sent=requests.post("http://127.0.0.1:8080/saveOrder/",json=apidist)
        newRecords.append(sent.json())
    return Response(newRecords)