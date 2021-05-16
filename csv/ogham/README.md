# Ogham Data - Ogham Data as CSV

## Words (og_words.csv)

-   comma seperated
-   license:
    -   combined: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de>)
-   origin:
    -   [A Guide to Ogam (Q70310399)](https://www.wikidata.org/wiki/Q70310399)
-   method:
    -   manual digitalisation

| id          | label | translation            | reference            | variants | context             | wikidata_id           | wikidata_type      |
| ----------- | ----- | ---------------------- | -------------------- | -------- | ------------------- | --------------------- | ------------------ |
| internal id | label | translation to english | reference to McManus | aliases  | inscription context | Wikidata Q Identifier | Wikidata word type |

## Persons (og_persons.csv)

-   comma seperated
-   license:
    -   combined: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de>)
-   origin:
    -   [Celtic Inscribed Stones Project (Q106628017)](https://www.wikidata.org/wiki/Q106628017)
    -   [Ogham in 3D Project (Q106674066)](https://www.wikidata.org/wiki/Q106674066)
-   method:
    -   semi-automatic digitalisation from HTML / XML

| id          | label | name_caps      |
| ----------- | ----- | -------------- |
| internal id | label | name UPPERCASE |

## Sites (og_sites.csv)

-   comma seperated
-   license:
    -   combined: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de>)
-   origin:
    -   [Ogi-Ogham Project (Q70873595)](https://www.wikidata.org/wiki/Q70873595)
-   method:
    -   semi-automatic digitalisation by F. Thiery / S.C. Schmidt

| id          | label | wkt                     | wikidata_id           | townland_label | barony_label | county_label | province_label | country_label |
| ----------- | ----- | ----------------------- | --------------------- | -------------- | ------------ | ------------ | -------------- | ------------- |
| internal id | label | representative WKT geom | Wikidata Q Identifier | townland       | barony       | county       | province       | country       |

## Inscriptions (og_inscriptions.csv)

-   comma seperated
-   license:
    -   combined: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de>)
-   origin:
    -   [Ogi-Ogham Project (Q70873595)](https://www.wikidata.org/wiki/Q70873595)
-   method:
    -   semi-automatic digitalisation by F. Thiery

| id          | insc_no            | reading_no     |
| ----------- | ------------------ | -------------- |
| internal id | inscription number | reading number |

## Locations (og_locations.csv)

-   comma seperated
-   license:
    -   Ogham in 3D: [CC BY-NC-SA 3.0 Ireland](http://creativecommons.org/licenses/by-nc-sa/3.0/ie/deed.en_US)
    -   other: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de>)
-   origin:
    -   [Ogi-Ogham Project (Q70873595)](https://www.wikidata.org/wiki/Q70873595)
    -   [Celtic Inscribed Stones Project (Q106628017)](https://www.wikidata.org/wiki/Q106628017)
    -   [Ogham in 3D Project (Q106674066)](https://www.wikidata.org/wiki/Q106674066)
-   method:
    -   semi-automatic digitalisation / postgres join by F. Thiery / S.C. Schmidt

| id          | type          | wkt          | geom_orig      | geom_lastrecorded       | sitetype      | site      | grid                |
| ----------- | ------------- | ------------ | -------------- | ----------------------- | ------------- | --------- | ------------------- |
| internal id | location type | WKT geometry | o3d geom: orig | o3d geom: last recorded | o3d site type | cisp site | cisp grid reference |

## Readings (og_reasings.csv)

-   comma seperated
-   license:
    -   Ogham in 3D: [CC BY-NC-SA 3.0 Ireland](http://creativecommons.org/licenses/by-nc-sa/3.0/ie/deed.en_US)
    -   other: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de>)
-   origin:
    -   [Ogi-Ogham Project (Q70873595)](https://www.wikidata.org/wiki/Q70873595)
    -   [Celtic Inscribed Stones Project (Q106628017)](https://www.wikidata.org/wiki/Q106628017)
    -   [Ogham in 3D Project (Q106674066)](https://www.wikidata.org/wiki/Q106674066)
-   method:
    -   semi-automatic digitalisation / postgres join by F. Thiery / S.C. Schmidt

| id          | label | language                                                                                                         | script                                                                                                         | scientist | scientist_year |
| ----------- | ----- | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | --------- | -------------- |
| internal id | label | language type[\*](https://www.ucl.ac.uk/archaeology/cisp/database/manual/node3.html#SECTION00341000000000000000) | script type[\*](https://www.ucl.ac.uk/archaeology/cisp/database/manual/node3.html#SECTION00341000000000000000) | reader    | reading year   |

## Stones (og_stones.csv)

-   comma seperated
-   license:
    -   Ogham in 3D: [CC BY-NC-SA 3.0 Ireland](http://creativecommons.org/licenses/by-nc-sa/3.0/ie/deed.en_US)
    -   other: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de>)
-   origin:
    -   [Ogi-Ogham Project (Q70873595)](https://www.wikidata.org/wiki/Q70873595)
    -   [Celtic Inscribed Stones Project (Q106628017)](https://www.wikidata.org/wiki/Q106628017)
    -   [Ogham in 3D Project (Q106674066)](https://www.wikidata.org/wiki/Q106674066)
-   method:
    -   semi-automatic digitalisation / postgres join by F. Thiery / S.C. Schmidt

| id          | label | desc        | wikidata_id           | original_id      | width | height | depth       | thickness        | h_status        | w_status        | t_status        | discovery_year | discovery_who    | currentsetting                                                                                                     | currentlocation  | form                                                                                                    | completeness                                                                                                    | preservation                                                                                                    | preservation_note |
| ----------- | ----- | ----------- | --------------------- | ---------------- | ----- | ------ | ----------- | ---------------- | --------------- | --------------- | --------------- | -------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------ | ---------------- | ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ----------------- |
| internal id | label | description | Wikidata Q Identifier | ID of the origin | width | height | depth (o3d) | thickness (cisp) | h_status (cisp) | w_status (cisp) | t_status (cisp) | discovery year | discovery person | current setting[\*](https://www.ucl.ac.uk/archaeology/cisp/database/manual/node3.html#SECTION00331000000000000000) | current location | form[\*](https://www.ucl.ac.uk/archaeology/cisp/database/manual/node3.html#SECTION00335000000000000000) | completeness[\*](https://www.ucl.ac.uk/archaeology/cisp/database/manual/node3.html#SECTION00331000000000000000) | preservation[\*](https://www.ucl.ac.uk/archaeology/cisp/database/manual/node3.html#SECTION00331000000000000000) | preservation_note |

## Stones / References (og_stones_references.csv)

-   comma seperated
-   license:
    -   combined: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de>)
-   origin:
    -   [Ogi-Ogham Project (Q70873595)](https://www.wikidata.org/wiki/Q70873595)
    -   [Celtic Inscribed Stones Project (Q106628017)](https://www.wikidata.org/wiki/Q106628017)
-   method:
    -   semi-automatic digitalisation / postgres join by F. Thiery

| id          | original_id      | stone_type | cisp_id | o3d    | macalister_1945 | macalister_1907 | mcmanus_1991  | macalister_1902 | macalister_1897 | cuppage_1986  | macalister_1949 | brash_1879    | osullivan_1996 | power_1992    | macalister_1909 | petrie_1872   | brikil_1993   | raftery_1960  | okasha_forsyth_2001 | ferguson_1887 | power_1997    | g_id         | ciic_stone | cisp_stone | o3d_stone |
| ----------- | ---------------- | ---------- | ------- | ------ | --------------- | --------------- | ------------- | --------------- | --------------- | ------------- | --------------- | ------------- | -------------- | ------------- | --------------- | ------------- | ------------- | ------------- | ------------------- | ------------- | ------------- | ------------ | ---------- | ---------- | --------- |
| internal id | ID of the origin | type       | CISP ID | O3D ID | reference no.   | reference no.   | reference no. | reference no.   | reference no.   | reference no. | reference no.   | reference no. | reference no.  | reference no. | reference no.   | reference no. | reference no. | reference no. | reference no.       | reference no. | reference no. | Reference ID | CIIC Stone | CISP Stone | O3D Stone |
