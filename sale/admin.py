from django.contrib import admin
from .models import Sale, SaleDetail
from django.contrib import messages
from django.utils.translation import ngettext

# Register your models here.


class SaleDetailInLine(admin.TabularInline):
    model = SaleDetail
    extra = 0


class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'status_label', 'patient', 'date')

    inlines = [
        SaleDetailInLine,
    ]
    actions = ['make_accepted', 'make_canceled']
    readonly_fields = ('date',)

    @admin.action(description='Marca venta/s seleccionadas como aceptada')
    def make_accepted(self, request, queryset):
        updated = queryset.update(status='A')
        self.message_user(request, ngettext(
            '%d La venta fue exitosamente marcada como aceptada.',
            '%d Las ventas fueron exitosamente marcadas como aceptadas.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Marca venta/s seleccionadas como cancelada')
    def make_canceled(self, request, queryset):
        updated = queryset.update(status='C')
        self.message_user(request, ngettext(
            '%d La venta fue exitosamente marcada como cancelada.',
            '%d Las ventas fueron exitosamente marcadas como cancelada.',
            updated,
        ) % updated, messages.SUCCESS)
        queryset.delete()


class SaleDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'sale', 'product', 'amount', 'price')


admin.site.register(Sale, SaleAdmin)
admin.site.register(SaleDetail, SaleDetailAdmin)

