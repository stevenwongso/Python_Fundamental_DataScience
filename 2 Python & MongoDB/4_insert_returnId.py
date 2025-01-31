import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["py_mongo"]
mycol = mydb["users"]

mydata = { "nama": "Budi", "usia": "26" }
x = mycol.insert_one(mydata)
# get id dari data yg baru saja terkirim
print(x.inserted_id)

# =================== for insert_many() =======================

mydata = [
    {'nama': 'Euis', 'usia': 35, 'kota': 'Denpasar'},
    {'nama': 'Fafa', 'usia': 29, 'kota': 'Jakarta'},
    {'nama': 'Gian', 'usia': 22, 'kota': 'Sorong'}
]
x = mycol.insert_many(mydata)
print(x.inserted_ids)