#!/bin/bash

# Comprobar si se proporcionó un argumento
if [ -z "$1" ]; then
  echo "Ingrese su username de Git/Github:"
  read suffix
else
  suffix=$1
fi

# Cambiar a la rama 'develop' con el sufijo
git checkout "develop-$suffix"
git pull origin "develop-$suffix"

# Crear otra rama con el sufijo
git checkout -b "feature/feature-2-$suffix"
git push origin "feature/feature-2-$suffix"

# Fusionar ramas con el sufijo
git checkout "develop-$suffix"
git merge --no-ff "feature/feature-1-$suffix"
git push origin "develop-$suffix"

# Crear algunos archivos
cat << EOF >> hello.py
if __name__ == "__main__":
    print("Hello world")
    exit(0)
EOF

# Añadir el commit en la rama con el sufijo
git checkout "feature/feature-2-$suffix"
git add hello.py
git commit -m "Add hello world in python"
git push origin "feature/feature-2-$suffix"
