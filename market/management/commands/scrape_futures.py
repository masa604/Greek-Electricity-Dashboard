from django.core.management.base import BaseCommand
from market.scraper import scrape_enex_data

class Command(BaseCommand):
    help = 'Raspa dados de futuros do site da ENEX Group'

    def handle(self, *args, **options):
        if scrape_enex_data():
            self.stdout.write(self.style.SUCCESS('Dados raspados com sucesso!'))
        else:
            self.stdout.write(self.style.ERROR('Falha ao raspar dados.'))