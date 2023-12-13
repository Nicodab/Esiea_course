#!/bin/bash

# Répertoire cible
target_dir="conf"

# Nom du fichier source
source_file="router.unix"

# Créer le répertoire s'il n'existe pas
mkdir -p "$target_dir"

# Copier le fichier 10 000 fois
for ((i=1; i<=10000; i++))
do
  cp "$source_file" "$target_dir/$source_file.$i"
done

echo "La génération est terminée."
