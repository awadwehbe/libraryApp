from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)#CharField is used for small texts 
    author = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.title #self.title mean that the title of object itself (it is similar to this in java).

#book = Book(title="The Great Gatsby", author="F. Scott Fitzgerald") this is an instance of this model
#If you try to print or display this instance as a string, like this:
#print(book)
#The __str__ method will be called, and it will return the title attribute, so the output will be:
#The Great Gatsby