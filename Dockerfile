FROM python:3.9.13-slim

COPY requirements requirements
RUN pip install --disable-pip-version-check --no-cache-dir -r requirements/main.txt

COPY rc rc
COPY setup.py .
RUN pip install --disable-pip-version-check --no-cache-dir -e .

ENTRYPOINT ["rc"]
