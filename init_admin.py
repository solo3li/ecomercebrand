import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bervado_project.settings')
django.setup()

from django.contrib.auth.models import User

def run():
    print("Checking for superuser...")
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
        print("Superuser 'admin' created automatically.")
    else:
        print("Superuser already exists. Skipping.")

if __name__ == '__main__':
    run()
