from .models import BookingHistory, Room
import datetime 

class RoomManager():
    def __init__(self):
        pass

    def check_if_room_available(
        self,
        room_id,
        number_of_people,
        start_date,
        end_date
        ):
        """
        check_if_room_available() -> Bool \n
        Kayıttan öncede kullanılmak üzere odanın müsait olup olmaması durumunu 
        kontrol eder.
        """
        
        room = Room.objects.get(pk=room_id) # Seçilen oda 
        
        if room.Capacity < number_of_people:
            raise Exception("Not enough capacity")        
            
        
        # başlangıç zamanı <= bitiş zamanı, bitiş zamanı >= başlangıç zamanı, 
        # 9.10 - 11.00
        # 9.20 - 10.10

        
        history_check = BookingHistory.objects.filter(
            StartDate__lte=end_date,
            EndDate__gte=start_date,
            Room__id=room_id
            ).exists() # varsa, oda dolu demektir.

        if history_check:
            raise Exception("Room not available")

        return True
        

    def get_available_room(self,number_of_people,start_date,end_date) :

        """
        Geriye dönen listede, 
        en uygun olandan en az uygun olana kadar sıralama yapılacaktır.
        """


        # NumOfPeople >= Capacity

        available_room_list = Room.objects.filter(Capacity__gte=number_of_people)


        # Başlangıç ve bitiş tarihlerinde dolu olan odalar 

        unavailable_room_list = BookingHistory.objects.filter(
            StartDate__lte=end_date,
            EndDate__gte = start_date)

        
        # exclude edip, desc capacity şeklinde sıraladım burdan sonra extend edilebilir
        # limitasyon getirilebilir

        available_room_list = available_room_list.exclude(id__in = [history.Room_id for history in unavailable_room_list])


        return available_room_list.order_by("Capacity")

    def serialize(self,r_data,startDate,endDate):
        return_data = []

        for data in r_data:
            return_data.append(
                {
                    "Roomid" : data.id,
                    "RoomName" : data.Name,
                    "Between" : [startDate,endDate] 
                }
            )


        return return_data

        
    def book_room(self,room_id,number_of_people,start_date,end_date):
        """
        book_room() -> None \n
        Veritabanına yeni kayıt oluşturur.
        """
        self.check_if_room_available(
            room_id,
            number_of_people,
            start_date,
            end_date) # uygun değilse hata vericek. viewdan handle edeceğiz.

        new_record = BookingHistory(
            Room_id=room_id,
            StartDate=start_date,
            EndDate=end_date,
            NumberOfPeople=number_of_people
            )

        new_record.save()






        
    







