all: build run

build:
	rm -rf dist
	java -jar /usr/local/lib/antlr-4.9.2-complete.jar \
	-Dlanguage=Python3 mus.g4 -visitor -o dist

run:
	python3 main.py