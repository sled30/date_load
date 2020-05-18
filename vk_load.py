import os
import db


def read_file(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            date = line.split(',')
            name = serialize_esc(date[0])
            surname = serialize_esc(date[1])
            email = serialize_esc(date[2])
            id_email = db.insert_email(email)
            password = serialize_esc(date[3])
            phone = serialize_esc(date[4])
            phone = serialize_phone(phone)
            id_phone = db.insert_phone(phone)
            id_date = db.insert_date(name, surname, id_email, password, id_phone)
        file.close()

def serialize_esc(string):
    return string.strip().lstrip('\'').rstrip('\'')

def serialize_phone(string):
    return string.rstrip(');')
def create_turn():
    base_dir = 'datafiles'
    files = os.listdir(base_dir)
    check = db.save_turn_vk_files(files)

def rename_file_in(source_file):
    try:

        os.rename('datafiles/' + source_file, 'datafiles/in/' + source_file)
    except Exception as e:
        print(e)
def rename_file_load(source_file):
    try:
        os.rename('datafiles/in/' + source_file, 'datafiles/load/' + source_file)
    except Exception as e:
        raise

if __name__ == "__main__":
    file_dir = 'datafiles'
    # file_name = 'xzaio'
    #
    # read_file(file_dir + '/' + file_name)
    create_turn()
    turns = db.get_turn_vk_files()
    for file in turns:
        read_file(file_dir + '/in/' + file[0])
        rename_file_load(file[0])
