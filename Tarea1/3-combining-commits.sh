#!/bin/bash

# Comprobar si se proporcionó un argumento
if [ -z "$1" ]; then
  echo "Ingrese su username de Git/Github:"
  read suffix
else
  suffix=$1
fi

# Integrar la segunda rama con el sufijo
git checkout "develop-$suffix"
git pull origin "develop-$suffix"
git merge --no-ff "feature/feature-2-$suffix"
git push origin "develop-$suffix"

# Crear una nueva rama con el sufijo
git checkout -b "feature/feature-3-$suffix"
git push origin "feature/feature-3-$suffix"

# Crear algunos archivos y varios commits
cat << EOF >> printcpu.c
#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
   FILE *cpuinfo = fopen("/proc/cpuinfo", "rb");
   char *arg = 0;
   size_t size = 0;
   while(getdelim(&arg, &size, 0, cpuinfo) != -1)
   {
      puts(arg);
   }
   free(arg);
   fclose(cpuinfo);
   return 0;
}
EOF

git add printcpu.c
git commit -m "Add arm info"

cat << EOF >> meminfo.c
#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
   FILE *meminfo = fopen("/proc/meminfo", "rb");
   char *arg = 0;
   size_t size = 0;
   while(getdelim(&arg, &size, 0, meminfo) != -1)
   {
      puts(arg);
   }
   free(arg);
   fclose(meminfo);
   return 0;
}
EOF

git add meminfo.c
git commit -m "Add Memory info"

git push origin "feature/feature-3-$suffix"
