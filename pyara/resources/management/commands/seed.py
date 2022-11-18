import requests
from django.core.management.base import BaseCommand
from ...models import Fish


def get_fishs():
  url = 'https://www.fishwatch.gov/api/species'
  r = requests.get(url, headers={'Content-Type':
    'application/json'})
  fish = r.json()
  return fish

def seed_fish():
  for i in get_fishs():
  fish = Fish(
    name=i["Species Name"],
    scientific_name=i["Scientific Name"],
  )
  fish.save()

  def clear_data():
      Fish.objects.all().delete()


class Command(BaseCommand):
  def handle(self, *args, **options):
    seed_fish()
    # clear_data()
    print("completed")