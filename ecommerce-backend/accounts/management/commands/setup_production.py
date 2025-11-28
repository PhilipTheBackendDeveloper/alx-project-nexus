from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.core.management import call_command
from products.models import Product
import os

User = get_user_model()


class Command(BaseCommand):
    help = 'Set up production environment with superuser and sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write("=" * 60)
        self.stdout.write(self.style.SUCCESS('🚀 Production Setup Started'))
        self.stdout.write("=" * 60)
        
        # Create superuser
        self.create_superuser()
        
        # Load sample data
        self.load_sample_data()
        
        self.stdout.write("=" * 60)
        self.stdout.write(self.style.SUCCESS(' Production Setup Complete!'))
        self.stdout.write("=" * 60)
    
    def create_superuser(self):
        """Create superuser if it doesn't exist."""
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')
        
        if User.objects.filter(email=email).exists():
            self.stdout.write(
                self.style.WARNING(f'⏭  Superuser {email} already exists')
            )
            return
        
        try:
            User.objects.create_superuser(
                email=email,
                password=password,
                first_name='Admin',
                last_name='User'
            )
            self.stdout.write(
                self.style.SUCCESS(f' Superuser created: {email}')
            )
            self.stdout.write(
                self.style.WARNING(f'  Remember to change the password!')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f' Error creating superuser: {str(e)}')
            )
    
    def load_sample_data(self):
        """Load sample data if database is empty."""
        product_count = Product.objects.count()
        
        if product_count > 0:
            self.stdout.write(
                self.style.WARNING(
                    f'⏭  Database already has {product_count} products'
                )
            )
            return
        
        try:
            self.stdout.write(' Loading sample data...')
            call_command('seed_data')
            new_count = Product.objects.count()
            self.stdout.write(
                self.style.SUCCESS(f' {new_count} products created!')
            )
        except Exception as e:
            self.stdout.write(
                self.style.WARNING(f'  Could not load sample data: {str(e)}')
            )