from pymongo import MongoClient

myclient = MongoClient('localhost', 27017)
mydb = myclient["PhoneNumberDB"]

# print(client.list_database_names())

mycol = mydb["PhoneBook"]


# x = mycol.insert_one({"first_name": "yousef", "last_name": "zare", "phonenumber1": "09123456789"})
# print(x.inserted_id)

def update(old_phone, new_phone):
    for i in range(10):
        i = str(i)
        query = {"phonenumber" + i: old_phone}
        newvalues = {"$set": {"phonenumber" + i: new_phone}}
        mycol.update_one(query, newvalues)


def delete(phone_num):
    for i in range(10):
        i = str(i)
        query = {"phonenumber"+i: phone_num}
        mycol.delete_one(query)

    return f'delete done'


def insert(fname, lname, phone_num):
    w = mycol.insert_one({"first_name": fname, "last_name": lname, "phonenumber1": phone_num})
    return f'insert done'

