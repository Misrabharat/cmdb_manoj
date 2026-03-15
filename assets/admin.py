from django.contrib import admin
from .models import Asset, Assignment, Comment
from django.contrib import admin

admin.site.site_header = "CMDB Administration"
admin.site.site_title = "CMDB Admin Portal"
admin.site.index_title = "CMDB Management"

class AssetAdmin(admin.ModelAdmin):

    list_display = (
        'serial_number',
        'company',
        'computer_type',
        'brand',
        'model',
        'year',
        'opco_asset_tag',
        'invoice_number',
        'invoice_date',
        'state',
        'comments',
        'column1',
        'column2'
    )

    search_fields = (
        'serial_number',
        'company',
        'computer_type',
        'brand',
        'model',
        'opco_asset_tag',
        'invoice_number',
        'state'
    )

    list_filter = (
        'brand',
        'year',
        'state',
        'company'
    )


admin.site.register(Asset, AssetAdmin)
admin.site.register(Assignment)
admin.site.register(Comment)