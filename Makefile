PROJECT := example

SITE_ROOT := $(CURDIR)
DJANGO_ROOT = $(SITE_ROOT)/$(PROJECT)

PRODUCTION_SETTINGS = $(PROJECT).settings.settings.production
LOCAL_SETTINGS = $(PROJECT).settings.settings.local

PRODUCTION_POSTFIX := --settings=$(PRODUCTION_SETTINGS) --pythonpath=$(SITE_ROOT)
LOCAL_POSTFIX := --settings=$(LOCAL_SETTINGS) --pythonpath=$(SITE_ROOT)

.PHONY: clean collectstatic migrate install deploy cmd local lint

clean:
	@find . -name "*.pyc" -print0 | xargs -0 rm -rf
	@find . -name "__pycache__" -print0 | xargs -0 rm -rf
	@find . -name default.db -exec rm {} \;
	@find . -name whoosh_index -exec rm {} \;

collectstatic:
	$(PYTHONBIN) $(DJANGO_ROOT)/manage.py collectstatic -c --noinput $(PRODUCTION_POSTFIX)

migrate:
	@python $(DJANGO_ROOT)/manage.py syncdb --noinput $(PRODUCTION_POSTFIX)
	@python $(PYTHON_BIN) $(DJANGO_ROOT)/manage.py migrate $(PRODUCTION_POSTFIX)
	@python $(DJANGO_ROOT)/manage.py update_index $(PRODUCTION_POSTFIX)

install:
	@pip install -r requirements/production.txt

deploy: install migrate collectstatic

cmd:
	@python $(DJANGO_ROOT)/manage.py $(CMD) $(PRODUCTION_POSTFIX)

local.install:
	@pip install -r requirements/local.txt

local.runserver:
	@python $(DJANGO_ROOT)/manage.py runserver $(LOCAL_POSTFIX)

local.migrate:
	@python $(DJANGO_ROOT)/manage.py syncdb --noinput $(LOCAL_POSTFIX)
	@python $(DJANGO_ROOT)/manage.py migrate $(LOCAL_POSTFIX)
	@python $(DJANGO_ROOT)/manage.py rebuild_index --noinput $(LOCAL_POSTFIX)

local.cmd:
	python $(DJANGO_ROOT)/manage.py $(CMD) $(LOCAL_POSTFIX)

lint:
	@flake8 $(DJANGO_ROOT) --ignore=F403,E501
