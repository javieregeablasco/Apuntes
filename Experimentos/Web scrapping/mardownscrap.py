import requests # pip install requests , 
# pip install mypy → venv activate → mypy --install-types
from markdownify import markdownify as md # pip install markdownify
import argparse
import os

###########

# Configurar arguments
parser = argparse.ArgumentParser(
    description="Converteix una pàgina HTML (des de URL) a un arxiu Markdown (.md)"
)
# parser.add_argument("url", help="URL de l'arxiu HTML a convertir")
parser.add_argument("url", nargs="?", default="https://nachoiborraies.github.io/python/07.html", help="URL de l'arxiu HTML a convertir")
# parser.add_argument("nom_eixida", help="Nom de l'arxiu d'eixida (sense extensió .md)")
parser.add_argument("nom_eixida", nargs="?", default="sortida", help="Nom de l'arxiu d'eixida (sense extensió .md)")

args = parser.parse_args()

# Descarregar contingut HTML
print(f"📥 Descarregant contingut des de: {args.url}")
response = requests.get(args.url)

if response.status_code != 200:
    print(f"❌ Error al accedir a la URL (codi {response.status_code})")
    exit(1)

html = response.text

# Convertir a Markdown
print("⚙️  Convertint a format Markdown...")
markdown = md(html, heading_style="ATX")

# Guardar resultat
nom_arxiu = f"{args.nom_eixida}.md"
with open(nom_arxiu, "w", encoding="utf-8", newline="\n") as f:
    f.write(markdown)

print(f"✅ Conversió completada. Arxiu guardat com a: {nom_arxiu}")
print(f"📂 Ruta completa: {os.path.abspath(nom_arxiu)}")