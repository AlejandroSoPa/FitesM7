from django.core.management.base import BaseCommand
import random
from faker import Faker
from lloguer.models import Automobil

fake = Faker()

class Command(BaseCommand):
    help = 'Crea datos falsos de automóviles'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Iniciando creación de automóviles falsos...'))
        generate_automobils(10)
        self.stdout.write(self.style.SUCCESS('Creación de automóviles falsos completada.'))

def generate_automobils(count):
    for _ in range(count):
        marca = fake.company()
        model = fake.random_element(elements=('Sedan', 'SUV', 'Pickup', 'Hatchback'))
        matricula = generate_matricula()
        automobil = Automobil.objects.create(marca=marca, model=model, matricula=matricula)
        print(f"Automóvil creado: {automobil}")

def generate_matricula():
    letras = [chr(i) for i in range(65, 91)]  # Letras de la A a la Z
    numeros = [str(i) for i in range(10)]  # Números del 0 al 9
    matricula = ''.join(random.choices(letras, k=3)) + '-' + ''.join(random.choices(numeros, k=4)) + '-' + ''.join(random.choices(letras, k=2))
    return matricula

generate_automobils(200)
