from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .room_manager import RoomManager
from .serializers import AvailableRoomPostSerializer,BookRoomPostSerializer

manager = RoomManager()

@api_view(["POST"])
def get_availablerooms(request):
    request_model = JSONParser().parse(request)
    serializer = AvailableRoomPostSerializer(data=request_model)

    if serializer.is_valid():
        
        numberOfPeople = serializer.data["numberofpeople"]
        startDate = serializer.data["between"][0]
        endDate = serializer.data["between"][1]
        
        return_data = manager.get_available_room(
            numberOfPeople,
            startDate,
            endDate
            
        )

        return_data = manager.serialize(return_data,startDate,endDate)

        return JsonResponse(
            {
               "options" : return_data
            },
            status=200
        )
    
    return JsonResponse({"success":False,"errors":serializer.errors},status=400)

@api_view(["POST"])
def bookroom(request):
    try:
        request_model = JSONParser().parse(request)
        serializer = BookRoomPostSerializer(data=request_model)

        if serializer.is_valid():
            manager.book_room(serializer.data["Roomid"],serializer.data["Numberofpeople"],serializer.data["Between"][0],serializer.data["Between"][1])
            return JsonResponse({"success": True},safe=False,status=201)
        return JsonResponse({"success":False,"errors": serializer.errors},status=400)
    except Exception as ex:
        return JsonResponse({"success":False,"error": str(ex)},status=400)

