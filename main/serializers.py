from rest_framework import serializers
from .models import Film, UserFilmRelation
from comment.serializers import CommentSerializer


class FilmListSerializer(serializers.ModelSerializer):
    # annotated_likes = serializers.IntegerField(read_only=True)
    rating = serializers.DecimalField(max_digits=3, decimal_places=2, read_only=True)

    class Meta:
        model = Film
        fields = ('id', 'title', 'image', 'year', 'rating', )




class FilmDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'


    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['comments count'] = instance.comments.count()
        repr['comments'] = CommentSerializer(instance=instance.comments.all(), many=True).data

        return repr


class UserFilmRelationSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserFilmRelation
        fields = '__all__'

class ChangeSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserFilmRelation
        fields = '__all__'











































































