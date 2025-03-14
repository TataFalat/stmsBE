from rest_framework import serializers
from .models import Order, Waypoint

class WaypointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waypoint
        fields = ['location', 'street', 'number', 'postalCode', 'city', 'country', 'type']

class OrderSerializer(serializers.ModelSerializer):
    waypoints = WaypointSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ['id', 'number', 'customerName', 'date', 'waypoints']
    
    def create(self, validated_data):
        waypoints = validated_data.pop('waypoints')
        order = Order.objects.create(**validated_data)
        for waypoint in waypoints:
            Waypoint.objects.create(order=order, **waypoint)
        return order
