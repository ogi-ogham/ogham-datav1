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
file_name = "og_stones"
dir_path = os.path.dirname(os.path.realpath(__file__))
file_in = dir_path.replace("\\rdf\\py", "\\csv\\ogham") + "\\" + file_name + ".csv"

# read csv file
data = pd.read_csv(
    file_in,
    encoding='utf-8',
    sep=',',
    usecols=['id', 'label', 'desc', 'wikidata_id', 'original_id', 'width', 'height', 'depth', 'thickness', 'h_status', 'w_status', 't_status', 'discovery_year', 'discovery_who', 'currentsetting', 'currentlocation', 'form', 'completeness', 'preservation', 'preservation_note', 'smr_no'],
    na_values=['.', '??', 'NULL']  # take any '.' or '??' values as NA
)
print(data.info())

# create triples from dataframe
lineNo = 2
outStr = ""
lines = []
for index, row in data.iterrows():
    tmpno = lineNo - 2
    if tmpno % 1000 == 0:
        print(tmpno)
    lineNo += 1
    # info
    lines.append("ogham:Y" + str(row['id']) + " " + "rdf:type" + " oghamonto:OghamStone .")
    fullstring = str(row['label'])
    mode = ""
    if "Macalister" in fullstring:
        lines.append("ogham:Y" + str(row['id']) + " " + "rdf:type" + " oghamonto:OghamStone_CIIC .")
        mode = "ciic"
    elif "CISP" in fullstring:
        lines.append("ogham:Y" + str(row['id']) + " " + "rdf:type" + " oghamonto:OghamStone_CISP .")
        mode = "cisp"
    elif "3D" in fullstring:
        lines.append("ogham:Y" + str(row['id']) + " " + "rdf:type" + " oghamonto:OghamStone_O3D .")
        mode = "o3d"
    elif "Squirrel" in fullstring:
        lines.append("ogham:Y" + str(row['id']) + " " + "rdf:type" + " oghamonto:OghamStone_Squirrel .")
        mode = "squirrel"
    lines.append("ogham:Y" + str(row['id']) + " " + "rdfs:label" + " " + "'" + str(row['label']) + "'@en" + ".")
    lines.append("ogham:Y" + str(row['id']) + " " + "rdfs:comment" + " " + "'" + str(row['desc']) + "'@en" + ".")
    lines.append("ogham:Y" + str(row['id']) + " " + "oghamonto:exactMatch" + " wd:" + str(row['wikidata_id']) + " .")
    lines.append("ogham:Y" + str(row['id']) + " " + "dc:identifier " + "'" + str(row['original_id']) + "' .")
    if str(row['width']) != 'nan':
        if str(row['width']) != 'undefined':
            lines.append("ogham:Y" + str(row['id']) + " " + "oghamonto:width" + " " + "" + str(row['width']) + "" + ".")
    if str(row['height']) != 'nan':
        if str(row['height']) != 'undefined':
            lines.append("ogham:Y" + str(row['id']) + " " + "oghamonto:height" + " " + "" + str(row['height']) + "" + ".")
    if str(row['depth']) != 'nan':
        if str(row['depth']) != 'undefined':
            lines.append("ogham:Y" + str(row['id']) + " " + "oghamonto:depth" + " " + "" + str(row['depth']) + "" + ".")
    if str(row['thickness']) != 'nan':
        if str(row['thickness']) != 'undefined':
            lines.append("ogham:Y" + str(row['id']) + " " + "oghamonto:thickness" + " " + "" + str(row['thickness']) + "" + ".")
    if str(row['h_status']) != 'nan':
        if str(row['h_status']) != 'undefined':
            lines.append("ogham:Y" + str(row['id']) + " " + "oghamonto:h_status" + " " + "'" + str(row['h_status']) + "'" + ".")
    if str(row['w_status']) != 'nan':
        if str(row['w_status']) != 'undefined':
            lines.append("ogham:Y" + str(row['id']) + " " + "oghamonto:w_status" + " " + "'" + str(row['w_status']) + "'" + ".")
    if str(row['t_status']) != 'nan':
        if str(row['t_status']) != 'undefined':
            lines.append("ogham:Y" + str(row['id']) + " " + "oghamonto:t_status" + " " + "'" + str(row['t_status']) + "'" + ".")
    if str(row['discovery_year']) != 'nan':
        if str(row['discovery_year']) != 'undefined':
            lines.append("ogham:Y" + str(row['id']) + " " + "oghamonto:discovery_year" + " " + "'" + str(int(row['discovery_year'])) + "'" + ".")
    if str(row['discovery_who']) != 'nan':
        if str(row['discovery_who']) != 'undefined':
            lines.append("ogham:Y" + str(row['id']) + " " + "oghamonto:discovery_who" + " " + "'" + str(row['discovery_who']) + "'" + ".")
    if str(row['currentsetting']) != 'nan':
        if str(row['currentsetting']) != 'undefined':
            lines.append("ogham:Y" + str(row['id']) + " " + "oghamonto:currentsetting" + " " + "'" + str(row['currentsetting']) + "'" + ".")
    if str(row['currentlocation']) != 'nan':
        if str(row['currentlocation']) != 'undefined':
            lines.append("ogham:Y" + str(row['id']) + " " + "oghamonto:currentlocation" + " " + "'" + str(row['currentlocation']) + "'" + ".")
    if str(row['form']) != 'nan':
        if str(row['form']) != 'undefined':
            lines.append("ogham:Y" + str(row['id']) + " " + "oghamonto:form" + " " + "'" + str(row['form']) + "'" + ".")
    if str(row['completeness']) != 'nan':
        if str(row['completeness']) != 'undefined':
            lines.append("ogham:Y" + str(row['id']) + " " + "oghamonto:completeness" + " " + "'" + str(row['completeness']) + "'" + ".")
    if str(row['preservation']) != 'nan':
        if str(row['preservation']) != 'undefined':
            lines.append("ogham:Y" + str(row['id']) + " " + "oghamonto:preservation" + " " + "'" + str(row['preservation']) + "'" + ".")
    if str(row['preservation_note']) != 'nan':
        if str(row['preservation_note']) != 'undefined':
            lines.append("ogham:Y" + str(row['id']) + " " + "oghamonto:preservation_note" + " " + "'" + str(row['preservation_note']) + "'" + ".")
    if str(row['smr_no']) != 'nan':
        if str(row['smr_no']) != 'undefined':
            lines.append("ogham:Y" + str(row['id']) + " " + "oghamonto:smr_no" + " " + "'" + str(row['smr_no']) + "'" + ".")
    # license
    if mode == "ciic":
        lines.append("ogham:Y" + str(row['id']) + " " + "dct:license" + " <" + "https://creativecommons.org/licenses/by/4.0/deed.de" + "> .")
        lines.append("ogham:Y" + str(row['id']) + " " + "dct:creator" + " <" + "https://orcid.org/0000-0002-3246-3531" + "> .")
        lines.append("ogham:Y" + str(row['id']) + " " + "dct:rightsHolder" + " <" + "https://orcid.org/0000-0002-3246-3531" + "> .")  # FT
        lines.append("ogham:Y" + str(row['id']) + " " + "dct:rightsHolder" + " <" + "https://orcid.org/0000-0003-4696-2101" + "> .")  # SCS
    elif mode == "o3d":
        lines.append("ogham:Y" + str(row['id']) + " " + "dct:license" + " <" + "http://creativecommons.org/licenses/by-nc-sa/3.0/ie/deed.en_US" + "> .")
        lines.append("ogham:Y" + str(row['id']) + " " + "dct:creator" + " <" + "https://orcid.org/0000-0002-3246-3531" + "> .")
        lines.append("ogham:Y" + str(row['id']) + " " + "dct:rightsHolder" + " <" + "https://orcid.org/0000-0002-3246-3531" + "> .")
        lines.append("ogham:Y" + str(row['id']) + " " + "dct:rightsHolder" + " wd:Q106674066 .")  # o3d
    elif mode == "cisp":
        lines.append("ogham:Y" + str(row['id']) + " " + "dct:license" + " <" + "https://creativecommons.org/licenses/by/4.0/deed.de" + "> .")
        lines.append("ogham:Y" + str(row['id']) + " " + "dct:creator" + " <" + "https://orcid.org/0000-0002-3246-3531" + "> .")
        lines.append("ogham:Y" + str(row['id']) + " " + "dct:rightsHolder" + " <" + "https://orcid.org/0000-0002-3246-3531" + "> .")
        lines.append("ogham:Y" + str(row['id']) + " " + "dct:rightsHolder" + " wd:Q106628017 .")  # cisp
    elif mode == "squirrel":
        lines.append("ogham:Y" + str(row['id']) + " " + "dct:license" + " <" + "https://creativecommons.org/licenses/by/4.0/deed.de" + "> .")
        lines.append("ogham:Y" + str(row['id']) + " " + "dct:creator" + " <" + "https://orcid.org/0000-0002-3246-3531" + "> .")
        lines.append("ogham:Y" + str(row['id']) + " " + "dct:rightsHolder" + " <" + "https://orcid.org/0000-0002-3246-3531" + "> .")  # FT
        lines.append("ogham:Y" + str(row['id']) + " " + "dct:rightsHolder" + " <" + "https://orcid.org/0000-0003-4696-2101" + "> .")  # SCS
    # prov-o
    lines.append("ogham:Y" + str(row['id']) + " " + "prov:wasAttributedTo" + " ogham:PythonStonesCIIC .")
    lines.append("ogham:Y" + str(row['id']) + " " + "prov:wasDerivedFrom" + " <https://github.com/ogi-ogham/ogham-datav1/blob/main/csv/ogham/" + file_name + ".csv> .")
    lines.append("<https://github.com/ogi-ogham/ogham-datav1/blob/main/csv/ogham/" + file_name + ".csv> " + "prov:wasDerivedFrom" + " <" + "https://www.ucl.ac.uk/archaeology/cisp/database/" + "> .")
    lines.append("<https://github.com/ogi-ogham/ogham-datav1/blob/main/csv/ogham/" + file_name + ".csv> " + "prov:wasDerivedFrom" + " <" + "https://ogham.celt.dias.ie/menu.php?lang=en&menuitem=81&overviewinfo=file" + "> .")
    lines.append("<https://github.com/ogi-ogham/ogham-datav1/blob/main/csv/ogham/" + file_name + ".csv> " + "prov:wasDerivedFrom" + " wd:Q70256237 .")
    lines.append("<https://github.com/ogi-ogham/ogham-datav1/blob/main/csv/ogham/" + file_name + ".csv> " + "prov:wasAttributedTo" + " wd:Q106628017 .")
    lines.append("<https://github.com/ogi-ogham/ogham-datav1/blob/main/csv/ogham/" + file_name + ".csv> " + "prov:wasAttributedTo" + " wd:Q106674066 .")
    lines.append("<https://github.com/ogi-ogham/ogham-datav1/blob/main/csv/ogham/" + file_name + ".csv> " + "prov:wasAttributedTo" + " wd:Q70256237 .")
    lines.append("ogham:Y" + str(row['id']) + " " + "prov:wasGeneratedBy" + " ogham:Y" + str(row['id']) + "_activity .")
    lines.append("ogham:Y" + str(row['id']) + "_activity " + "rdf:type" + " prov:Activity .")
    lines.append("ogham:Y" + str(row['id']) + "_activity " + "prov:startedAtTime '" + starttime + "'^^xsd:dateTime .")
    lines.append("ogham:Y" + str(row['id']) + "_activity " + "prov:endedAtTime '" + datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "'^^xsd:dateTime .")
    lines.append("ogham:Y" + str(row['id']) + "_activity " + "prov:wasAssociatedWith" + " ogham:PythonStonesCIIC .")
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
