from django.db import models


# A model is the Python object which describes the database table's data. The list of fields need specified here,
# along with the associated types or parameters. By default all models have an auto-increment integer field called id
# which is automatically assigned and acts a primary key.

# might not need separate models for new book and review? Maybe one book model, but two different forms which use the
# same model?


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=80)
    rating = models.IntegerField(default=0)

    # Below is the Python equivalent of a toString() method.
    def __str__(self):
        return self.title


# class ReviewBook(models.Model):
#     rating = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.rating
