# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"14A2.00","system":"readv2"},{"code":"6146200","system":"readv2"},{"code":"6624","system":"readv2"},{"code":"7Q01.00","system":"readv2"},{"code":"9OI9.00","system":"readv2"},{"code":"G202.00","system":"readv2"},{"code":"G203.00","system":"readv2"},{"code":"G20z.11","system":"readv2"},{"code":"10818","system":"med"},{"code":"11056","system":"med"},{"code":"13188","system":"med"},{"code":"15106","system":"med"},{"code":"15377","system":"med"},{"code":"16173","system":"med"},{"code":"16292","system":"med"},{"code":"16565","system":"med"},{"code":"18057","system":"med"},{"code":"18482","system":"med"},{"code":"18590","system":"med"},{"code":"18765","system":"med"},{"code":"1894","system":"med"},{"code":"19070","system":"med"},{"code":"204","system":"med"},{"code":"20497","system":"med"},{"code":"21660","system":"med"},{"code":"21826","system":"med"},{"code":"21837","system":"med"},{"code":"22333","system":"med"},{"code":"27511","system":"med"},{"code":"28684","system":"med"},{"code":"29310","system":"med"},{"code":"30770","system":"med"},{"code":"31464","system":"med"},{"code":"31816","system":"med"},{"code":"32423","system":"med"},{"code":"3425","system":"med"},{"code":"37086","system":"med"},{"code":"3712","system":"med"},{"code":"39649","system":"med"},{"code":"3979","system":"med"},{"code":"43664","system":"med"},{"code":"4372","system":"med"},{"code":"43935","system":"med"},{"code":"44350","system":"med"},{"code":"44549","system":"med"},{"code":"4668","system":"med"},{"code":"50157","system":"med"},{"code":"52127","system":"med"},{"code":"52427","system":"med"},{"code":"52621","system":"med"},{"code":"57987","system":"med"},{"code":"60655","system":"med"},{"code":"61166","system":"med"},{"code":"61660","system":"med"},{"code":"62432","system":"med"},{"code":"62718","system":"med"},{"code":"63000","system":"med"},{"code":"63164","system":"med"},{"code":"63466","system":"med"},{"code":"66567","system":"med"},{"code":"6702","system":"med"},{"code":"67232","system":"med"},{"code":"68659","system":"med"},{"code":"69753","system":"med"},{"code":"7057","system":"med"},{"code":"72030","system":"med"},{"code":"72668","system":"med"},{"code":"73586","system":"med"},{"code":"799","system":"med"},{"code":"8296","system":"med"},{"code":"83473","system":"med"},{"code":"85944","system":"med"},{"code":"8732","system":"med"},{"code":"8857","system":"med"},{"code":"93055","system":"med"},{"code":"95334","system":"med"},{"code":"95359","system":"med"},{"code":"96743","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hypertension-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hypertension---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hypertension---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hypertension---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
