from rest_framework_json_api import serializers
from fullybooked.models import Book

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author', 'rating')
