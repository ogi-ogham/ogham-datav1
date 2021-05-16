# Ogham Data - Crosstables as CSV

## geospatial joins

### ct_barony_townland.csv

-   comma seperated
-   license:
    -   combined: <https://creativecommons.org/licenses/by/4.0/deed.de>
-   method:
    -   PostGIS join

| id_townland | id_barony |
| ----------- | --------- |
| townland id | barony id |

### ct_country_province.csv

-   comma seperated
-   license:
    -   combined: <https://creativecommons.org/licenses/by/4.0/deed.de>
-   method:
    -   PostGIS join

| id_province | id_country |
| ----------- | ---------- |
| province id | country id |

### ct_county_barony.csv

-   comma seperated
-   license:
    -   combined: <https://creativecommons.org/licenses/by/4.0/deed.de>
-   method:
    -   PostGIS join

| id_county | id_barony |
| --------- | --------- |
| county id | barony id |

### ct_province_county.csv

-   comma seperated
-   license:
    -   combined: <https://creativecommons.org/licenses/by/4.0/deed.de>
-   method:
    -   PostGIS join

| id_province | id_county |
| ----------- | --------- |
| province id | county id |

## ogham crosstables

### ct_insc_read.csv

-   comma seperated
-   license:
    -   combined: <https://creativecommons.org/licenses/by/4.0/deed.de>
-   method:
    -   postgres join

| id_insc        | id_read    |
| -------------- | ---------- |
| inscription id | reading id |

### ct_site_barony.csv

-   comma seperated
-   license:
    -   combined: <https://creativecommons.org/licenses/by/4.0/deed.de>
-   method:
    -   PostGIS join

| id_site | id_barony |
| ------- | --------- |
| site id | barony id |

### ct_site_country.csv

-   comma seperated
-   license:
    -   combined: <https://creativecommons.org/licenses/by/4.0/deed.de>
-   method:
    -   PostGIS join

| id_site | id_country |
| ------- | ---------- |
| site id | country id |

### ct_site_country.csv

-   comma seperated
-   license:
    -   combined: <https://creativecommons.org/licenses/by/4.0/deed.de>
-   method:
    -   PostGIS join

| id_site | id_county |
| ------- | --------- |
| site id | county id |

### ct_site_province.csv

-   comma seperated
-   license:
    -   combined: <https://creativecommons.org/licenses/by/4.0/deed.de>
-   method:
    -   PostGIS join

| id_site | id_province |
| ------- | ----------- |
| site id | province id |

### ct_site_townland.csv

-   comma seperated
-   license:
    -   combined: <https://creativecommons.org/licenses/by/4.0/deed.de>
-   method:
    -   PostGIS join

| id_site | id_townland |
| ------- | ----------- |
| site id | townland id |

### ct_site_townland.csv

-   comma seperated
-   license:
    -   combined: <https://creativecommons.org/licenses/by/4.0/deed.de>
-   method:
    -   postgres join

| id_site | id_location |
| ------- | ----------- |
| site id | location id |

### ct_stone_insc.csv

-   comma seperated
-   license:
    -   combined: <https://creativecommons.org/licenses/by/4.0/deed.de>
-   method:
    -   postgres join

| id_stone | id_insc        |
| -------- | -------------- |
| stone id | inscription id |

### ct_stone_person.csv

-   comma seperated
-   license:
    -   combined: <https://creativecommons.org/licenses/by/4.0/deed.de>
-   method:
    -   postgres join

| id_stone | id_person |
| -------- | --------- |
| stone id | person id |

### ct_stone_site.csv

-   comma seperated
-   license:
    -   combined: <https://creativecommons.org/licenses/by/4.0/deed.de>
-   method:
    -   postgres join

| id_stone | id_site |
| -------- | ------- |
| stone id | site id |

### ct_stone_squirrel.csv

-   comma seperated
-   license:
    -   combined: <https://creativecommons.org/licenses/by/4.0/deed.de>
-   method:
    -   postgres join

| id_stone | id_squirrel       |
| -------- | ----------------- |
| stone id | squirrel stone id |

### ct_stone_word.csv

-   comma seperated
-   license:
    -   combined: <https://creativecommons.org/licenses/by/4.0/deed.de>
-   method:
    -   postgres join

| id_stone | id_word |
| -------- | ------- |
| stone id | word id |
