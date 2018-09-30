PYTHON_BIN := .venv/bin

all: install

.PHONY: install clean venv

install: venv

venv: $(PYTHON_BIN)/activate

$(PYTHON_BIN)/activate: requirements.txt
	sudo pip3 install virtualenv
	test -d $(PYTHON_BIN) || virtualenv .venv
	$(PYTHON_BIN)/pip install -Ur requirements.txt
	touch $(PYTHON_BIN)/activate

clean:
	rm -rf .venv
