# Webová aplikace
Vznikla v předmětu Webové technologie na Gymnáziu Arabská ve školním roce 2025/2026.
Toto je repozitář jednoho ze studentů tohoto předmětu.

## Local development

Aplikace používá Python Virtual Environment, před spuštěním je potřeba vytvořit venv (pokud neexistuje):

```bash
# Linux
python3 -m venv venv

# Windows
py -3 -m venv venv
```

Dále je třeba venv aktivovat:

```bash
# [Linux]
source ./venv/bin/activate

# Windows - Bash
source ./venv/Scripts/activate
```

Je třeba ujistit se, že jsou nainstalovány všechny závislosti:

```bash
# (venv)$
pip install -r requirements.txt
```

Spustit lokalni server

```bash
cd prj
./manage.py runserver
```

Pokud pouštíme projekt poprvé, je třeba inicializovat DB pomocí

```bash
./manage.py migrate
```

Pokud je DB prázdná a chceme mít přístup do Django administrace, vytvoříme si uživatele pomocí

```bash
./manage.py createsuperuser
```

Doporučuji použít username `admin` a heslo `admin`, bez e-mailu.

## Změna `models.py`

Po kazde zmene v models.py je treba pustit skript, ktery vygeneruje zmenu struktury DB.

```bash
./manage.py makemigrations
```

Pote zmenu DB aplikovat na aktualni zivou DB

```bash
./manage.py migrate
```

# Color scheme
## Odborný článek
Jedná se o webovou databázi, která zaznamenává palety barev, samotných barev a jejich respektivní detaily. Hlavní gimika tohoto programu by blo, že každý den tento program nabídne novou/jinou **paletu dne**, kterou může uživatel použít na svou práci. Z toho vyplívá, že uživatel bude schopen nahrát fotografii s tímto dílem k dané paletě. Pokud tedy přiloží svoji práci tak poté (po skončení lhůty) se daná paleta i s fotografií uloží do "**galerie**". Dále bude uživatel schopen si danou paletu *bookmarknou* a ta se uloží do složky **oblíbená**. Další částí by byla možnost jít do poddatabáze, kte by byly sepsané různé informace samotné barvy (např: odborné jméno, hex, extra informace), které by se čerpali z extarních zdrojů. Uživatel bude moci připisovat sám do těchto informací. Všechny části ohledně samotného přizpůsobování uživatele budou zamčené za přihlášením uživatele, tudíž se jedná o osobní zápisy.
Nabízí se tedy i možnost pro nepřihlášeného uživatele v podobě pouhé palety dne, ale pokud by uživatel zvažoval dělat více, tak by se musel zaregistrovat nobo jednoduše připojit na svůj účet.

### nepřihlášný uživatel
Buď by nepřihlášený uivatel pouze mohl vidět paletu dne, a nebo by se jednalo o aplikaci, kde je nutné se přihlásit.

### přihlášený uživatel
přihlášený uživatel bude mt k dispozity veškeré nástroje zmínené výše v odborném članku.

### admin
Admin jako takyvý bude moci měnit *prmanetní* informace na stránce (změna/přidání/ubrání popisků, informací, barev, palet).

## Userflow
![userflow](foto/userflow.png)

## Wireframe
![userflow](foto/wireframe1.png)
![userflow](foto/wireframe2.png)

## DB-Schéma
![userflow](foto/DB-diagram.png)
