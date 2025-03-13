from django.utils.dateparse import parse_date
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rooms.models import Room, PhotoGallery
from bookings.models import Booking
from .serializers import RoomSerializer, PhotoGallerySerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    @action(detail=False, methods=['post'])
    def check_availability(self, request):
        """ চেক করবে নির্দিষ্ট তারিখের মধ্যে কোনো রুম বুক করা হয়েছে কি না """
        check_in_date_str = request.data.get('check_in_date')
        check_out_date_str = request.data.get('check_out_date')

        if not check_in_date_str or not check_out_date_str:
            return Response({"error": "Check-in and check-out dates are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            check_in_date = parse_date(check_in_date_str)
            check_out_date = parse_date(check_out_date_str)

            if not check_in_date or not check_out_date:
                raise ValueError("Invalid date format")
        except (ValueError, TypeError):
            return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

        # বুকিং করা রুমগুলো খুঁজে বের করা হচ্ছে
        booked_rooms = Booking.objects.filter(
            status='Confirmed',
            check_in_date__lt=check_out_date,
            check_out_date__gt=check_in_date
        ).values_list('room_id', flat=True)

        # শুধুমাত্র available রুমগুলো দেখাবে
        available_rooms = Room.objects.exclude(id__in=booked_rooms).filter(is_available=True)

        serializer = self.get_serializer(available_rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def filter_by_room_type(self, request):
        """ নির্দিষ্ট `room_type` অনুযায়ী এবং `available` রুম ফিল্টার """
        room_type = request.query_params.get('room_type')

        if not room_type:
            return Response({"error": "Room type is required."}, status=status.HTTP_400_BAD_REQUEST)

        rooms = Room.objects.filter(room_type=room_type, is_available=True)
        serializer = self.get_serializer(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def filter_by_price(self, request):
        """ নির্দিষ্ট `price_per_night` অনুযায়ী এবং `available` রুম ফিল্টার """
        max_price = request.query_params.get('price_per_night')

        if not max_price:
            return Response({"error": "Max price is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            max_price = float(max_price)  # Ensure it's a number
        except ValueError:
            return Response({"error": "Invalid max_price. It should be a number."}, status=status.HTTP_400_BAD_REQUEST)

        # `price_per_night` ফিল্টার করা হচ্ছে
        rooms = Room.objects.filter(price_per_night__lte=max_price, is_available=True)
        
        if not rooms.exists():
            return Response({"message": "No available rooms found within this price range."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=False, methods=['get'])
    def filter_by_availability(self, request):
        """ শুধুমাত্র `available` রুম ফিল্টার """
        rooms = Room.objects.filter(is_available=True)
        serializer = self.get_serializer(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PhotoGalleryViewSet(viewsets.ModelViewSet):
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoGallerySerializer
