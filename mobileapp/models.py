from django.db import models
from PIL import Image
import os


class JobApplication(models.Model):
    MARITAL_STATUS_CHOICES = [
        ('single', 'Холост/Не замужем'),
        ('married', 'Женат/Замужем'),
        ('divorced', 'Разведён(а)'),
        ('widowed', 'Вдовец/Вдова'),
    ]

    full_name = models.CharField("ФИО", max_length=255)
    date_of_birth = models.DateField("Дата рождения")
    marital_status = models.CharField("Семейное положение", max_length=20, choices=MARITAL_STATUS_CHOICES)
    has_criminal_record = models.BooleanField("Судимость")
    address = models.CharField("Адрес проживания", max_length=255)
    mobile_number = models.CharField("Мобильный номер", max_length=20)
    photo = models.ImageField("Фото", upload_to='job_applications/photos/')
    passport_series = models.CharField("Серия паспорта", max_length=10)
    passport_number = models.CharField("Номер паспорта", max_length=20)
    passport_issued_by = models.CharField("Кем выдан паспорт", max_length=255)
    passport_issue_date = models.DateField("Дата выдачи паспорта")
    created_at = models.DateTimeField("Дата подачи", auto_now_add=True)

    class Meta:
        verbose_name = "Заявление на приём"
        verbose_name_plural = "Заявления на приём"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.photo and not self.photo.name.endswith('.webp'):
            img_path = self.photo.path
            img = Image.open(img_path)

            if img.mode != 'RGB':
                img = img.convert('RGB')

            webp_filename = os.path.splitext(self.photo.name)[0] + '.webp'
            webp_path = os.path.join(os.path.dirname(img_path), os.path.basename(webp_filename))
            img.save(webp_path, 'WEBP', quality=85)

            self.photo.name = webp_filename
            os.remove(img_path)

            super().save(update_fields=['photo'])

    def __str__(self):
        return self.full_name
