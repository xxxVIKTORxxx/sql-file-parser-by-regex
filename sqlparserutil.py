

#import pandas as pd
import re
import csv

sqlfile1 = "Sample-SQL-File-500000-Rows.sql"
test1 = "database/test.sql"
test2 = "database/test3.sql"
test3 = "database/test4.sql"
test_list = [sqlfile1, test1, test2, test3]
sqlfile = test_list[2]


def sqlreader(sqlfile):
    with open(sqlfile) as sqlfile:
        reader = csv.reader(sqlfile, delimiter=' ', quotechar='|')
        sqldatafile = ''
        for row in reader:
            sqldatafile = sqldatafile + ''.join(row) + '\n'
    return sqldatafile

             
def tablesfinder(sqldatafile):
    #tables
    table_names = re.findall('CREATETABLE[\w]*`([A-Za-z0-9.:;!?<>()-+=\s\w\d]*)`\(', sqldatafile)
    if len(table_names) > 0:
        print('Tables names: "{}"'.format(table_names))
        print('Amount of Tables: {}'.format(len(table_names)))

        pattern = '|INSERTINTO'
        inserts = sqldatafile.replace('INSERTINTO',pattern).split('|')
        print('Inserts Amount: {}'.format(len(inserts)))
        i=-1
        inserts_table_names = []
        for t in inserts[1:]:
            i +=1
            #columns names and counting for table
            columns_names = re.search('INSERTINTO\W([A-Za-z0-9.:;!?<>\(\)-+=\s\w\d]*)\W*([\WA-Za-z0-9.:;!?<>()-+=\s\w\d]*)\WVALUES', t)
            if columns_names:
                print(columns_names[1])
                columns = columns_names[2].replace('`', '').split(',')
                columns_str = ''
                for column in columns:
                    columns_str = columns_str + '"' + str(column) + '", '
                print('Columns Names in Table "{}" is: {}'.format(columns_names[1], columns_str[:-2]))
                print('Amount of Columns in Table "{}" is: {}'.format(columns_names[1], len(columns)))
                inserts_table_names.append(columns_names[1])
            else:
                pass
        
        ii=-1
        insert_index = []
        for insert_name in inserts_table_names:
            ii+=1
            insert_index.append(ii)
        print(inserts_table_names)
        print(insert_index)

        iii=-1
        rows_sum = 0
        for insert_name in inserts_table_names:
            rows_sum = 0
            iii+=1
            if len(inserts_table_names) < 19:
                rows_sum = inserts[iii].count('\n')
                if insert_name != inserts_table_names[iii+1]:
                    rows_sum += inserts[iii+2].count('\n')
            else:
                rows_sum = inserts[ii+1].count('\n')
                print('Amount of Rows in Table "{}": {}\n'.format(insert_name, rows_sum))
            

        #rows counter for table

            #if columns_names[1] == 
            #rows_sum += insert.count('\n')
            #print('Amount of Rows in Table "{}": {}\n'.format(table_names[i], rows_sum))

    else:
        print('No Tables detected\n')


#for sql in test_list:
#    sqlfileparser(sql)
def main():
    tablesfinder(sqlreader(sqlfile))

main()
