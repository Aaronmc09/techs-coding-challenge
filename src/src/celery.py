import os
from celery import Celery
from urllib import request
import csv
import psycopg2
from celery.signals import celeryd_after_setup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")
app = Celery("src")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


# Loads data from CSV if database is empty
@celeryd_after_setup.connect
def load_data(**kwargs):

    def int_or_null(value: str):
        return int(value) if value.isdigit() else "NULL"

    def clean_string(value: str):
        return value.replace("'", "")

    conn = psycopg2.connect(
        host="db",
        database=os.environ.get("POSTGRES_DB"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD"),
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * from records")
    result = cursor.fetchone()
    _id = 1

    print("Loading data..")

    if not result:

        print("Downloading csv..")

        csv_url = "https://data.cityofnewyork.us/api/views/7yc5-fec2/rows.csv"

        print("Download complete!")

        response = request.urlopen(csv_url)
        lines = [line.decode("utf-8") for line in response.readlines()]
        cr = csv.reader(lines)
        # Skip headers
        next(cr, None)

        for row in cr:

            sql_insert = f"INSERT INTO records VALUES ({_id}, '{clean_string(row[0])}', '{clean_string(row[1])}', " \
                         f"'{clean_string(row[2])}', {int_or_null(row[4])}, " \
                         f"{int_or_null(row[5])}, {int_or_null(row[6])}, {int_or_null(row[7])}, {int_or_null(row[8])}, " \
                         f"{int_or_null(row[9])}, {int_or_null(row[10])}, {int_or_null(row[11])}, {int_or_null(row[12])}, " \
                         f"{int_or_null(row[13])}, {int_or_null(row[14])}, {int_or_null(row[16])}, {int_or_null(row[18])}, " \
                         f"{int_or_null(row[20])}, {int_or_null(row[22])}, {int_or_null(row[24])}, {int_or_null(row[26])}, " \
                         f"{int_or_null(row[28])}, {int_or_null(row[30])}, {int_or_null(row[32])}, {int_or_null(row[34])}, " \
                         f"{int_or_null(row[36])}, {int_or_null(row[38])}, {int_or_null(row[40])}, {int_or_null(row[42])}, " \
                         f"{int_or_null(row[44])}, {int_or_null(row[46])}, {int_or_null(row[48])}, {int_or_null(row[49])}, " \
                         f"{int_or_null(row[51])}, {int_or_null(row[53])}, {int_or_null(row[55])}, " \
                         f"{int_or_null(row[59])}, {int_or_null(row[60])}, {int_or_null(row[62])}, {int_or_null(row[64])}, " \
                         f"{int_or_null(row[66])})"
            cursor.execute(sql_insert)
            _id += 1

        cursor.execute("SELECT setval('records_id_seq', (SELECT MAX(id) FROM records)+1);")
        conn.commit()

    print("Load complete!")
    cursor.close()
    conn.close()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
