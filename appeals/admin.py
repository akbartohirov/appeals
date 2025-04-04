from django.contrib import admin
from .models import Appeal, AppealFile

# Inline для файлов
class AppealFileInline(admin.TabularInline):
    model = AppealFile
    extra = 1
    fields = ['file', 'uploaded_at']
    readonly_fields = ['uploaded_at']

# Админка для обращений
@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'appeal_date', 'status', 'currency', 'damage']
    search_fields = ['name', 'client_code', 'client_card']
    list_filter = ['appeal_org', 'appointment_type', 'status', 'currency']
    inlines = [AppealFileInline]

# Отдельная регистрация файлов (если нужно)
@admin.register(AppealFile)
class AppealFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'appeal', 'file', 'uploaded_at']
    readonly_fields = ['uploaded_at']
