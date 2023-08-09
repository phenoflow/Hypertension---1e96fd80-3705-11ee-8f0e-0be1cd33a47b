# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"G24..00","system":"readv2"},{"code":"G244.00","system":"readv2"},{"code":"G24z.00","system":"readv2"},{"code":"G24z100","system":"readv2"},{"code":"G24zz00","system":"readv2"},{"code":"16059","system":"med"},{"code":"25371","system":"med"},{"code":"31341","system":"med"},{"code":"31387","system":"med"},{"code":"31755","system":"med"},{"code":"32976","system":"med"},{"code":"34744","system":"med"},{"code":"42229","system":"med"},{"code":"51635","system":"med"},{"code":"57288","system":"med"},{"code":"59383","system":"med"},{"code":"7329","system":"med"},{"code":"73293","system":"med"},{"code":"97533","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hypertension-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["secondary-hypertension---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["secondary-hypertension---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["secondary-hypertension---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
