from rest_framework import serializers
from . import models 
class RoomSerializer(serializers.Serializer):
    class Meta:
        model = models.Room


def validate_between(value):
    if len(value) != 2:
        raise serializers.ValidationError("Between field not valid!")
        
    value.sort() # startdate,enddate sıkıntı olmaması için. 
    #Aslında uygun değilse, direk validation error atmak daha mantıklı

    return value


class AvailableRoomPostSerializer(serializers.Serializer):
    numberofpeople = serializers.IntegerField(required=True)
    between = serializers.ListField(child=serializers.DateTimeField())
    
    def validate_between(self,value):
        return validate_between(value)
        

class BookRoomPostSerializer(serializers.Serializer):
    Roomid = serializers.IntegerField(required=True)
    Numberofpeople = serializers.IntegerField(required=True)
    Between = serializers.ListField(child=serializers.DateTimeField())

    def validate_Between(self,value):
        return validate_between(value)


