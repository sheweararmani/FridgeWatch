import csv
import datetime
global ListboxList


def find_item_date_and_name(item_id, items_access_copy, good_food_types):

    i = 0
    arr = []
    for row in items_access_copy:
        # print(row)
        if i == 0:
            i = i + 1
        else:
            # we have found the item, now access the exp date
            if int(row[0]) == item_id and row[2] in good_food_types:
                exp_date = datetime.datetime.strptime(row[3], "%Y-%m-%d")
                name = row[1]
                arr.append(exp_date)
                arr.append(name)
    return arr


def start(ID):
    good_food_types = ["Fruit", "Beverages", "Baking", "Vegetables", "Condiments", "Meats", "Breads & Cereal", "Entrees",
                       "Diary", "Snacks", "Desserts", "Seafood", "Candy", "snacks", "Baby food", "Legumes", "Soups", "Sauces", "Sides"]
    ListboxList = []
    items = open("ProductDatabase.csv", "r")
    users = open("users.csv", "r")
    items_access = csv.reader(items)
    items_access_copy = []
    users_access = csv.reader(users)
    user_id = int(ID)  # This will depend on the USER!!! CHANGE ME IN THE GUI
    user_items = []
    for row in items_access:
        items_access_copy.append(row)
    i = 0
    for row in users_access:
        if i == 0:
            i = i + 1  # IGNORE THE HEADER
        else:
            if int(row[0]) == user_id:  # we have found the user, access their items
                exp_date_and_name = find_item_date_and_name(
                    int(row[1]), items_access_copy, good_food_types)
                current_date = datetime.datetime.now()
                print(exp_date_and_name)
                if exp_date_and_name != []:
                    ListboxList.append(str(exp_date_and_name[1]) + " will expire in " + str(
                        (exp_date_and_name[0] - current_date).days) + " days")
                print(ListboxList)

    return ListboxList


def delete_item(user_id, item_id, file_name="users.csv"):

    data = []

    # open and reader every row of the csv file
    with open(file_name, newline="") as csvfile:
        item_reader = csv.reader(csvfile, delimiter=',')
        for i, row in enumerate(item_reader):
            print(row)

            # skip the column headers
            if i == 0:
                data.append(row)
                continue

            # skip the data to be deleted
            if int(row[0]) == int(user_id) and int(row[1]) == int(item_id):
                continue

            # append the data to keeep
            data.append(row)

    # write the data to the csv file
    with open(file_name, 'w', newline="") as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)
