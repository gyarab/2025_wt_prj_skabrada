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


# Doomsday clock
## článek odbornářů
Nápad na vedení databáze inspirované na základě stejnojmeného, už existujícího, projektu. Toto je ovšem zkušební projekt na design stránky a na další příležitostní zkušenosti, které se díky tomudle vyskytnou. Navíc by bylo fajn skusit nějakou zjednosušenou verzi, protože originí je dosti (za mne) chaotická při prvním otevření a hodně lidí by to odtáhlo.
Představuji si jednoduché zavedení pouze pozorovatele a editora. Lepe řečeno jakýkoliv uživatel by mohl přidat jakoukoliv informaci vázající se k tématu, kde by uvedl svůj článek s jeho zdroji, a to by se přidalo. Pokud by tyto informace byly sporné, tak by mohl jakýkoliv uživatel tnto článek nahlásit a to by se poslalo do veřejného hlasování, kte můžou volit všichni aktivní uživatelé po nějakou dobu, po které by se článek vymazal, nebo zůstal v databázi.
Co se týče samotné databáze, tak bych rád uvedlo; o co se jedná (doom clock), jednotlivé články podle časové osy, externí zdroje, rekordy a například i vyhledávání keywords... Především by jsem se soustředil na vyzuální stránku a přehlednost projektu. Jedna z těch přehledností také bude, že na této stránce nebudou vyskakovat žádné reklamy, což beru jako velké plus.

ps: O víkendu proběhne komplet předělání na základě mého rozhodnutí o zvolení jiného tématu (zase).

## User and his flow
![userflow](foto/userflow.png)

## Wires acros frames
![wireframe](foto/wireframe.png)
![wireframe](foto/wireframe2.png)

## DB - schéma
![DB-schema](foto/DB-schema.png.png)
