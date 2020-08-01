from django.test import TestCase
from api.models import BookingHistory,Room
from api.room_manager import RoomManager

class RoomManagerTest(TestCase):
    room_list = [
        {
            "room_name" : "Room1",
            "capacity" : 8
        },
        {
            "room_name" : "Room2", #
            "capacity" : 3
        },
        {
            "room_name" : "Room3", # 
            "capacity" : 21
        },
        {
            "room_name" : "Room4",# 
            "capacity" : 5
        },
        {
            "room_name" : "Room5", # 
            "capacity" : 7
        },
        {
            "room_name" : "Room6", # 
            "capacity" : 2
        }] 
    test_cases_for_available_rooms = [
            {
                "numberofpeople" : 10,
                "between" : ["2018-05-11 09:10:00","2018-05-11 10:10:00"],
                "expected_room_name" : "Room3"
            },
            {
                "numberofpeople" : 3,
                "between" : ["2018-05-11 09:10:00","2018-05-11 10:10:00"],
                "expected_room_name" : "Room2"
            },
            {
                "numberofpeople" : 5,
                "between" : ["2018-05-11 09:10:00","2018-05-11 10:10:00"],
                "expected_room_name" : "Room4"
            },
            {
                "numberofpeople" : 6,
                "between" : ["2018-05-11 09:10:00","2018-05-11 10:10:00"],
                "expected_room_name" : "Room5"
            },
            {
                "numberofpeople" : 8,
                "between" : ["2018-05-11 09:10:00","2018-05-11 10:10:00"],
                "expected_room_name" : "Room1"
            }
        ]
    roommanager = None

    def setUp(self):
        self.roommanager = RoomManager()
        # Önce oda eklemeleri yapıcaz.
        for room in self.room_list:
            Room.objects.create(Name=room["room_name"],Capacity=room["capacity"])

    def test_available_rooms(self):
        
        for test in self.test_cases_for_available_rooms:
            self.assertEqual(
                self.roommanager.get_available_room(
                    test["numberofpeople"],
                    test["between"][0],
                    test["between"][1]
                )[0].Name,test["expected_room_name"]
            )

    def test_not_enough_capacity(self):
        # book_room için tekrar test yazmaya gerek yok
        
        # Capacity exception 
        room = Room.objects.filter(Capacity=5).first()

        with self.assertRaisesMessage(Exception,"Not enough capacity"):
            self.roommanager.check_if_room_available(
                room.id,
                10,
                "2018-05-11 09:10:00",
                "2018-05-11 10:10:00"
            )
    
    def test_room_is_occupied(self):
        
        # Önce bi kayıt oluşturalım, dolu olan zamanlar için kontrolünü yapalım

        test_room = Room.objects.create(Name="Test_Room",Capacity=5)

        self.roommanager.book_room(
            test_room.id,
            3,
            "2020-08-01 09:00:00",
            "2020-08-01 10:00:00"
        ) # Odayı rezerve ettikten sonra,

        with self.assertRaisesMessage(Exception,"Room not available"):
            self.roommanager.check_if_room_available(
                test_room.id,
                3,
                "2020-08-01 09:50:00",
                "2020-08-01 10:50:00"
            )





    
    
        
