SuperUser:
marcus
P@55w0rd1


todo: Add templates, base template etc



Migrations: 
python manage.py makemigrations tenant
python manage.py makemigrations portfolios
python manage.py makemigrations properties

Relationship query:
p = Portfolio.objects.get(pk=1)
p.property_set.all()