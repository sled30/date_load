import os



def read_file(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            date = line.split(',')
            name = serialize_esc(date[0])
            surname = serialize_esc(date[1])
            email = serialize_esc(date[2])
            password = serialize_esc(date[3])
            phone = serialize_esc(date[4])
            phone = serialize_phone(phone)
            print(phone)
        file.close()

def serialize_esc(string):
    return string.strip().lstrip('\'').rstrip('\'')

def serialize_phone(string):
    return string.rstrip(');')


if __name__ == "__main__":
    file_dir = 'datafiles'
    file_name = 'xzaio'

    read_file(file_dir + '/' + file_name)
