from django.contrib import admin
from .models import User
from .models import deletetable
from .models import Suggestion
from .models import modification

admin.site.register(User)
admin.site.register(modification)
admin.site.register(Suggestion)
admin.site.register(deletetable)
# Register your models here.
