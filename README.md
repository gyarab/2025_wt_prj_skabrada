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