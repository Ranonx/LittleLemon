from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


#TestCase class
class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Pizza", price=100, inventory=50)
        Menu.objects.create(title="Burger", price=50, inventory=30)

    def test_getall(self):
       # Get API response
        url = reverse('menuitem-list')  # actual name of your Menu list view URL
        response = self.client.get(url)

        # Get data from db
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the serialized data equals the response data
        self.assertEqual(response.data, serializer.data)