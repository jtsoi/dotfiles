PYTHON_BIN := venv/bin

all: install

.PHONY: install clean lsetup check-aws-env pull-vars push-vars

check-aws-env:
ifndef AWS_ACCESS_KEY
	$(error AWS_ACCESS_KEY is undefined)
endif
ifndef AWS_SECRET_ACCESS_KEY
	$(error AWS_SECRET_ACCESS_KEY is undefined)
endif

install: venv

venv: $(PYTHON_BIN)/activate

$(PYTHON_BIN)/activate: requirements.txt
	test -d $(PYTHON_BIN) || virtualenv venv
	$(PYTHON_BIN)/pip2 install -Ur requirements.txt
	touch $(PYTHON_BIN)/activate

clean:
	rm -rf venv

pull-vars: check-aws-env
	$(PYTHON_BIN)/s3cmd sync --no-preserve --exclude=.gitignore s3://jtsoi-secrets/dotfiles/vars/ vars/

push-vars: check-aws-env
	$(PYTHON_BIN)/s3cmd sync --no-preserve --exclude=.gitignore vars/ s3://jtsoi-secrets/dotfiles/vars/

lsetup: venv
	$(PYTHON_BIN)/fab local setup
