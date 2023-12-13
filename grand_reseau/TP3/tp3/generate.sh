#!/bin/bash
# Step 0

# Répertoire cible
target_dir="conf"

# fichier source
source_file="router.unix"

# Créer le répertoire s'il n'existe pas
mkdir -p "$target_dir"

# Copier 10 000 fois le fichier
for ((i=1; i<=75000; i++))
do
  cp "$source_file" "$target_dir/$source_file.$i"
done

echo "La génération est terminée."
