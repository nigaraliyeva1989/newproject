from django.db import models


# Create your models here.

class GeneralSetting(models.Model):
    name = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='name test1',
        help_text="This is variable of the setting"

    )
    description = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='description',
        help_text=""
    )
    parameters = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='parameters',
        help_text=""

    )
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name='updated_date',
        help_text=""

    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='created_date',
        help_text=""

    )

    def __str__(self):
        return f'General Setting: {self.name}'

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Setting'
        ordering = ('name',)

    class ImageSetting(models.Model):
        name = models.CharField(
            default='',
            max_length=255,
            blank=True,
            verbose_name='name test1',
            help_text="This is variable of the setting"

        )
        description = models.CharField(
            default='',
            max_length=255,
            blank=True,
            verbose_name='description',
            help_text=""
        )
        file = models.ImageField(

            default='',
            verbose_name='Image',
            help_text='',
            blank=True,
            upload_to='images/',
        )
        updated_date = models.DateTimeField(
            blank=True,
            auto_now=True,
            verbose_name='updated_date',
            help_text=""

        )
        created_date = models.DateTimeField(
            blank=True,
            auto_now_add=True,
            verbose_name='created_date',
            help_text=''

        )

        def __str__(self):
            return f'ImageSetting{self.name}'

        class Meta:
            verbose_name = 'Image Setting'
            verbose_name_plural = 'Image Setting'
            ordering = ('name',)

