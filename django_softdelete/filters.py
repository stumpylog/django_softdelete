from django.contrib.admin import SimpleListFilter


class SoftDeleteFilter(SimpleListFilter):
    title = 'is deleted'
    parameter_name = 'is_deleted'

    def lookups(self, request, model_admin):
        return (
            ('true', 'Deleted Softly'),
            ('false', 'Not Deleted'),
        )

    def queryset(self, request, queryset):
        value = {
            'true': False,
            'false': True,
        }[self.value() or 'false']
        return queryset.filter(deleted_at__isnull=value)
