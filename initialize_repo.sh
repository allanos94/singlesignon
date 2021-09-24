#!/bin/sh -e

if [ $# -eq 0 ]; then
  ve_dir=ve
else
  ve_dir="$1"
fi

if [ ! -d "$ve_dir" ]; then
  python3.8 -m venv "$ve_dir"
fi

"$ve_dir"/bin/pip install -r requirements.txt

ve/bin/python mysite/manage.py migrate
ve/bin/python mysite/manage.py flush
ve/bin/python mysite/manage.py loaddata mysite/fixtures/data.json

