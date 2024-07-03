from django.contrib import admin
from .models import Flan, ContactForm, NewsletterForm
# Register your models here.

admin.site.register(Flan)
admin.site.register(NewsletterForm)
admin.site.register(ContactForm)