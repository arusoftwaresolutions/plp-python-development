def file_managing(file_name, copy_to):
    """this function takes two parameters  file_name the file going to be copyed
    and copy_to the file where the copying file will be saved"""
    try:
        with open(file_name, 'r') as file:
            data=file.read()

    except FileNotFoundError:
        print(f"the file name {file_name} doesn't exists in this directory ")
   
    else:
        if data != '':
            with open(copy_to, 'w') as file:
                file.write(data.upper())
        else:
            print(f"the file {file_name} is an empty file")
    finally:
        print("excution finished")


file_name=input("enter the file name you want to copy: ")
copy_to=input("enter file name where to copy the file: ")
file_managing(file_name, copy_to)
