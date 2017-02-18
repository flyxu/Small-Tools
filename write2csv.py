import csv
filepath=[]
labels=[]
file_object = open('./path_label.csv', 'wb')
file = csv.writer(file_object)
file.writerow(["filepath", "label"])
file_path = zip(filepath, labels)
for i in range(len(filepath)):
    file.writerow(file_path[i])
file_object.close()
print 'Done'