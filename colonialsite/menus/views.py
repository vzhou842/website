from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import viewsets, generics

from django_filters.rest_framework import DjangoFilterBackend

from menus.models import MenuCategory, Dish, Rating
from menus.serializers import MenuCategorySerializer, DishSerializer, RatingSerializer

# Create your views here.

@login_required
def index(request):
    title = "Colonial Menus"
    template = 'menus/index.html'
    context = {
            'title': title
            }

    return render(request, template, context)

class DishViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    """ API endpoint that allows dishes to be viewed or edited """
    queryset = Dish.objects.all().order_by('name')
    serializer_class = DishSerializer

    @detail_route(methods=['delete'])
    def remove_dish_from_menu(self, request, pk=None):
        dish = self.get_object()
        remove_menu = request.data['menu']
        deleteSet = MenuCategory.objects.filter(id=remove_menu)
        for d in deleteSet:
            dish.menus.remove(d)
        return Response({'status':'removed from menu'})

class RatingViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = Rating.objects.all().order_by('value')
    serializer_class = RatingSerializer

    def perform_create(self, serializer):
        new_rating = serializer.save(reviewingUser=self.request.user)

class MenuCategoryViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all().order_by('category')
    serializer_class = MenuCategorySerializer

class MenuCategoryByDate(LoginRequiredMixin, generics.ListAPIView):
    model = MenuCategory
    serializer_class = MenuCategorySerializer
    queryset = MenuCategory.objects.all().order_by('category')
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('date',)
