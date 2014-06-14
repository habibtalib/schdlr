from datetime import timedelta

from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError

from django.contrib.auth.models import User

from schedule.models import *


class Command(BaseCommand):

    def handle(self, *args, **options):
        admin, _ = User.objects.get_or_create(username='admin', is_superuser=True, is_staff=True)
        admin.set_password('admin')
        admin.save()

        for i in range (5):
            Location.objects.get_or_create(
                location_name='Location {}'.format(i),
                square_footage=100,
                capacity=100
            )

        resource = Resource.objects.get_or_create(
            is_fixed=True,
            resource_type="speakers",
            description="Bose 5.1",
            location=Location.objects.get(location_name='Location 1')
        )

        _1 = timezone.now()
        _2 = timezone.now() + timedelta(hours=1)
        _3 = timezone.now() + timedelta(hours=5)
        _4 = timezone.now() + timedelta(hours=6)

        dates = [_1, _2, _3, _4]

        for i, date in enumerate(dates):
            event = Event.objects.create(
                event_name='Testing Event {}'.format(i),
                setup_start=date,
                setup_end=timezone.now(),
                event_start=timezone.now(),
                event_end=timezone.now(),
                teardown_start=timezone.now(),
                teardown_end=date + timedelta(hours=1),
                status='pending',
                visibility='public',
                location=Location.objects.get(location_name='Location 1'),
                contact_name='John Richard',
                contact_email='john.richard@gmail.com'
            )
