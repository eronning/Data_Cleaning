#!/usr/bin/env python
import sys
import csv

furniture_path = ''
title_col_val = 'producttitle_value'
description_col_val = 'productdesp_value'
price_col_val = 'productdetails_link_prices'
type_col_val = 'type'
title_col_num = 0
description_col_num = 0
price_col_num = 0
type_col_num = 0

def main():
    '''
    For CSV:
    '''
    with open(furniture_path) as f:
        reader = csv.reader(f)
        header = next(reader)
        for i in range(len(header)):
            if header[i] == title_col_val:
                title_col_num = i
            if header[i] == description_col_val:
                description_col_num = i
            if header[i] == price_col_val:
                price_col_num = i
            if header[i] == type_col_val:
                type_col_num = i
        included_cols = [title_col_num, description_col_num, price_col_num, type_col_num]
        data = []
        for row in reader:
            content = list(unicode(row[i], 'utf-8') for i in included_cols)
            data.append(content)
        
        with open('clean_furniture.csv') as w:
            writer = csv.writer(w)
            row = ['name', 'description', 'price', 'type']
            for i in range(len(row)):
                row[i] = row[i].encode('utf-8')
            writer.writerow(row)    
    
    # TODO: clean furniture.csv
    pass

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: python clean_furniture.py furniture'
    furniture_path = sys.argv[1]
    main()
