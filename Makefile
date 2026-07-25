
src	=	$(wildcard *.py)

name  =		103cipher

all: $(name)

$(name):	$(src)
	    cp main.py $(name)
		chmod +x $(name)

clean:
	    rm -f $(name)

fclean: clean
	    rm -f $(BINTESTNAME)

re:		clean $(name)
