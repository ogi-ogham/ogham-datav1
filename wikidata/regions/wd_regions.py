__author__ = "Florian Thiery"
__copyright__ = "MIT Licence 2022, Florian Thiery"
__credits__ = ["Florian Thiery"]
__license__ = "MIT"
__version__ = "beta"
__maintainer__ = "Florian Thiery"
__email__ = "mail@fthiery.de"
__status__ = "beta"
__update__ = "2022-12-12"

# import dependencies
import uuid
import requests
import io
import pandas as pd
import os
import codecs
import datetime
import importlib  # py3
import sys

# set UTF8 as default
importlib.reload(sys)  # py3
# reload(sys) #py2

# uncomment the line below when using Python version <3.0
# sys.setdefaultencoding('UTF8')

# set starttime
starttime = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")

# set input csv
starttime = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")

# set input csv
file_name = "wd_regions.csv"
dir_path = os.path.dirname(os.path.realpath(__file__))
file_in = dir_path + "\\" + file_name

# read csv file
data = pd.read_csv(
    file_in,
    encoding='utf-8',
    sep='|',
    usecols=['label', 'desc', 'wc'],
    na_values=['.', '??']  # take any '.' or '??' values as NA
)
print(data.info())

# create triples from dataframe
lineNo = 2
outStr = ""
lines = []
for index, row in data.iterrows():
    # print(lineNo)
    tmpno = lineNo - 2
    if tmpno % 10 == 0:
        print(tmpno)
    lineNo += 1
    # QS
    lines.append("CREATE")
    lines.append("LAST" + "\t" + "Len" + "\t" + "\"" + str(row["label"]) + "\"")
    lines.append("LAST" + "\t" + "Den" + "\t" + "\"" + str(row["desc"]) + "\"")
    lines.append("LAST" + "\t" + "P31" + "\t" + "Q110897622")
    lines.append("LAST" + "\t" + "P31" + "\t" + "Q839954")
    lines.append("LAST" + "\t" + "P361" + "\t" + "Q100530634")
    lines.append("LAST" + "\t" + "P361" + "\t" + "Q70873595")
    lines.append("LAST" + "\t" + "P3896" + "\t" + "\"" + "" + str(row["wc"]).replace("_", " ") + "\"" + "\t" + "S248" + "\t" + "Q100530634")

files = (len(lines) / 100000) + 1
print("lines", len(lines), "files", int(files))

# set output path
dir_path = os.path.dirname(os.path.realpath(__file__))

# write output files
print("start writing QS file")

f = 0
step = 100000
fileprefix = "wd_regions"
for x in range(1, int(files) + 1):
    filename = dir_path + "\\" + fileprefix + ".qs"
    file = codecs.open(filename, "w", "utf-8")
    i = f
    for i, line in enumerate(lines):
        if (i > f - 1 and i < f + step):
            file.write(line)
            file.write("\r\n")
    f = f + step
    print("Yuhu! > " + fileprefix + ".qs")
    file.close()

print("*****************************************")
print("SUCCESS")
print("closing script")
print("*****************************************")
