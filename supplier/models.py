import uuid

from django.core.validators import RegexValidator
from django.db import models
from django.core.exceptions import ValidationError

from supplier.choices import STATE_CHOICES


def validate_cnpj(value):
    if len(value) != 14 or not value.isdigit():
        raise ValidationError("CNPJ must have 14 digits.")


def validate_image_size(image):
    max_size_kb = 500
    if image.size > max_size_kb * 1024:
        raise ValidationError(f"The maximum allowed size is {max_size_kb} KB")


class Supplier(models.Model):
    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    cnpj = models.CharField(
        "CNPJ",
        max_length=14,
        blank=True, null=True,
        validators=[
            validate_cnpj,
            RegexValidator(r'^\d{14}$', 'CNPJ must be 14 digits.')
        ]
    )

    name = models.CharField("Nome", max_length=255)
    logo = models.ImageField("Logo", upload_to='logos/', blank=True, validators=[validate_image_size])
    origin_state = models.CharField("Estado de origem", max_length=2, choices=STATE_CHOICES)
    cost_per_kwh = models.DecimalField("Custo por kWh", max_digits=10, decimal_places=2)
    minimum_kwh_limit = models.PositiveIntegerField("limite mínimo de kWh")
    total_clients = models.PositiveIntegerField("Total de clientes")
    average_rating = models.DecimalField('Avaliação média dos clientes', max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name
