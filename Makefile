GOCMD=go
GOBUILD=$(GOCMD) build
BINARY_NAME=dddsp.out

all: build
build:
	$(GOBUILD) -o $(BINARY_NAME) -v
