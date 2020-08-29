from django.urls import path
from . import views
from .views import (
    PostListView
)


urlpatterns = [
	path('', PostListView.as_view(), name='home'),
	path('search/',views.search,name='search' ),
        path('anho/<int:ango>',views.filtroanho,name='anho'),
        path('mes/<int:ango>/<str:mes>',views.filtromes,name='mes'),
    #path('show/',views.showFac,name='showFac')
]
