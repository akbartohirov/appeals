import openpyxl
from django.http import HttpResponse
from django.contrib import admin
from .models import Appeal, AppealFile


def export_to_excel(modeladmin, request, queryset):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Обращения"

    # Заголовки
    headers = [
        "ID", "Name", "Appeal Org", "Appointment", "Appointment Type",
        "Client Code", "Client Card", "Drop Card", "Appeal Date",
        "Responsible", "Controller", "Damage", "Currency", "Status", "Measures"
    ]
    ws.append(headers)

    for obj in queryset:
        ws.append([
            obj.id,
            obj.name,
            obj.appeal_org,
            obj.appointment,
            obj.appointment_type,
            obj.client_code,
            obj.client_card,
            obj.drop_card,
            obj.appeal_date.strftime('%Y-%m-%d'),
            obj.responsible,
            obj.controller,
            obj.damage,
            obj.currency,
            obj.status,
            obj.measures,
        ])

    # Возврат Excel-файла
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = "attachment; filename=appeals_export.xlsx"
    wb.save(response)
    return response

export_to_excel.short_description = "📥 Скачать выбранные обращения в Excel"


class AppealFileInline(admin.TabularInline):
    model = AppealFile
    extra = 1
    fields = ['file', 'uploaded_at']
    readonly_fields = ['uploaded_at']


@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'appeal_date', 'status', 'currency', 'damage']
    search_fields = ['name', 'client_code', 'client_card']
    list_filter = ['appeal_org', 'appointment_type', 'status', 'currency']
    inlines = [AppealFileInline]
    actions = [export_to_excel]  # <-- тут добавляем кнопку

@admin.register(AppealFile)
class AppealFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'appeal', 'file', 'uploaded_at']
    readonly_fields = ['uploaded_at']