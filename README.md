# DORK SCANNER #

Un scanner de moteurs de recherche typique qui scrape les moteurs de recherche avec des requêtes que vous fournissez afin de trouver des URL vulnérables.


## Introduction ##

Le dorking est une technique utilisée par les rédactions, les organismes d'enquête, les auditeurs de sécurité et les criminels avertis pour interroger divers moteurs de recherche afin de trouver des informations cachées sur des sites Web publics et des vulnérabilités exposées par des serveurs publics. Le dorking est une façon d'utiliser les moteurs de recherche à leur pleine capacité pour pénétrer les services basés sur le web à des profondeurs qui ne sont pas nécessairement visibles au premier abord.

## Exigences ##

```
pip3 install -r requirements.txt
```

## Utilisation ##

```
$ python3 dorkScanner.py --help
utilisation : dorkScanner.py [-h] [-q QUERY] [-e ENGINE] [-p PAGES] [-P PROCESSES] [-o OUTPUT]

arguments facultatifs :
  -h, --help affiche ce message d'aide et sort
  -q QUERY, --query QUERY
                        Spécifie la requête de recherche sans ''.
  -e ENGINE, --engine ENGINE
                        Spécifie le moteur de recherche (Ask | Bing | WoW)
  -p PAGES, --pages PAGES
                        Spécifie le nombre de pages (par défaut : 1)
  -P PROCESSES, --processes PROCESSES
                        Spécifiez le nombre de processus (par défaut : 2)
  -o OUTPUT, --output OUTPUT 
			Spécifie le nom du fichier de sortie (chemin absolu ou relatif)
```

### Vous pouvez également spécifier les arguments à l'intérieur du programme :

```
Entrez la requête de recherche : 
Choisissez le moteur de recherche (Ask | Bing | WoW) :
```
