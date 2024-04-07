from rest_framework import serializers
from places.models import Place, Comment

class PlaceSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    address = serializers.CharField()
    image = serializers.ImageField()


    def validate(self, data):
        name = data.get('name')

        if len(name)<4:
            result = {
                "status":False,
                "message": "Name len is less than 4"
            }

            raise serializers.ValidationError(result)

        address = data.get('address')

        if address.isalpha():
            result = {
                "status": False,
                "message": "Address ichida sonlar ham ishtirok etishi lozim"
            }

            raise serializers.ValidationError(result)

        return data


    def create(self, validated_data):
        name = validated_data.get('name')
        description = validated_data.get('description')
        address = validated_data.get('address')
        image = validated_data.get('image')

        Place.objects.create(
            name=name,
            address=address,
            description=description,
            image=image
        )

        return validated_data


    
    

class CommentSerializer(serializers.Serializer):
    user=serializers.CharField()
    place=serializers.CharField()
    comment_text=serializers.CharField()
    star_given=serializers.IntegerField()

    def validate(self, data):
        
        star_given = data.get('star_given')

        if star_given < 0 and star_given > 5:
            raise serializers.ValidationError('star given must be  >1 and <5')

        return data