#!/bin/bash

# Comprobar si se proporcionó un argumento
if [ -z "$1" ]; then
  echo "Ingrese su username de Git/Github:"
  read suffix
else
  suffix=$1
fi

# Actualizar la rama main
git checkout main
git pull origin main

# Seguir un estándar
git checkout -b "develop-$suffix"
git push origin "develop-$suffix"
git checkout -b "feature/feature-1-$suffix"
git push origin "feature/feature-1-$suffix"
