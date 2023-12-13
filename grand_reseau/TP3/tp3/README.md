Step 0:


Step3:
150000  field2_length    :  1
150000  field3_length    :  9
75000   field4_length    :  13
75000   field4_length    :  18
150000  nb_of_fields     :  4
1       number_of_lines  :  150000

On voit bien que c'est consistent car le nombre de lignes d'erreurs détectées est de 150000 contre 75000 fichiers de configuration. Et je suis censé avoir 2 erreurs par fichier donc c'est correcte

Step 4:
2       field2_length    :  0
149784  field2_length    :  1
214     field2_length    :  18
216     field3_length    :  0
214     field3_length    :  27
149570  field3_length    :  9
216     field4_length    :  0
214     field4_length    :  1
74783   field4_length    :  13
1       field4_length    :  17
74785   field4_length    :  18
1       field4_length    :  24
2       nb_of_fields     :  1
214     nb_of_fields     :  2
149568  nb_of_fields     :  4
214     nb_of_fields     :  6
2       nb_of_fields     :  7
1       number_of_lines  :  150000

Ce n'est pas cohérent, je suis censé avoir 150000 lignes d'erreurs de 4 champs mais j'en obtient 149568 et cette erreur provient du fichier de sortie où il y a des lignes incohérentes comme: "conf/router.unix.15340 : interconf/router.unix.15351 : interface FastEthernet0".

Step5:
