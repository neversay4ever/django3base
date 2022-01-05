import csv
from demo.models import DataModel

# run exec(open('./save_data.py').read())  in django shell


with open("./data.demo.csv") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        _, created = DataModel.objects.get_or_create(
            gene_id=row[0],
            gene_length=row[1],
            gene_seq=row[2],
        )

print("DataModel END")
