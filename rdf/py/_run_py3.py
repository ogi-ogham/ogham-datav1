__author__ = "Florian Thiery"
__copyright__ = "MIT Licence 2021, Florian Thiery"
__credits__ = ["Florian Thiery"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Florian Thiery"
__email__ = "mail@fthiery.de"
__status__ = "1.0"
__update__ = "2021-05-11"

import glob
import os
import os.path

dir_path = os.path.dirname(os.path.realpath(__file__))
print("start _run_py3.py...")
dir_path_ttl1 = dir_path.replace("\\py", "\\ogham")
filelist1 = glob.glob(os.path.join(dir_path_ttl1, "*.ttl"))
for f in filelist1:
    os.remove(f)
dir_path_ttl2 = dir_path.replace("\\py", "\\geodata")
filelist2 = glob.glob(os.path.join(dir_path_ttl2, "*.ttl"))
for f in filelist2:
    os.remove(f)
dir_path_ttl3 = dir_path.replace("\\py", "\\crosstable")
filelist3 = glob.glob(os.path.join(dir_path_ttl3, "*.ttl"))
for f in filelist3:
    os.remove(f)
print("removed all ttl files...")

# ogham

exec(open(dir_path + "/og_sites.py").read())
exec(open(dir_path + "/og_inscriptions.py").read())
exec(open(dir_path + "/og_locations.py").read())
exec(open(dir_path + "/og_persons.py").read())
exec(open(dir_path + "/og_readings.py").read())
exec(open(dir_path + "/og_stones.py").read())
exec(open(dir_path + "/og_words.py").read())

sum_ogham = int(_config.count(0))

# geodata

exec(open(dir_path + "/gs_baronies.py").read())
exec(open(dir_path + "/gs_counties.py").read())
exec(open(dir_path + "/gs_countries.py").read())
exec(open(dir_path + "/gs_ireland_island.py").read())
exec(open(dir_path + "/gs_provinces.py").read())
exec(open(dir_path + "/gs_townlands.py").read())

step2 = int(_config.count(0))
sum_geodata = step2 - sum_ogham

# crostables

exec(open(dir_path + "/ct_barony_townland.py").read())
exec(open(dir_path + "/ct_province_county.py").read())
exec(open(dir_path + "/ct_county_barony.py").read())
exec(open(dir_path + "/ct_insc_read.py").read())
exec(open(dir_path + "/ct_site_barony.py").read())
exec(open(dir_path + "/ct_site_country.py").read())
exec(open(dir_path + "/ct_site_county.py").read())
exec(open(dir_path + "/ct_site_loc.py").read())
exec(open(dir_path + "/ct_site_province.py").read())
exec(open(dir_path + "/ct_site_townland.py").read())
exec(open(dir_path + "/ct_stone_insc.py").read())
exec(open(dir_path + "/ct_stone_person.py").read())
exec(open(dir_path + "/ct_stone_site.py").read())
exec(open(dir_path + "/ct_stone_squirrel.py").read())
exec(open(dir_path + "/ct_stone_word.py").read())

step3 = int(_config.count(0))
sum_crosstable = step3 - sum_ogham - sum_geodata

# references

exec(open(dir_path + "/og_stones_references.py").read())


print("SUM TRIPLES OGHAM: " + str(sum_ogham))
print("SUM TRIPLES GEODATA: " + str(sum_geodata))
print("SUM TRIPLES CROSSTABLES: " + str(sum_crosstable))
print("SUM TRIPLES: " + str(_config.count(0)))
