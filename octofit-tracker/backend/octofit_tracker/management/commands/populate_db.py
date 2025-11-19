from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel', is_superhero=True)
        captain = User.objects.create(email='captain@marvel.com', name='Captain America', team='Marvel', is_superhero=True)
        batman = User.objects.create(email='batman@dc.com', name='Batman', team='DC', is_superhero=True)
        superman = User.objects.create(email='superman@dc.com', name='Superman', team='DC', is_superhero=True)

        # Activities
        Activity.objects.create(user='Iron Man', type='Running', duration=30)
        Activity.objects.create(user='Captain America', type='Cycling', duration=45)
        Activity.objects.create(user='Batman', type='Swimming', duration=25)
        Activity.objects.create(user='Superman', type='Flying', duration=60)

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=85)

        # Workouts
        Workout.objects.create(name='Super Strength', difficulty='Hard')
        Workout.objects.create(name='Agility Training', difficulty='Medium')
        Workout.objects.create(name='Flight Practice', difficulty='Easy')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
