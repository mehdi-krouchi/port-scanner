# Port Scanner 

Scanner de ports TCP écrit en Python. Permet de détecter les ports ouverts sur une machine et d'identifier les services qui tournent dessus.

## Pourquoi ce projet ?

J'ai commencé à apprendre la cybersécurité et les réseaux, et un scanner de ports c'est un des premiers outils concrets qu'on utilise dans ce domaine. C'est la base de ce que fait Nmap.

## Ce que ça fait

- Tu entres une IP cible et une plage de ports
- Il teste chaque port et affiche ceux qui sont ouverts
- Il identifie le service associé (HTTP, SSH, FTP, MySQL...)
- Il mesure le temps du scan
- Il sauvegarde les résultats dans un fichier .txt

## Stack

- Python 3.13
- socket (connexions TCP)
- time (durée du scan)

## Lancer le script

```bash
python main.py
```

## Exemple

Scan de 127.0.0.1 — ports 1 à 1024
Port 22 — OUVERT (SSH)
Port 80 — OUVERT (HTTP)
Port 443 — OUVERT (HTTPS)

Scan terminé en 12.3 secondes.
3 port(s) ouvert(s) trouvé(s).

##  Avertissement

À utiliser uniquement sur des machines vous appartenant ou sur lesquelles vous avez une autorisation explicite.
