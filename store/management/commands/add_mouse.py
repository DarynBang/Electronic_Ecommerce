import pandas as pd
from django.core.management.base import BaseCommand
from store.models import *

class Command(BaseCommand):
    help = "Command is working as intended"

    def handle(self, *args, **options):
        file_path = r'C:\Users\Daryn Bang\Desktop\database_data\mouse_data.xlsx'
        df = pd.read_excel(file_path, sheet_name="Sheet1")

        PURPOSE_CHOICES = {
            'Gaming': 'Gaming',
            'Office': 'Office'
        }

        # Iterate over each row and create a keyboard instance
        for _, row in df.iterrows():
            try:
                # Retrieve or create the keyboardBrand instance
                brand_instance, created = MouseBrand.objects.get_or_create(mouse_brand=row['Brand'])
                led_instance, created = MOUSE_LED.objects.get_or_create(led=row['LED'])
                connection_instance, created = Connection.objects.get_or_create(connection=row['Connection'])
                purpose_value = PURPOSE_CHOICES.get(row['Purpose'])

                mouse = Mouse(
                    name=row['Title'],
                    price=row['Price'],
                    dpi=row['DPI'],
                    status=True,
                    brand=brand_instance,  # Use the instance instead of the string
                    LED=led_instance,
                    connection=connection_instance,
                    purpose=purpose_value,
                    image_link=row['image_link']
                )
                mouse.save()
                self.stdout.write(self.style.SUCCESS(f"Mouse '{mouse}' created successfully."))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error creating mouse: {e}"))

        self.stdout.write(self.style.SUCCESS("All mice imported successfully."))

