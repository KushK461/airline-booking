from rest_framework import serializers
from .models import Flight, Passenger

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id', 'flight_number', 'departure', 'arrival', 'origin', 'destination', 'capacity']

class PassengerSerializer(serializers.ModelSerializer):
    flight = FlightSerializer(read_only=True)

    class Meta:
        model = Passenger
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'flight']
