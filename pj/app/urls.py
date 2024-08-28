from django.urls import path

from app import views

urlpatterns = [
    path('hentai/', views.HentaiView.as_view(), name='hentai_view'),
    path('upd_hen/<int:id>',views.UpdateHentaiView.as_view() , name='update_hentai_view'),
    path('add_hentai/', views.HentaiView.as_view(), name='add_h'),
    path('del_hen/<int:id>', views.DeleteHentaiView.as_view(), name='delete_hentai_view'),

]