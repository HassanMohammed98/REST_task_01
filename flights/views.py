from rest_framework.generics import ListAPIView
from .models import Flight, Booking
from datetime import date
from .serializers import FlightListSerializer, BookingListSerializer


class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer

class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gt=date.today())
    serializer_class = BookingListSerializer