.PHONY: freeze requirements requirements-upgrade syncdb run run-public makemessages compilemessages

project_name=students

requirements:
	-@echo "### Installing requirements"
	-@pip install -r requirements.txt

requirements-upgrade:
	-@echo "### Upgrading requirements"
	-@pip freeze | cut -d = -f 1 | xargs pip install -U

freeze:
	-@echo "### Freezing python packages to requirements.txt"
	-@pip freeze > requirements.txt

syncdb:
	-@echo "### Creating database tables and loading fixtures"
	@PYTHONPATH=$(PYTHONPATH):. DJANGO_SETTINGS_MODULE=$(project_name).settings python manage.py syncdb --noinput
	@PYTHONPATH=$(PYTHONPATH):. DJANGO_SETTINGS_MODULE=$(project_name).settings python manage.py loaddata fixtures/*

run:
	@PYTHONPATH=$(PYTHONPATH):. DJANGO_SETTINGS_MODULE=$(project_name).settings python manage.py runserver

run-public:
	@PYTHONPATH=$(PYTHONPATH):. DJANGO_SETTINGS_MODULE=$(project_name).settings python manage.py runserver 0.0.0.0:8000

makemessages:
	-@django-admin.py makemessages --locale=en --extension=html,txt
	-@django-admin.py makemessages --locale=ru --extension=html,txt

compilemessages:
	-@django-admin.py compilemessages

cloc:
	-@echo "### Counting lines of code within the project"
	-@echo "# Total:" ; find . -iregex '.*\.py\|.*\.js\|.*\.html\|.*\.css' -type f -exec cat {} + | wc -l
	-@echo "# Python:" ; find . -name '*.py' -type f -exec cat {} + | wc -l
	-@echo "# JavaScript:" ; find . -name '*.js' -type f -exec cat {} + | wc -l
	-@echo "# HTML:" ; find . -name '*.html' -type f -exec cat {} + | wc -l
	-@echo "# CSS:" ; find . -name '*.css' -type f -exec cat {} + | wc -l

clean:
	-@echo "### Cleaning *.pyc files "
	-@rm *.pyc
	-@find . -name '*.pyc' -exec rm -f {} \;
