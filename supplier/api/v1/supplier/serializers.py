from rest_framework import serializers

from supplier.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        # fields = '__all__'
        exclude = ['id', 'created_at', 'updated_at']
