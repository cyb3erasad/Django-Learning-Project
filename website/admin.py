from django.contrib import admin
from .models import ChaiVarity, ChaiReview, ChaiStore, ChaiCertificate

# Register your models here.

class ChaiReviewInLine(admin.TabularInline):
    model = ChaiReview
    extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'chai_type', 'date_add')
    inlines = [ChaiReviewInLine]


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties', )

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number')


admin.site.register(ChaiVarity, ChaiVarietyAdmin)
admin.site.register(ChaiReview)
admin.site.register(ChaiStore, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)