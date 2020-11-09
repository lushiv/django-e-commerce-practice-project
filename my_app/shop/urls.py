from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = 'ShopHome'),
    path("about/", views.about_us, name = 'AboutUS'),
    path("contact/", views.contact, name = 'ContactUS'),
    path("tracker", views.tracker, name = 'Trackingstatus'),
    path("search/", views.search, name = 'Search'),
    path("productview/", views.prod_views, name = 'ProductViews'),
    path("checkout/", views.checkout, name = 'Checkout'),

]
