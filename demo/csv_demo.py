
import csv

if __name__ == '__main__':
    # 读取csv文件
    import csv
    with open('some.csv', 'rb') as f:        # 采用b的方式处理可以省去很多问题
        reader = csv.reader(f)
        for row in reader:
            # do something with row, such as row[0],row[1]


    import csv
    with open('some.csv', 'wb') as f:      # 采用b的方式处理可以省去很多问题
        writer = csv.writer(f)
        writer.writerows(someiterable)


    # 字典方式
    # 读
    import csv
    with open('names.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['first_name'], row['last_name'])


    # 写
    import csv
    with open('names.csv', 'w') as csvfile:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

    with open('egg2.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile,dialect='excel')
        spamwriter.writerow(['a', '1', '1', '2', '2'])
        spamwriter.writerow(['b', '3', '3', '6', '4'])
        spamwriter.writerow(['c', '7', '7', '10', '4'])
        spamwriter.writerow(['d', '11','11','11', '1'])
        spamwriter.writerow(['e', '12','12','14', '3'])