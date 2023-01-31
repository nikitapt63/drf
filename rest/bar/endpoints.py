from rest_framework.generics import ListAPIView
from .serializers import PageSerializer
from .models import Page


class PageListView(ListAPIView):
    serializer_class = PageSerializer
    queryset = Page.objects.all()
