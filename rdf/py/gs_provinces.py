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
file_name = "gs_provinces"
dir_path = os.path.dirname(os.path.realpath(__file__))
file_in = dir_path.replace("\\rdf\\py", "\\csv\\geodata") + "\\" + file_name + ".csv"

# read csv file
data = pd.read_csv(
    file_in,
    encoding='utf-8',
    sep=',',
    usecols=['id', 'label', 'wikidata_id', 'wkt'],
    na_values=['.', '??', 'NULL']  # take any '.' or '??' values as NA
)
print(data.info())

# create triples from dataframe
lineNo = 2
outStr = ""
lines = []
for index, row in data.iterrows():
    # print(lineNo)
    tmpno = lineNo - 2
    if tmpno % 1000 == 0:
        print(tmpno)
    lineNo += 1
    # info
    lines.append("ogham:GSD" + str(row['id']) + " " + "rdf:type" + " oghamonto:Province .")
    lines.append("ogham:GSD" + str(row['id']) + " " + "rdf:type" + " <http://www.opengis.net/ont/geosparql#Feature> .")
    lines.append("ogham:GSD" + str(row['id']) + " " + "rdfs:label" + " " + "'" + str(row['label']) + "'@en" + ".")
    lines.append("ogham:GSD" + str(row['id']) + " " + "oghamonto:exactMatch" + " wd:" + str(row['wikidata_id']) + " .")
    # geom
    lines.append("ogham:GSD" + str(row['id']) + " " + "geosparql:hasGeometry" + " ogham:GSD" + str(row['id']) + "_geom .")
    lines.append("ogham:GSD" + str(row['id']) + "_geom " + "rdf:type" + " sf:MultiPolygon .")
    geom = "\"" + str(row['wkt']) + "\"^^geosparql:wktLiteral"
    lines.append("ogham:GSD" + str(row['id']) + "_geom " + "geosparql:asWKT " + geom + ".")
    lines.append("ogham:GSD" + str(row['id']) + "_geom " + "oghamonto:hasEPSG " + "<http://www.opengis.net/def/crs/EPSG/0/4326>" + ".")
    # license
    lines.append("ogham:GSD" + str(row['id']) + " " + "dct:license" + " <" + "https://creativecommons.org/licenses/by-sa/4.0/deed.de" + "> .")
    lines.append("ogham:GSD" + str(row['id']) + " " + "dct:license" + " <" + "http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/" + "> .")
    lines.append("ogham:GSD" + str(row['id']) + " " + "dct:creator" + " <" + "https://orcid.org/0000-0002-3246-3531" + "> .")
    lines.append("ogham:GSD" + str(row['id']) + " " + "dct:rightsHolder" + " wd:Q3355441 .")  # OSi
    lines.append("ogham:GSD" + str(row['id']) + " " + "dct:rightsHolder" + " wd:Q7100893 .")  # OSNI
    # prov-o
    lines.append("ogham:GSD" + str(row['id']) + " " + "prov:wasAttributedTo" + " ogham:PythonStonesCIIC .")
    lines.append("ogham:GSD" + str(row['id']) + " " + "prov:wasDerivedFrom" + " <https://github.com/ogi-ogham/ogham-datav1/blob/main/csv/geodata/" + file_name + ".csv> .")
    lines.append("<https://github.com/ogi-ogham/ogham-datav1/blob/main/csv/geodata/" + file_name + ".csv> " + "prov:wasDerivedFrom" + " <https://www.opendatani.gov.uk/dataset/osni-open-data-largescale-boundaries-ni-outline> .")
    lines.append("<https://github.com/ogi-ogham/ogham-datav1/blob/main/csv/geodata/" + file_name + ".csv> " + "prov:wasDerivedFrom" + " <https://data-osi.opendata.arcgis.com/datasets/provinces-osi-national-statutory-boundaries-generalised-20m?geometry=-29.165%2C51.112%2C12.649%2C55.691> .")
    lines.append("<https://github.com/ogi-ogham/ogham-datav1/blob/main/csv/geodata/" + file_name + ".csv> " + "prov:wasAttributedTo" + " wd:Q3355441 .")  # OSNI
    lines.append("<https://github.com/ogi-ogham/ogham-datav1/blob/main/csv/geodata/" + file_name + ".csv> " + "prov:wasAttributedTo" + " wd:Q3355441 .")  # OSi
    lines.append("ogham:GSD" + str(row['id']) + " " + "prov:wasGeneratedBy" + " ogham:GSD" + str(row['id']) + "_activity .")
    lines.append("ogham:GSD" + str(row['id']) + "_activity " + "rdf:type" + " prov:Activity .")
    lines.append("ogham:GSD" + str(row['id']) + "_activity " + "prov:startedAtTime '" + starttime + "'^^xsd:dateTime .")
    lines.append("ogham:GSD" + str(row['id']) + "_activity " + "prov:endedAtTime '" + datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "'^^xsd:dateTime .")
    lines.append("ogham:GSD" + str(row['id']) + "_activity " + "prov:wasAssociatedWith" + " ogham:PythonStonesCIIC .")
    lines.append("")

files = (len(lines) / 100000) + 1
print("triples", len(lines), "files", int(files))
thiscount = len(lines)
_config.count(thiscount)

# write output files
f = 0
step = 100000
fileprefix = file_name + "_"
prefixes = ""
prefixes += "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\r\n"
prefixes += "@prefix owl: <http://www.w3.org/2002/07/owl#> .\r\n"
prefixes += "@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\r\n"
prefixes += "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\r\n"
prefixes += "@prefix geosparql: <http://www.opengis.net/ont/geosparql#> .\r\n"
prefixes += "@prefix dc: <http://purl.org/dc/elements/1.1/> .\r\n"
prefixes += "@prefix dct: <http://purl.org/dc/terms/> .\r\n"
prefixes += "@prefix sf: <http://www.opengis.net/ont/sf#> .\r\n"
prefixes += "@prefix prov: <http://www.w3.org/ns/prov#> .\r\n"
prefixes += "@prefix oghamonto: <http://ontology.ogham.link/> .\r\n"
prefixes += "@prefix ogham: <http://lod.ogham.link/data/> .\r\n"
prefixes += "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .\r\n"
prefixes += "@prefix wd: <http://www.wikidata.org/entity/> .\r\n"
prefixes += "\r\n"

for x in range(1, int(files) + 1):
    strX = str(x)
    filename = dir_path.replace("\\py", "\\geodata") + "\\" + fileprefix + strX + ".ttl"
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
