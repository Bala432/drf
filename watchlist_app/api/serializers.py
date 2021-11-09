from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Reviews

#Implementing ModelSerializer
class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewsSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields = "__all__"

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True,read_only=True)
    class Meta:
        model = StreamPlatform
        fields = "__all__"


# def name_length(value):
#         if len(value) < 2:
#             raise serializers.ValidationError("name is too short")
#         else:
#             return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField() 

#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self,instance,validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance

    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("name is too short")
    #     else:
    #         return value

    # def validate(self, data):
    #     if data['name'] != data['description']:
    #         return data
    #     else:
    #         raise serializers.ValidationError("Name and Description are same")


