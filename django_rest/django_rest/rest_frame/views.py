from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import  api_view
from rest_framework.response import  Response

# Create your views here.
def index(request):
    return render(request,'rest_frame/index.html')

# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])

@api_view(["GET","POST"])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)

        return JsonResponse(serializer.errors,status = 400 )

@csrf_exempt
def article_id(request,pk):
    try:
        article = Article.objects.get(pk=pk)

    except Article.DoesNotExist:

        return HttpResponse("Object doesn't exist")

    if request.method == "GET":
  
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article,data =data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors,status = 400 )

    elif request.method ==  "DELETE":
        article.delete()
        return HttpResponse(status=204)
        