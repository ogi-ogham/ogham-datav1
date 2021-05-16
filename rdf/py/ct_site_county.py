__author__ = "Florian Thiery"
__copyright__ = "MIT Licence 2021, Florian Thiery"
__credits__ = ["Florian Thiery"]
__license__ = "MIT"
__version__ = "beta"
__maintainer__ = "Florian Thiery"
__email__ = "mail@fthiery.de"
__status__ = "beta"
__update__ = "2021-05-11"

# import dependencies
import uuid
import requests
import io
import pandas as pd
import os
import codecs
import datetime
import importlib
import sys
import hashlib
import _config

# set UTF8 as default
importlib.reload(sys)
print("*****************************************")

# set starttime
starttime = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")

# set paths
file_name = "ct_site_county"
dir_path = os.path.dirname(os.path.realpath(__file__))
file_in = dir_path.replace("\\rdf\\py", "\\csv\\crosstable") + "\\" + file_name + ".csv"

# read csv file
data = pd.read_csv(
    file_in,
    encoding='utf-8',
    sep=',',
    usecols=['id_site', 'id_county'],
    na_values=['.', '??', 'NULL']  # take any '.' or '??' values as NA
)
print(data.info())

# create triples from dataframe
lineNo = 2
outStr = ""
lines = []
for index, row in data.iterrows():
    lines.append("ogham:OS" + str(row['id_site']) + " oghamonto:within " + "ogham:GSD" + str(row['id_county']) + " .")

files = (len(lines) / 100000) + 1
print("triples", len(lines), "files", int(files))
thiscount = len(lines)
_config.count(thiscount)

# write output files
f = 0
step = 100000
fileprefix = file_name + "_"
prefixes = ""
prefixes += "@prefix oghamonto: <http://ontology.ogham.link/> .\r\n"
prefixes += "@prefix ogham: <http://lod.ogham.link/data/> .\r\n"
prefixes += "\r\n"

for x in range(1, int(files) + 1):
    strX = str(x)
    filename = dir_path.replace("\\py", "\\crosstable") + "\\" + fileprefix + strX + ".ttl"
    file = codecs.open(filename, "w", "utf-8")
    file.write("# create triples from " + file_name + ".csv \r\n")
    file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
    file.write(prefixes)
    i = f
    for i, line in enumerate(lines):
        if (i > f - 1 and i < f + step):
            file.write(line)
            file.write("\r\n")
    f = f + step
    print(" > " + fileprefix + strX + ".ttl")
    file.close()

print("*****************************************")
print("SUCCESS: closing script")
print("*****************************************")
