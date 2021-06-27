#!/bin/bash

for i in $(cat ../files/statistic.txt | sed 's/ /\\/g') ; do
    line=$(echo -e "$i" | sed 's/\\/ /g')
    achat=$(echo -e "$line" | cut -d '|' -f 1)
    vente=$(echo -e "$line" | cut -d '|' -f 2)
    id_achat=$(echo -e "$achat" | awk '{print $1}')
    prix_achat=$(echo -e "$achat" | awk '{print $2}')
    id_vente=$(echo -e "$vente" | awk '{print $1}')
    prix_vente=$(echo -e "$vente" | awk '{print $2}')

    quot=$(echo "$prix_vente / $prix_achat * 100 - 100" | bc -l)
    dec=$(echo -e "$quot" | cut -c "1-5")

    echo -e "Benef: $dec%"
done
