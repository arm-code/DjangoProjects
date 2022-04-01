from django.shortcuts import render, redirect
from django import views
from django.http import HttpResponse
from .models import UserModel

# Create your views here.


class GetUsersView(views.View):

    def get(self, request):
        users = UserModel.objects.all()
        template_name = 'main/list.html'
        context = {
            'users': users
        }
        return render(request, template_name, context)
        # print("Los usuarios ", users)
        # return HttpResponse('Hola alexis')


def GetUserView(request, id):
    user = UserModel.objects.get(pk = id)
    template_name = 'main/detail.html'
    context = {
        'user': user
    }
    return render(request, template_name, context)