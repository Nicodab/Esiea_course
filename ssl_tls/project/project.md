# Projets pycryptodome

## Exercice 1

*But :
  Ecrire un logiciel de chiffrement multi-destinataires qui
  protege un fichier en confidentialite et en integrite.

  Un fois le fichier protege, il est envoye a N destinataires. Si le
  destinataire est legitime, il peut le deprotege,
    sinon il ne peut rien en  faire.

  Chaque intervenant possede un bi-cle RSA-2048 pour le
  chiffrement/dechiffrement et un bi-cle RSA-2048 pour la signature.

  Proteger le fichier en confidentialite:
    - Kc : random()
    - IV : random()
    - C = AES-CBC-256(input, Kc, IV)
    - RSA PKCS#1 OAEP
  Proteger le fichier en integrite:
    - Signer la totalite du message a envoyer
    - RSA PKCS#1 PSS

  0x00 || SHA256(kpub-1) || RSA_kpub-1(Kc || IV) || ... || 0x00 || SHA256(kpub-N) || RSA_kpub-N(Kc || IV) || 0x01 || C || Sign

*Usage pour un participant legitime:
  $ openssl genrsa 2048 > my_ciph_priv.pem [my_ciph_pub.pem]
  $ openssl genrsa 2048 > my_sign_priv.pem [my_sign_pub.pem]

  // Proteger input_file
  $ python multi_protect.py -e <input_file> <output_file> <my_sign_priv.pem> <my_ciph_pub.pem> [user1_ciph_pub.pem ... [userN_ciph_pub.pem]]
  // retourne 0 si OK, 1 sinon

  // Deproteger input_file
  $ python multi_protect.py -d <input_file> <output_file> <my_priv_ciph.pem> <my_pub_ciph.pem> <sender_sign_pub.pem>
  // retourne 0 si OK, 1 sinon


## Exercice 2
finir unprotect_symetric.py


## Exercice 3
finir unprotect_asymetric.py


## MISC
De facon generale
- l'archive envoyee sera 'propre', i.e. elle ne contiendra pas
d'executable ou de fichier objets issus de compilation
- assurez vous que vos projets fonctionnent chez moi (linux x86_64, python3)

date de reception (max) : 22/12/2023 @ 23:59 (GMT+1  -- HEURE FRANCAISE)
subject : [MSSIS_2324_crypto]
mail : olivier.tuchon+MSSIS2324@gmail.com
