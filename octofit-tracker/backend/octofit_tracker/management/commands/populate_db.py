from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True),
            User(name='Batman', email='batman@dc.com', team=dc, is_superhero=True),
        ]
        for user in users:
            user.save()

        # Create workouts
        workouts = [
            Workout(name='Web Swing', description='Swinging through the city'),
            Workout(name='Flight', description='Flying with armor'),
            Workout(name='Lasso Training', description='Lasso skills'),
            Workout(name='Stealth', description='Stealth and gadgets'),
        ]
        for workout in workouts:
            workout.save()

        # Assign suggested workouts
        workouts[0].suggested_for.add(users[0])  # Web Swing for Spider-Man
        workouts[1].suggested_for.add(users[1])  # Flight for Iron Man
        workouts[2].suggested_for.add(users[2])  # Lasso Training for Wonder Woman
        workouts[3].suggested_for.add(users[3])  # Stealth for Batman

        # Create activities
        Activity.objects.create(user=users[0], type='Swing', duration=30, date='2023-01-01')
        Activity.objects.create(user=users[1], type='Fly', duration=45, date='2023-01-02')
        Activity.objects.create(user=users[2], type='Lasso', duration=25, date='2023-01-03')
        Activity.objects.create(user=users[3], type='Stealth', duration=40, date='2023-01-04')

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
