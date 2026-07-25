
src	=	$(wildcard main.py Src/*.py)

name  =		103cipher

all: $(name)

$(name):	$(src)
	    cp main.py $(name)
		chmod +x $(name)

clean:
	    rm -f $(name)

fclean: clean

re:		clean $(name)
