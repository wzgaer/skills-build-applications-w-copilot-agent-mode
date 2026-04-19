from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as octo_models

from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        User = get_user_model()
        User.objects.all().delete()
        Team = octo_models.Team
        Team.objects.all().delete()
        Activity = octo_models.Activity
        Activity.objects.all().delete()
        Leaderboard = octo_models.Leaderboard
        Leaderboard.objects.all().delete()
        Workout = octo_models.Workout
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', team=marvel)
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='pass', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='pass', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='pass', team=dc)

        # Create Activities
        Activity.objects.create(user=ironman, type='run', duration=30, distance=5)
        Activity.objects.create(user=captain, type='cycle', duration=60, distance=20)
        Activity.objects.create(user=batman, type='swim', duration=45, distance=2)
        Activity.objects.create(user=superman, type='run', duration=50, distance=10)

        # Create Workouts
        Workout.objects.create(name='Morning Cardio', description='Run and cycle combo')
        Workout.objects.create(name='Strength', description='Pushups and squats')

        # Create Leaderboard
        Leaderboard.objects.create(user=ironman, score=100)
        Leaderboard.objects.create(user=captain, score=90)
        Leaderboard.objects.create(user=batman, score=95)
        Leaderboard.objects.create(user=superman, score=98)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
