from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Limpar dados existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Adicionar dados de teste
        user1 = User.objects.create(username='john_doe', email='john@example.com', password='password123')
        user2 = User.objects.create(username='jane_doe', email='jane@example.com', password='password123')

        team1 = Team.objects.create(name='Team Alpha')
        team1.members.add(user1, user2)

        # Corrigir a criação de atividades para usar timedelta
        Activity.objects.create(user=user1, activity_type='Running', duration=timedelta(minutes=30))
        Activity.objects.create(user=user2, activity_type='Cycling', duration=timedelta(hours=1))

        Leaderboard.objects.create(user=user1, score=100)
        Leaderboard.objects.create(user=user2, score=150)

        Workout.objects.create(name='Morning Yoga', description='A relaxing yoga session to start the day.')
        Workout.objects.create(name='HIIT', description='High-intensity interval training for advanced users.')

        # Adicionar mais dados de teste para cobrir diferentes cenários
        user3 = User.objects.create(username='alice_smith', email='alice@example.com', password='password123')
        user4 = User.objects.create(username='bob_brown', email='bob@example.com', password='password123')

        team2 = Team.objects.create(name='Team Beta')
        team2.members.add(user3, user4)

        Activity.objects.create(user=user3, activity_type='Swimming', duration=timedelta(minutes=45))
        Activity.objects.create(user=user4, activity_type='Hiking', duration=timedelta(hours=2))

        Leaderboard.objects.create(user=user3, score=200)
        Leaderboard.objects.create(user=user4, score=250)

        Workout.objects.create(name='Evening Stretch', description='A calming stretch routine for the evening.')
        Workout.objects.create(name='Cardio Blast', description='A high-energy cardio workout for all levels.')

        # Adicionar mais dados de teste com base no exemplo
        users = [
            User.objects.create(username='thundergod', email='thundergod@mhigh.edu', password='thundergodpassword'),
            User.objects.create(username='metalgeek', email='metalgeek@mhigh.edu', password='metalgeekpassword'),
            User.objects.create(username='zerocool', email='zerocool@mhigh.edu', password='zerocoolpassword'),
            User.objects.create(username='crashoverride', email='crashoverride@mhigh.edu', password='crashoverridepassword'),
            User.objects.create(username='sleeptoken', email='sleeptoken@mhigh.edu', password='sleeptokenpassword'),
        ]

        activities = [
            Activity.objects.create(user=users[0], activity_type='Cycling', duration=timedelta(hours=1)),
            Activity.objects.create(user=users[1], activity_type='Crossfit', duration=timedelta(hours=2)),
            Activity.objects.create(user=users[2], activity_type='Running', duration=timedelta(hours=1, minutes=30)),
            Activity.objects.create(user=users[3], activity_type='Strength', duration=timedelta(minutes=30)),
            Activity.objects.create(user=users[4], activity_type='Swimming', duration=timedelta(hours=1, minutes=15)),
        ]

        leaderboard_entries = [
            Leaderboard.objects.create(user=users[0], score=100),
            Leaderboard.objects.create(user=users[1], score=90),
            Leaderboard.objects.create(user=users[2], score=95),
            Leaderboard.objects.create(user=users[3], score=85),
            Leaderboard.objects.create(user=users[4], score=80),
        ]

        workouts = [
            Workout.objects.create(name='Cycling Training', description='Training for a road cycling event'),
            Workout.objects.create(name='Crossfit', description='Training for a crossfit competition'),
            Workout.objects.create(name='Running Training', description='Training for a marathon'),
            Workout.objects.create(name='Strength Training', description='Training for strength'),
            Workout.objects.create(name='Swimming Training', description='Training for a swimming competition'),
        ]

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
