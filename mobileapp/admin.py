from django.contrib import admin
from django.utils.html import format_html
from .models import JobApplication


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'date_of_birth',
        'marital_status',
        'has_criminal_record',
        'passport_series',
        'passport_number',
        'address',
        'created_at',
        'photo_tag',
    )
    readonly_fields = ('photo_tag', 'created_at')
    search_fields = ('full_name', 'passport_number', 'address')
    list_filter = ('marital_status', 'has_criminal_record', 'created_at')

    fieldsets = (
        ("Личная информация", {
            'fields': (
                'full_name',
                'date_of_birth',
                'marital_status',
                'has_criminal_record',
                'address',
                'mobile_number',
                'photo',
                'photo_tag',
            )
        }),
        ("Паспортные данные", {
            'fields': (
                'passport_series',
                'passport_number',
                'passport_issued_by',
                'passport_issue_date',
            )
        }),
        ("Системные данные", {
            'fields': (
                'created_at',
            )
        }),
    )

    def photo_tag(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="100" height="100" style="object-fit: cover; border-radius: 8px; transform: rotate(270deg);" />',
                obj.photo.url
            )
        return "-"

    photo_tag.short_description = "Фото"
