from django.contrib import admin

from .models import Book, UserRating

class BookInline(admin.TabularInline):
    model = Book
    extra = 3

class UserRatingInline(admin.TabularInline):
    model = UserRating
    extra = 3

class BookAdmin(admin.ModelAdmin):
    inlines = [UserRatingInline]

class UserRatingAdmin(admin.ModelAdmin):
    list_display = ('book', 'score', 'user')
    list_filter = ['score']
    search_fields = ['book__title']

admin.site.register(Book, BookAdmin)
admin.site.register(UserRating, UserRatingAdmin)