__author__ = "Florian Thiery"
__copyright__ = "MIT Licence 2021, Florian Thiery"
__credits__ = ["Florian Thiery"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Florian Thiery"
__email__ = "mail@fthiery.de"
__status__ = "1.0"
__update__ = "2021-05-13"

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
file_name = "og_stones_references"
dir_path = os.path.dirname(os.path.realpath(__file__))
file_in = dir_path.replace("\\rdf\\py", "\\csv\\ogham") + "\\" + file_name + ".csv"

# read csv file
data = pd.read_csv(
    file_in,
    encoding='utf-8',
    sep=',',
    usecols=['g_id', 'id', 'original_id', 'stone_type', 'cisp_id', 'o3d', 'macalister_1945', 'macalister_1907', 'mcmanus_1991', 'macalister_1902', 'macalister_1897', 'cuppage_1986', 'macalister_1949', 'brash_1879', 'osullivan_1996', 'power_1992', 'macalister_1909', 'petrie_1872', 'brikil_1993', 'raftery_1960', 'okasha_forsyth_2001', 'ferguson_1887', 'power_1997', 'ciic_stone', 'cisp_stone', 'o3d_stone'],
    na_values=['.', '??', 'NULL']  # take any '.' or '??' values as NA
)
print(data.info())

# create triples from dataframe
lineNo = 2
outStr = ""
lines = []
references = []
for index, row in data.iterrows():
    # output things
    tmpno = lineNo - 2
    if tmpno % 1000 == 0:
        print(tmpno)
    lineNo += 1

    # fill cross array
    references_tmp = []
    if str(row['ciic_stone']) != 'nan':
        if str(row['ciic_stone']) != 'undefined':
            references_tmp.append("ogham:Y" + str(int(row['ciic_stone'])))
    if str(row['cisp_stone']) != 'nan':
        if str(row['cisp_stone']) != 'undefined':
            references_tmp.append("ogham:Y" + str(int(row['cisp_stone'])))
    if str(row['o3d_stone']) != 'nan':
        if str(row['o3d_stone']) != 'undefined':
            references_tmp.append("ogham:Y" + str(int(row['o3d_stone'])))
    if str(row['macalister_1945']) != 'nan':
        if str(row['macalister_1945']) != 'undefined':
            references_tmp.append("ogham:macalister_1945:" + str(row['macalister_1945']))
    if str(row['cisp_id']) != 'nan':
        if str(row['cisp_id']) != 'undefined':
            references_tmp.append("ogham:cisp:" + str(row['cisp_id']).replace(" ", "_").replace('/', "_"))
    if str(row['o3d']) != 'nan':
        if str(row['o3d']) != 'undefined':
            references_tmp.append("ogham:o3d:" + str(row['o3d']).replace(" ", "_"))
    if str(row['macalister_1907']) != 'nan':
        if str(row['macalister_1907']) != 'undefined':
            references_tmp.append("ogham:macalister_1907:" + str(int(row['macalister_1907'])))
    if str(row['mcmanus_1991']) != 'nan':
        if str(row['mcmanus_1991']) != 'undefined':
            references_tmp.append("ogham:mcmanus_1991:" + str(row['mcmanus_1991']).replace(" ", "_"))
    if str(row['macalister_1902']) != 'nan':
        if str(row['macalister_1902']) != 'undefined':
            references_tmp.append("ogham:macalister_1902:" + str(int(row['macalister_1902'])))
    if str(row['macalister_1897']) != 'nan':
        if str(row['macalister_1897']) != 'undefined':
            references_tmp.append("ogham:macalister_1897:" + str(int(row['macalister_1897'])))
    if str(row['cuppage_1986']) != 'nan':
        if str(row['cuppage_1986']) != 'undefined':
            references_tmp.append("ogham:cuppage_1986:" + str(row['cuppage_1986']).replace('(', "_").replace(')', "").replace(" ", "_"))
    if str(row['macalister_1949']) != 'nan':
        if str(row['macalister_1949']) != 'undefined':
            references_tmp.append("ogham:macalister_1949:" + str(int(row['macalister_1949'])))
    if str(row['brash_1879']) != 'nan':
        if str(row['brash_1879']) != 'undefined':
            references_tmp.append("ogham:brash_1879:" + str(int(row['brash_1879'])))
    if str(row['osullivan_1996']) != 'nan':
        if str(row['osullivan_1996']) != 'undefined':
            references_tmp.append("ogham:osullivan_1996:" + str(int(row['osullivan_1996'])))
    if str(row['power_1992']) != 'nan':
        if str(row['power_1992']) != 'undefined':
            references_tmp.append("ogham:power_1992:" + str(int(row['power_1992'])))
    if str(row['macalister_1909']) != 'nan':
        if str(row['macalister_1909']) != 'undefined':
            references_tmp.append("ogham:macalister_1909:" + str(int(row['macalister_1909'])))
    if str(row['petrie_1872']) != 'nan':
        if str(row['petrie_1872']) != 'undefined':
            references_tmp.append("ogham:petrie_1872:" + str(int(row['petrie_1872'])))
    if str(row['brikil_1993']) != 'nan':
        if str(row['brikil_1993']) != 'undefined':
            references_tmp.append("ogham:brikil_1993:" + str(int(row['brikil_1993'])))
    if str(row['raftery_1960']) != 'nan':
        if str(row['raftery_1960']) != 'undefined':
            references_tmp.append("ogham:raftery_1960:" + str(int(row['raftery_1960'])))
    if str(row['okasha_forsyth_2001']) != 'nan':
        if str(row['okasha_forsyth_2001']) != 'undefined':
            references_tmp.append("ogham:okasha_forsyth_2001:" + str(row['okasha_forsyth_2001']).replace(" ", "_"))
    if str(row['ferguson_1887']) != 'nan':
        if str(row['ferguson_1887']) != 'undefined':
            references_tmp.append("ogham:ferguson_1887:" + str(int(row['ferguson_1887'])))
    if str(row['power_1997']) != 'nan':
        if str(row['power_1997']) != 'undefined':
            references_tmp.append("ogham:power_1997:" + str(int(row['power_1997'])))

    # reference
    lines.append("_:" + str(row['g_id']) + " " + "rdf:type" + " oghamonto:ReferenceChain .")
    lines.append("_:" + str(row['g_id']) + " " + "oghamonto:referenceList \"" + str(references_tmp) + "\" .")

    # create initial nodes
    if int(str(row['id'])) > 10000000 and int(str(row['id'])) < 20000000:
        lines.append("ogham:ciic:" + str(row['id']) + " " + "rdf:type" + " oghamonto:" + "macalister_1945" + " .")
        lines.append("ogham:ciic:" + str(row['id']) + " " + "rdfs:label" + " 'ciic:" + str(row['id']) + "' .")
    if int(str(row['id'])) > 20000000 and int(str(row['id'])) < 30000000:
        lines.append("ogham:cisp:" + str(row['id']) + " " + "rdf:type" + " oghamonto:" + "CISP" + " .")
        lines.append("ogham:cisp:" + str(row['id']) + " " + "rdfs:label" + " 'cisp:" + str(row['id']) + "' .")
    if int(str(row['id'])) > 30000000 and int(str(row['id'])) < 40000000:
        lines.append("ogham:o3d:" + str(row['id']) + " " + "rdf:type" + " oghamonto:" + "OghamIn3D" + " .")
        lines.append("ogham:o3d:" + str(row['id']) + " " + "rdfs:label" + " 'o3d:" + str(row['id']) + "' .")
    if int(str(row['id'])) > 50000000 and int(str(row['id'])) < 60000000:
        lines.append("ogham:squirrel:" + str(row['id']) + " " + "rdf:type" + " oghamonto:" + "SquirrelOgham" + " .")
        lines.append("ogham:squirrel:" + str(row['id']) + " " + "rdfs:label" + " 'squirrel:" + str(row['id']) + "' .")

    # create reference nodes
    for x in references_tmp:
        split = x.split(":")
        tmp = x + " " + "rdf:type" + " oghamonto:" + split[1] + " ."
        if ":Y" not in x and tmp not in lines:
            lines.append(x + " " + "rdf:type" + " oghamonto:" + split[1] + " .")
            lines.append(x + " " + "rdfs:label" + " '" + str(x).replace("ogham:", "") + "' .")

    # create edges nodes
    for x in references_tmp:
        for y in references_tmp:
            tmp = x + " " + "oghamonto:equals" + " " + y + "" + "."
            if x != y and tmp not in lines:
                lines.append(x + " " + "oghamonto:equals" + " " + y + "" + ".")

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
