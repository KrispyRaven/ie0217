#!/bin/bash

# Comprobar si se proporcionó un argumento
if [ -z "$1" ]; then
  echo "Ingrese su username de Git/Github:"
  read suffix
else
  suffix=$1
fi

# Crear algunos archivos
cat << EOF >> hello.c
#include "stdio.h"

int main() {
    printf("Hello World!\n");
    return 0;
}
EOF

cat << EOF >> Makefile
.PHONY: clean all

SRCS := $(wildcard *.c)
EXES := $(SRCS:.c=.x)
CFLAGS := -Wall -Werror

all: $(EXES)

%.x: %.c
	$(CC) $^ $(CFLAGS) -o $@
	mv $@ $(basename $@)

.PHONY: all clean

clean:
	$(RM) $(EXES) *~
EOF

# Crear commits
git add Makefile hello.c
git commit -m "Add makefile"
git push origin "feature/feature-1-$suffix"
