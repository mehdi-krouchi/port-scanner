import socket
import time

SERVICES = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
    443: "HTTPS", 3306: "MySQL", 3389: "RDP",
    8080: "HTTP-ALT", 8443: "HTTPS-ALT"
}

def scan_port(ip, port, timeout=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        resultat = sock.connect_ex((ip, port))
        sock.close()
        return resultat == 0
    except Exception:
        return False

def main():
    cible = input("Adresse IP à scanner : ")
    port_debut = int(input("Port de début : "))
    port_fin = int(input("Port de fin : "))

    print(f"\nScan de {cible} — ports {port_debut} à {port_fin}")
    print("-" * 40)

    ports_ouverts = []
    debut_temps = time.time()

    for port in range(port_debut, port_fin + 1):
        if scan_port(cible, port):
            service = SERVICES.get(port, "Inconnu")
            ligne = f"Port {port} — OUVERT ({service})"
            print(ligne)
            ports_ouverts.append(ligne)

    duree = round(time.time() - debut_temps, 2)
    print("-" * 40)
    print(f"Scan terminé en {duree} secondes.")
    print(f"{len(ports_ouverts)} port(s) ouvert(s) trouvé(s).")

    nom_fichier = f"scan_{cible}.txt"
    with open(nom_fichier, "w") as f:
        f.write(f"Scan de {cible} — ports {port_debut} à {port_fin}\n")
        f.write("-" * 40 + "\n")
        for ligne in ports_ouverts:
            f.write(ligne + "\n")
        f.write("-" * 40 + "\n")
        f.write(f"Scan terminé en {duree} secondes.\n")
        f.write(f"{len(ports_ouverts)} port(s) ouvert(s).\n")

    print(f"\nRésultats sauvegardés dans {nom_fichier}")

main()