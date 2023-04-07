from rest_framework import serializers

from comment.models import Comments


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comments
        fields = '__all__'


# class UserCommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comments
#         fields = ('id', 'body', 'film', 'created_at')
#
#     def to_representation(self, instance):
#         repr = super().to_representation(instance)
#         repr['film_title'] = instance.film.title
#         return repr