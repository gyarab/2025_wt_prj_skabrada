# Webová aplikace
Vznikla v předmětu Webové technologie na Gymnáziu Arabská ve školním roce 2025/2026.
Toto je repozitář jednoho ze studentů tohoto předmětu.

## Local development

Aplikace používá Python Virtual Environment, před spuštěním je potřeba vytvořit venv (pokud neexistuje):

```bash
# Linux
python3 -m venv venv

# Windows
python -m venv venv
```

Dále je třeba venv aktivovat:

```bash
# [Linux]
source ./venv/bin/activate

# Windows - Bash
source venv/Scripts/activate

# Windows - Power shell
.\venv\Scripts\activate
```

Je třeba ujistit se, že jsou nainstalovány všechny závislosti:

```bash
# (venv)$
pip install -r requirements.txt
```


# Knihovna Babylon
Inspirováno stejnojmeným dílem. Tento projekt by se snažil docílit stejného fenoménu, který toto dílo nabízí v podobě "nekončící" knihovny, která by se dala wolně procházet a v níž by mohl uživatel luštit komplexní slova a jejich význam. Premise je taková, že každá místnost v této knihovně má tisíce knih se stovkami stránek. Každá stránka obsahuje kolem 25 náhodných znaků. Kvůli velikosti této knihovny se ovšem dá najít význam všeho, co je někde jinde uvedeno...