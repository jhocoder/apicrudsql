FROM python:3.12

WORKDIR /apisql

COPY . .

RUN python3 -m venv venv
RUN ./venv/bin/pip install --no-cache-dir -r requirements.txt

CMD [ "./venv/bin/python", "src/app.py" ]


