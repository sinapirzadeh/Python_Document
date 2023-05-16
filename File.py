txtFile = open('C:\\Users\Pirzadeh\Desktop\\text.txt')
print(txtFile.read())
txtFile.seek(0)
print(txtFile.read())