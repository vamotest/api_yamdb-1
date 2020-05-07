from rest_framework import serializers

from .models import User, Category, Genre, Title


class SendCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class CheckConfirmationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    confirmation_code = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('first_name', 'last_name', 'username', 'bio', 'email', 'role',)
        model = User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug',)
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug',)
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    # name = serializers.SlugRelatedField(slug_field='slug', many=True, queryset=Genre.objects.all())
    # category = serializers.SlugRelatedField(slug_field='slug', queryset=Category.objects.all())
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True, required=False, allow_null=True)

    class Meta:
        #fields = ('id', 'name', 'year', 'genre', 'category', 'description',)
        fields = '__all__'
        model = Title
