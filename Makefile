# var declarations
DEPS?=""

# const declarations
VENV="env"
PIP="./${VENV}/bin/pip"
PY="./${VENV}/bin/python3"


# targets
all:
	# do somthing

test:
	# run test paln

clean:
	# clean something


config: requirements.txt
	python3 -m venv ${VENV}
	${PIP} install -r requirements.txt


add_dep:
	${PIP} install ${DEPS}
	${PIP} freeze > ./requirements.txt