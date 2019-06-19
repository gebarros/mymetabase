#-*- coding: UTF-8 -*-

import sys

input_table = open(sys.argv[1], 'r')
output = open("01_insert_eleicoes_data.sql", "w")

output.write("BEGIN;\nUSE metabase;\n")

for i in input_table:
    line = i.strip()
    if not line.startswith("Sigla"):
        
        fields = line.split("\t")
        if len(fields) == 3:
            
            fields.extend([0,0,0,0,0])

        state_code = fields[0]
        city = fields[2]
        n_eleitores2010 = fields[3]
        n_eleitores2012 = fields[4]
        n_eleitores2014 = fields[5]
        n_eleitores2016 = fields[6]
        n_eleitores2018 = fields[7]

        
        
        if not n_eleitores2010:
            n_eleitores2010 = 0
        if not n_eleitores2012:
            n_eleitores2012 = 0
        if not n_eleitores2014:
            n_eleitores2014 = 0
        if not n_eleitores2016:
            n_eleitores2016 = 0
        if not n_eleitores2018:
            n_eleitores2018 = 0

        output.write('INSERT INTO n_eleitores (id,state_code,city,n_eleitores2010,n_eleitores2012,n_eleitores2014,n_eleitores2016,n_eleitores2018) VALUES (NULL,"{}","{}",{},{},{},{},{});\n'.format(state_code,city,\
            n_eleitores2010,n_eleitores2012,n_eleitores2014,n_eleitores2016,n_eleitores2018))

output.write("COMMIT;\n")

input_table.close()
output.close()
