#!/bin/bash

# Comprobar si se proporcionó un argumento
if [ -z "$1" ]; then
  echo "Ingrese su username de Git/Github:"
  read suffix
else
  suffix=$1
fi

# Integrar la tercera rama con el sufijo
git checkout "develop-$suffix"
git pull origin "develop-$suffix"
git merge --no-ff "feature/feature-3-$suffix"
git push origin "develop-$suffix"

# Crear una nueva rama con el sufijo
git checkout -b "feature/feature-4-$suffix"
git push origin "feature/feature-4-$suffix"

# Eliminar archivos y empezar de nuevo
rm *.c *.py Makefile
mkdir src build