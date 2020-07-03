SuperUser:
marcus | test@test.com | dummy@test.com | becky@test.com
P@55w0rd1


todo: Add templates, base template etc
Add Log in functionality


Migrations: 
python manage.py makemigrations tenant
python manage.py makemigrations portfolios
python manage.py makemigrations properties

Relationship query:
p = Portfolio.objects.get(pk=1)
p.property_set.all()