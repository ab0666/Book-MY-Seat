from django.urls import path
from attendee import views
from attendee.controller import authview, queues, checkout, booking


urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("services", views.services, name="services"),
    path('services/<str:slug>', views.servicesview, name="servicesview"),
    path('services/<str:cate_slug>/<str:evt_slug>', views.eventview, name="eventview"), 


    path('register/', authview.register, name="register"),
    path('login/', authview.loginpage, name="loginpage"),
    path('logout', authview.logoutpage, name="logout"),

    path('add-to-queues', queues.addtoqueues, name="addtoqueues"),
    path('queues', queues.viewqueues, name="queues"),
    path('update-queues', queues.updatequeues, name="updatequeues"),
    path('delete-cart-item', queues.deletecartitem, name="deletecartitem"),

    path('checkout', checkout.index, name="checkout"),
    path('placebooking', checkout.placebooking, name="placebooking"),
    path('my-bookings', booking.index, name= "mybookings"),
    path('view-booking/<str:t_no>', booking.viewbooking, name= "bookingview"),

] 