---
title: OGC Collections (Schema)


toc_footers:
  - Version 0.1
  - <a href='#'>OGC Collections</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: OGC Collections (Schema)
---

# Overview

The distribution of a geospatial dataset in an API is organized into one or more collections of data. How the data is split into collections in a distribution depends on the intended use of the data. Two common approaches for organizing the data are: by semantic type and by spatial clustering. The OGC Collections JSON resource provides information about and access to the data in each collection of the distribution.

[Maturity](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Mature

# Examples

## Collections example with a single collection

```json
{
  "links": [
    { "href": "http://data.example.org/collections.json",
      "rel": "self", "type": "application/json", "title": "this document" },
    { "href": "http://data.example.org/collections.html",
      "rel": "alternate", "type": "text/html", "title": "this document as HTML" },
    { "href": "http://schemas.example.org/1.0/buildings.json",
      "rel": "describedby", "type": "application/schema+json", "title": "JSON schema for Acme Corporation building data" },
    { "href": "http://download.example.org/buildings.gpkg",
      "rel": "enclosure", "type": "application/geopackage+sqlite3", "title": "Bulk download (GeoPackage)", "length": 472546 }
  ],
  "collections": [
      {
         "id": "buildings",
         "title": "Buildings",
         "description": "Buildings in the city of Bonn.",
         "itemType": "feature",
         "extent": {
            "spatial": {
               "bbox": [ [ 7.01, 50.63, 7.22, 50.78 ] ]
            },
            "temporal": {
               "interval": [ [ "2010-02-15T12:34:56Z", null ] ]
            }
         },
         "links": [
            { "href": "https://data.example.org/collections/buildings.json",
               "rel": "self", "type": "application/json", "title": "This collection" },
            { "href": "https://data.example.org/collections/buildings.html",
               "rel": "alternate", "type": "text/html", "title": "This collection as HTML" },
            { "href": "https://data.example.org/collections/buildings/items",
               "rel": "items", "type": "application/geo+json",
               "title": "Buildings" },
            { "href": "https://data.example.org/collections/buildings/items",
               "rel": "http://www.opengis.net/def/rel/ogc/1.0/items", "type": "application/geo+json",
               "title": "Buildings" },
            { "href": "https://creativecommons.org/publicdomain/zero/1.0/",
               "rel": "license", "type": "text/html",
               "title": "CC0-1.0" },
            { "href": "https://creativecommons.org/publicdomain/zero/1.0/rdf",
               "rel": "license", "type": "application/rdf+xml",
               "title": "CC0-1.0" }
         ]
      }
   ]
}
```


## Collections example with a global list of CRS identifiers

In this example, the "bonn_buildings" collection is offered in all the CRSs specified in the global list plus three other CRSs.

The "tor_buildings" collection is offered in the CRSs specified in the global list.

The "dc_buildings" collection is only offered in the default CRS (i.e., WGS 84 longitude, latitude).
```json
{
  "links": [
    { "href": "http://data.example.org/collections.json",
      "rel": "self", "type": "application/json", "title": "this document" },
    { "href": "http://data.example.org/collections.html",
      "rel": "alternate", "type": "text/html", "title": "this document as HTML" },
    { "href": "http://schemas.example.org/1.0/buildings.xsd",
      "rel": "describedby", "type": "application/xml", "title": "GML application schema for Acme Corporation building data" },
    { "href": "http://download.example.org/buildings.gpkg",
      "rel": "enclosure", "type": "application/geopackage+sqlite3", "title": "Bulk download (GeoPackage)", "length": 472546 }
  ],
  "crs": [
     "http://www.opengis.net/def/crs/OGC/1.3/CRS84",
     "http://www.opengis.net/def/crs/EPSG/0/4326",
     "http://www.opengis.net/def/crs/EPSG/0/3857",
     "http://www.opengis.net/def/crs/EPSG/0/3395"
  ],
  "collections": [
     {
       "id": "bonn_buildings",
       "title": "Bonn Buildings",
       "description": "Buildings in the city of Bonn.",
       "extent": {
         "spatial": {
           "bbox": [ [ 7.01, 50.63, 7.22, 50.78 ] ]
         },
         "temporal": {
           "interval": [ [ "2010-02-15T12:34:56Z", null ] ]
         }
       },
       "links": [
         { "href": "http://data.example.org/collections/bonn_buildings/items",
           "rel": "items", "type": "application/geo+json",
           "title": "Bonn Buildings" },
         { "href": "https://creativecommons.org/publicdomain/zero/1.0/",
           "rel": "license", "type": "text/html",
           "title": "CC0-1.0" },
         { "href": "https://creativecommons.org/publicdomain/zero/1.0/rdf",
           "rel": "license", "type": "application/rdf+xml",
           "title": "CC0-1.0" }
       ],
       "crs": [
          "#/crs",
          "http://www.opengis.net/def/crs/EPSG/0/4258",
          "http://www.opengis.net/def/crs/EPSG/0/25831",
          "http://www.opengis.net/def/crs/EPSG/0/25832"
       ]
     },
     {
       "id": "tor_buildings",
       "title": "Toronto Buildings",
       "description": "Buildings in the city of Toronto.",
       "extent": {
         "spatial": {
           "bbox": [ [ -79.62, 43.58, -79.12, 43.87 ] ]
         },
         "temporal": {
           "interval": [ [ "2010-02-15T12:34:56Z", null ] ]
         }
       },
       "links": [
         { "href": "http://data.example.org/collections/tor_buildings/items",
           "rel": "items", "type": "application/geo+json",
           "title": "Toronto Buildings" },
         { "href": "https://creativecommons.org/publicdomain/zero/1.0/",
           "rel": "license", "type": "text/html",
           "title": "CC0-1.0" },
         { "href": "https://creativecommons.org/publicdomain/zero/1.0/rdf",
           "rel": "license", "type": "application/rdf+xml",
           "title": "CC0-1.0" }
       ],
       "crs": [
          "#/crs"
       ]
     },
     {
       "id": "dc_buildings",
       "title": "Washington DC Buildings",
       "description": "Buildings in the city of Washington DC.",
       "extent": {
         "spatial": {
           "bbox": [ [ -77.12, 38.80, -76.89, 39.01 ] ]
         },
         "temporal": {
           "interval": [ [ "2010-02-15T12:34:56Z", null ] ]
         }
       },
       "links": [
         { "href": "http://data.example.org/collections/dc_buildings/items",
           "rel": "items", "type": "application/geo+json",
           "title": "DC Buildings" },
         { "href": "https://creativecommons.org/publicdomain/zero/1.0/",
           "rel": "license", "type": "text/html",
           "title": "CC0-1.0" },
         { "href": "https://creativecommons.org/publicdomain/zero/1.0/rdf",
           "rel": "license", "type": "application/rdf+xml",
           "title": "CC0-1.0" }
         ],
         "crs": [
           "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
       ]
     }
  ]
}
```

# Schema

[schema.yaml](https://raw.githubusercontent.com/avillar/bblocks/master/registereditems/geo/common/data_types/ogc_collections/schema.yaml)
# Sources

* [OGC API - Features, Part 1, 7.13.2: Feature Collections Response](http://www.opengis.net/doc/IS/ogcapi-features-1/1.0#_response_4)
