# Catherine Morgan, Roger T Webb, Mathew J Carr, Evangelos Kontopantelis, Carolyn A Chew-Graham, Nav Kapur, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"Eu33200","system":"readv2"},{"code":"Eu33.00","system":"readv2"},{"code":"Eu33400","system":"readv2"},{"code":"Eu33.12","system":"readv2"},{"code":"Eu32z14","system":"readv2"},{"code":"Eu32A00","system":"readv2"},{"code":"Eu33100","system":"readv2"},{"code":"Eu33.13","system":"readv2"},{"code":"Eu33z00","system":"readv2"},{"code":"Eu33000","system":"readv2"},{"code":"Eu33316","system":"readv2"},{"code":"Eu3y111","system":"readv2"},{"code":"Eu33313","system":"readv2"},{"code":"Eu33314","system":"readv2"},{"code":"Eu33.11","system":"readv2"},{"code":"Eu33315","system":"readv2"},{"code":"Eu33300","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('depression-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["depression-xrecurr---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["depression-xrecurr---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["depression-xrecurr---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
