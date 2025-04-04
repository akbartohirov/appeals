from django.db import models

class Appeal(models.Model):
    ORG_CHOICES = [
        ('OrgA', 'Organization A'),
        ('OrgB', 'Organization B'),
    ]

    APPOINTMENT_TYPE_CHOICES = [
        ('Type1', 'Type 1'),
        ('Type2', 'Type 2'),
    ]

    CURRENCY_CHOICES = [
        ('UZS', 'UZS'),
        ('USD', 'USD'),
        ('EUR', 'EUR'),
    ]

    name = models.CharField(max_length=255)
    appeal_org = models.CharField(max_length=100, choices=ORG_CHOICES)
    appointment = models.CharField(max_length=255)
    appointment_type = models.CharField(max_length=100, choices=APPOINTMENT_TYPE_CHOICES)
    client_code = models.CharField(max_length=100)
    client_card = models.CharField(max_length=100)
    drop_card = models.CharField(max_length=100)  # <-- Новое поле
    appeal_date = models.DateField()
    responsible = models.CharField(max_length=255)
    controller = models.CharField(max_length=255)
    damage = models.IntegerField()
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    status = models.CharField(max_length=100)
    measures = models.TextField()

    def __str__(self):
        return f"{self.name} — {self.appeal_date}"


class AppealFile(models.Model):
    appeal = models.ForeignKey('Appeal', on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='appeal_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

