=====
Exo 1
=====


Compiler Suricata depuis la branche master du git
=================================================

.. code-block::

 git clone https://github.com/OISF/suricata.git
 cd suricata
 ./scripts/bundle.sh
 sudo apt install libpcap-dev autoconf libtool libmagic-dev
 ./autogen.sh
 ./configure --prefix=/home/user/suricata
 make
 make install-full


ANalyse de trace
================

Utilisons un pcap avec du contenu:

.. code-block::

 wget https://www.malware-traffic-analysis.net/2022/10/31/2022-10-31-IcedID-with-DarkVNC-and-Cobalt-Strike-full-pcap-raw.pcap.zip -c
 unzip 2022-10-31-IcedID-with-DarkVNC-and-Cobalt-Strike-full-pcap-raw.pcap.zip

Rejouer le pcap avec suricata
-----------------------------

On n'utilisera pas de signatures et on redirigera la sortie dans un répertoire dédié.

Utiliser jq pour analyser le fichier
-------------------------------------

Quels event_type sont générés ?
Quel semble être le réseau interne ?
Quels sont les domaines contactés en TLS et http ?
Vérifier les noms de domaines suspects sur virustotal
Quel est le nom du domain windows ?
Quel est le nom de l'utilisateur ?
Quel est le nom de la machine sur le réseau et son IP ?
ddQuel sont les services offerts sur le réseau en TCP ? ? 

Sécurisation et configuration de Suricata
-----------------------------------------

#Récupérer et compiler https://github.com/OISF/suricata/pull/8196 
#Activer le support de landlock
Ajouter le calcul des sha256 et filemagic aux événements fileinfo
Activer http all headers
Rejouer le fichier pcap

Ma première signature
---------------------

Installer Suricata Language Server: https://github.com/StamusNetworks/suricata-language-server
Ecrire une signature alertant sur les requêtes DNS vers le domaine `yeloypod.hair`
Tester la signature sur le pcap en ne chargeant que cette signature

Vérification de certificats TLS
-------------------------------

Capturer le traffic à destination du site de l'esiea
Ecrire une signature alertant si le certificat TLS du site change
Vérifier en rejouant le pcap généré

Dataset
-------

Ecrire des signatures utilisant dataset pour collecter les hostnames utilisés lors des connexions applicatives
Rejouer le pcap
Analyser la liste des domaines en regardant les alertes
Faire de même en regardant le fichier généré

Rejouer le pcap MTA avec les signatures activées
-------------------------------------------------

Le logiciel suricata-update télécharge les règles ET-Open.

Activer la journalisation pcap conditionelle en utilisant l'option --set
Rejouer le pcap en chargeant les signatures. On veillera à effectuer une sortie dans un répertoire différent.
Quels sont les signatures déclenchées sur le pcap ?
Quelles sont les menaces ?
Analyser l'événement produit par 2032086. Pourquoi a-t-on une alerte ?
Récupérer tous les événements sur le flow
Utiliser gophercap (ou tcpdump) pour récupérer le contenu des paquets du flow
Quelle est la taille du fichier pcap généré par Suricata ? Quel est le rapport de compression.

Unix socket mode
----------------

Récupérer les 5 derniers fichier de malware-traffic-analysis
Lancer Suricata en mode unix socket
Analyser les fichiers pcaps télécharger en stockant le résultat de l'analyse dans un répertoire par pcap 


