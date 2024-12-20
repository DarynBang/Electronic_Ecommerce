import django_filters
from .models import *

class LaptopFilter(django_filters.FilterSet):
    # Dynamically get distinct values from the database
    cpu_choices = [(cpu, cpu) for cpu in Laptop.objects.values_list('cpu', flat=True).distinct()]
    cpu = django_filters.ChoiceFilter(choices=cpu_choices, label='CPU')

    ram_choices = [(ram, ram) for ram in Laptop.objects.values_list('ram', flat=True).distinct()]
    ram = django_filters.ChoiceFilter(choices=ram_choices, label='RAM')

    brand_choices = [(brand, brand) for brand in Laptop.objects.values_list('id__b_name', flat=True).distinct()]
    id__b_name = django_filters.ChoiceFilter(choices=brand_choices, label='Brand')

    gpu_choices = [(gpu, gpu) for gpu in Laptop.objects.values_list('graphic_card', flat=True).distinct()]
    graphic_card = django_filters.ChoiceFilter(choices=gpu_choices, label='Graphic Card')

    purpose_choices = [(purpose, purpose) for purpose in Laptop.objects.values_list('purpose', flat=True).distinct()]
    purpose = django_filters.ChoiceFilter(choices=purpose_choices, label='Purpose')

    status_choices = [('New', 'New'), ('2nd', '2nd')]
    id__status = django_filters.ChoiceFilter(choices=status_choices, label="Product Status")

    price = django_filters.RangeFilter(label='Price Range')

    order_by_price = django_filters.OrderingFilter(
        label="Sort Price by order",
        fields=(
            ('id__price', 'price'),  # Field in the Product model
        ),
        field_labels={
            'id__price': 'Price',
        },
        choices=[
            ('id__price', 'Ascending'),
            ('-id__price', 'Descending'),
        ]
    )


    class Meta:
        model = Laptop
        fields = ['id__b_name', 'cpu', 'ram', 'graphic_card', 'purpose', 'price', 'id__status']


class KeyboardFilter(django_filters.FilterSet):
    # Dynamically get distinct values from the database
    brand_choices = [(brand, brand) for brand in Keyboard.objects.values_list('id__b_name', flat=True).distinct()]
    id__b_name = django_filters.ChoiceFilter(choices=brand_choices, label='Brand')

    switch_choices = [(switch, switch) for switch in Keyboard.objects.values_list('switch_type', flat=True).distinct()]
    switch_type = django_filters.ChoiceFilter(choices=switch_choices, label='Switch Type')

    layout_choices = [(layout, layout) for layout in Keyboard.objects.values_list('layout', flat=True).distinct()]
    layout = django_filters.ChoiceFilter(choices=layout_choices, label='Layout')

    status_choices = [('New', 'New'), ('2nd', '2nd')]
    id__status = django_filters.ChoiceFilter(choices=status_choices, label="Product Status")

    price = django_filters.RangeFilter(label='Price Range')

    order_by_price = django_filters.OrderingFilter(
        label="Sort Price by order",
        fields=(
            ('id__price', 'price'),  # Field in the Product model
        ),
        field_labels={
            'id__price': 'Price',
        },
        choices=[
            ('id__price', 'Ascending'),
            ('-id__price', 'Descending'),
        ]
    )

    connection_choices = [
        (connection, connection)
        for connection in ElectronicAccessories.objects.values_list('connection', flat=True).distinct()
    ]
    connection = django_filters.ChoiceFilter(
        label="Connection Type",
        choices=connection_choices,
        method='filter_by_connection'
    )

    class Meta:
        model = Laptop
        fields = ['id__b_name', 'switch_type', 'layout', 'price', 'id__status', 'connection']


    def filter_by_connection(self, queryset, name, value):
        # Filter keyboards based on connection type from ElectronicAccessories
        accessory_ids = ElectronicAccessories.objects.filter(connection=value).values_list('id', flat=True)
        return queryset.filter(id__id__in=accessory_ids)


class MouseFilter(django_filters.FilterSet):
    # Dynamically get distinct values from the database
    brand_choices = [(brand, brand) for brand in Mouse.objects.values_list('id__b_name', flat=True).distinct()]
    id__b_name = django_filters.ChoiceFilter(choices=brand_choices, label='Brand')

    led_choices = [(led, led) for led in Mouse.objects.values_list('led_color', flat=True).distinct()]
    led_color = django_filters.ChoiceFilter(choices=led_choices, label='LED Color')

    dpi = django_filters.RangeFilter(label='DPI Range')

    status_choices = [('New', 'New'), ('2nd', '2nd')]
    id__status = django_filters.ChoiceFilter(choices=status_choices, label="Product Status")

    price = django_filters.RangeFilter(label='Price Range')

    order_by_price = django_filters.OrderingFilter(
        label="Sort Price by order",
        fields=(
            ('id__price', 'price'),  # Field in the Product model
        ),
        field_labels={
            'id__price': 'Price',
        },
        choices=[
            ('id__price', 'Ascending'),
            ('-id__price', 'Descending'),
        ]
    )

    connection_choices = [
        (connection, connection)
        for connection in ElectronicAccessories.objects.values_list('connection', flat=True).distinct()
    ]
    connection = django_filters.ChoiceFilter(
        label="Connection Type",
        choices=connection_choices,
        method='filter_by_connection'
    )

    class Meta:
        model = Laptop
        fields = ['id__b_name', 'led_color', 'dpi', 'price', 'id__status', 'connection']

    def filter_by_connection(self, queryset, name, value):
        accessory_ids = ElectronicAccessories.objects.filter(connection=value).values_list('id', flat=True)
        return queryset.filter(id__id__in=accessory_ids)


class HeadphoneFilter(django_filters.FilterSet):
    # Dynamically get distinct values from the database
    brand_choices = [(brand, brand) for brand in Headphone.objects.values_list('id__b_name', flat=True).distinct()]
    id__b_name = django_filters.ChoiceFilter(choices=brand_choices, label='Brand')

    type_choices = [(type, type) for type in Headphone.objects.values_list('type', flat=True).distinct()]
    type = django_filters.ChoiceFilter(choices=type_choices, label='Type')

    status_choices = [('New', 'New'), ('2nd', '2nd')]
    id__status = django_filters.ChoiceFilter(choices=status_choices, label="Product Status")

    price = django_filters.RangeFilter(label='Price Range')

    order_by_price = django_filters.OrderingFilter(
        label="Sort Price by order",
        fields=(
            ('id__price', 'price'),  # Field in the Product model
        ),
        field_labels={
            'id__price': 'Price',
        },
        choices=[
            ('id__price', 'Ascending'),
            ('-id__price', 'Descending'),
        ]
    )

    connection_choices = [
        (connection, connection)
        for connection in ElectronicAccessories.objects.values_list('connection', flat=True).distinct()
    ]
    connection = django_filters.ChoiceFilter(
        label="Connection Type",
        choices=connection_choices,
        method='filter_by_connection'
    )

    class Meta:
        model = Laptop
        fields = ['id__b_name', 'type', 'price', 'id__status', 'connection']

    def filter_by_connection(self, queryset, name, value):
        accessory_ids = ElectronicAccessories.objects.filter(connection=value).values_list('id', flat=True)
        return queryset.filter(id__id__in=accessory_ids)