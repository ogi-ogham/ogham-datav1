__author__ = "Florian Thiery"
__copyright__ = "MIT Licence 2021, Florian Thiery"
__credits__ = ["Florian Thiery"]
__license__ = "MIT"
__version__ = "beta"
__maintainer__ = "Florian Thiery"
__email__ = "mail@fthiery.de"
__status__ = "beta"
__update__ = "2021-05-28"

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
file_name = "og_sites"
dir_path = os.path.dirname(os.path.realpath(__file__))
file_in = dir_path.replace("\\rdf\\py", "\\csv\\ogham") + "\\" + file_name + ".csv"

# read csv file
data = pd.read_csv(
    file_in,
    encoding='utf-8',
    sep=',',
    usecols=['id', 'label', 'wkt', 'wikidata_id', 'townland_label', 'barony_label', 'county_label', 'province_label', 'country_label'],
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
    lines.append("ogham:OS" + str(row['id']) + " " + "rdf:type" + " oghamonto:OghamSite .")
    lines.append("ogham:OS" + str(row['id']) + " " + "rdf:type" + " <https://pleiades.stoa.org/places/vocab#Place> .")
    lines.append("ogham:OS" + str(row['id']) + " " + "rdfs:label" + " " + "'" + str(row['label']).replace("'", "`") + "'@en" + ".")
    lines.append("ogham:OS" + str(row['id']) + " " + "oghamonto:exactMatch" + " wd:" + str(row['wikidata_id']) + " .")
    lines.append("ogham:OS" + str(row['id']) + " " + "oghamonto:label_townland" + " " + "'" + str(row['townland_label']).replace("'", "`") + "'" + ".")
    lines.append("ogham:OS" + str(row['id']) + " " + "oghamonto:label_barony" + " " + "'" + str(row['barony_label']).replace("'", "`") + "'" + ".")
    lines.append("ogham:OS" + str(row['id']) + " " + "oghamonto:label_county" + " " + "'" + str(row['county_label']).replace("'", "`") + "'" + ".")
    lines.append("ogham:OS" + str(row['id']) + " " + "oghamonto:label_province" + " " + "'" + str(row['province_label']).replace("'", "`") + "'" + ".")
    lines.append("ogham:OS" + str(row['id']) + " " + "oghamonto:label_country" + " " + "'" + str(row['country_label']).replace("'", "`") + "'" + ".")
    # geom
    lines.append("ogham:OS" + str(row['id']) + " " + "geosparql:hasGeometry" + " ogham:OS" + str(row['id']) + "_geom .")
    lines.append("ogham:OS" + str(row['id']) + " " + "oghamonto:representativePoint" + " ogham:OS" + str(row['id']) + "_geom .")
    lines.append("ogham:OS" + str(row['id']) + "_geom " + "rdf:type" + " sf:Point .")
    point = "\"" + str(row['wkt']) + "\"^^geosparql:wktLiteral"
    lines.append("ogham:OS" + str(row['id']) + "_geom " + "geosparql:asWKT " + point + ".")
    lines.append("ogham:OS" + str(row['id']) + "_geom " + "oghamonto:hasEPSG " + "<http://www.opengis.net/def/crs/EPSG/0/4326>" + ".")
    # license
    lines.append("ogham:OS" + str(row['id']) + " " + "dct:license" + " <" + "https://creativecommons.org/licenses/by/4.0/deed.de" + "> .")
    lines.append("ogham:OS" + str(row['id']) + " " + "dct:creator" + " <" + "https://orcid.org/0000-0002-3246-3531" + "> .")
    lines.append("ogham:OS" + str(row['id']) + " " + "dct:rightsHolder" + " <" + "https://orcid.org/0000-0002-3246-3531" + "> .")  # FT
    lines.append("ogham:OS" + str(row['id']) + " " + "dct:rightsHolder" + " <" + "https://orcid.org/0000-0003-4696-2101" + "> .")  # SCS
    lines.append("ogham:OS" + str(row['id']) + " " + "dct:rightsHolder" + " wd:Q85384744 .")  # townland-ie
    # prov-o
    lines.append("ogham:OS" + str(row['id']) + " " + "prov:wasAttributedTo" + " ogham:PythonStonesCIIC .")
    lines.append("ogham:OS" + str(row['id']) + " " + "prov:wasDerivedFrom" + " <https://github.com/ogi-ogham/ogham-datav1/blob/main/csv/ogham/" + file_name + ".csv> .")
    lines.append("<https://github.com/ogi-ogham/ogham-datav1/blob/main/csv/ogham/" + file_name + ".csv> " + "prov:wasDerivedFrom" + " <https://www.townlands.ie> .")
    lines.append("<https://github.com/ogi-ogham/ogham-datav1/blob/main/csv/ogham/" + file_name + ".csv> " + "prov:wasAttributedTo" + " wd:Q85384744 .")
    lines.append("ogham:OS" + str(row['id']) + " " + "prov:wasGeneratedBy" + " ogham:OS" + str(row['id']) + "_activity .")
    lines.append("ogham:OS" + str(row['id']) + "_activity " + "rdf:type" + " prov:Activity .")
    lines.append("ogham:OS" + str(row['id']) + "_activity " + "prov:startedAtTime '" + starttime + "'^^xsd:dateTime .")
    lines.append("ogham:OS" + str(row['id']) + "_activity " + "prov:endedAtTime '" + datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "'^^xsd:dateTime .")
    lines.append("ogham:OS" + str(row['id']) + "_activity " + "prov:wasAssociatedWith" + " ogham:PythonStonesCIIC .")
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
    filename = dir_path.replace("\\py", "\\ogham") + "\\" + fileprefix + strX + ".ttl"
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
