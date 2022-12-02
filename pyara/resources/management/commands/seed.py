import requests
from django.core.management.base import BaseCommand
from ...models import Quote


def get_quote():
    url = 'https://programming-quotes-api.herokuapp.com/Quotes/random'
    r = requests.get(url, headers={'Content-Type':
                                       'application/json'})
    quote = r.json()
    return quote


def seed_quote():
    random_quote = get_quote()
    quote = Quote(
        author=random_quote["author"],
        en=random_quote["en"],
    )
    quote.save()


def clear_data():
    Quote.objects.all().delete()


class Command(BaseCommand):
    def handle(self, *args, **options):
        seed_quote()
#        clear_data()
        print("completed")
