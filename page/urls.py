from django.urls import path
from .views import (
    home_view,
    # about_us_view,
    # #contact_us_view,
    # vision_view,
    # test_page,
    # #agamirli,
    page_view,
    #page_view_staff
)


urlpatterns = [
    path('', home_view, name='home'),
    # path('hakkimizda/', about_us_view, name='about_us'),
    # #path('iletisim/', contact_us_view, name='contact_us'),
    # path('vizyonumuz/', vision_view, name='vision'),
    # path('testpage/aga/', test_page, name='testpage'),
    # #path('staff/aghamir_aghamirli/', agamirli, name='agamirli'),
    path('<slug:slug>/', page_view),
    path('staff/<slug:slug>/', page_view),
    #path('staff/<slug:slug>/', page_view),
]
