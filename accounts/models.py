from django.db import models

class Book(models.Model):
    # Fields for the book model
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)  # Could be a list of authors in a string (or a many-to-many relationship for multiple authors)
    genre = models.CharField(max_length=100)
    publisher = models.CharField(max_length=255)
    publication_date = models.DateField()
    language = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)  # Assuming you want to upload an image
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    format = models.CharField(max_length=50)  # e.g., Hardcover, Paperback, etc.

    def __str__(self):
        return self.title
