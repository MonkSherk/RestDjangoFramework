from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Hentai

# Create your views here.

model_global = Hentai

class HentaiView(APIView):
    def get(self, request):
        data = model_global.objects.all().values()
        return Response({
            'data': data,
            'count': data.count()
        })

    def post(self, request):
        added_model = model_global.objects.create(
            title=request.data.get('title'),
            author=request.data.get('author'),
            description=request.data.get('description'),
            publication_date = request.data.get('publication_date')
        )
        return Response({
            'data': model_to_dict(added_model),
            'message': 'Hentai added successfully.'
        })



class UpdateHentaiView(APIView):
    def get(self,request,id):
        hentai = model_global.objects.filter(id=id).values()
        if hentai:
            return Response({
                'data': hentai
            })
        else:
            return Response({
               'message': 'Hentai not found.'
            })
    def put(self, request, id):
        hentai = model_global.objects.get(id=id)
        if hentai:
            hentai.title = request.data.get('title')
            hentai.author = request.data.get('author')
            hentai.description = request.data.get('description')
            hentai.save()
            return Response({
                'data': model_to_dict(hentai),
                'message': 'Hentai updated successfully.'
            })
        else:
            return Response({
                'message': 'Hentai not found.'
            })

class DeleteHentaiView(APIView):
    def get(self, request, id):
        hentai = model_global.objects.filter(id=id).values()
        if hentai:
            return Response({
                'data': hentai
            })
        else:
            return Response({
               'message': 'Hentai not found.'
            })
    def delete(self, request, id):
        hentai = model_global.objects.filter(id=id)
        if hentai:
            hentai.delete()
            return Response({
                'message': 'Hentai deleted successfully.'
            })
        else:
            return Response({
                'message': 'Hentai not found.'
            })