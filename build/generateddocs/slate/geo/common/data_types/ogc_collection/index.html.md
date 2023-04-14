---
title: OGC Collection (Schema)


toc_footers:
  - Version 0.1
  - <a href='#'>OGC Collection</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: OGC Collection (Schema)
---

# Overview

An OGC Collection resource is a JSON object that provides information about and access to a set of geospatial resources, through links to API endpoints and/or files online. It is most commonly used to describe geospatial datasets, but can be used for collections of anything geospatial.

[Maturity](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Mature

# Description

An OGC Collection is often included in an API as one of several collections of data.
But it can also be used as a standalone file to provide static metadata and links to geospatial data.

## Pre-defined properties

| Property                  | Type       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|---------------------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                        | string     | *REQUIRED*. Unique identifier of the collection. The identifier is used, for example, as a path element in URIs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| title                     | string     | The human readable title of the collection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| description               | string     | A free-text description of the resources in the collection. The content may include Markdown and HTML markup.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| itemType                  | string     | Indicator about the type of the data items in the collection. The items can be accessed by following the items link, if provided. The default value is "feature".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| links                     | [ Link ]   | *REQUIRED*. Links to other resources. See Link relation types for typical link relations included in a collection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| extent                    | [ Extent ] | *CONDITIONAL*. The extent of the data in the collection. The property has to be provided, if the data has a spatial or temporal extent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| crs                       | [ URI ]    | The list of coordinate reference systems supported by the API for this collection. Each coordinate reference systems is identified by a URI. See Coordinate reference system (CRS) identifiers. At least WGS84 longitude/latitude (with optional ellipsoidal height) has to be supported.<br/><br/>If the collection is embedded in an OGC Collections resource that includes a global list of CRS identifiers, the special value "#/crs" can be used to declare all coordinate reference systems in the global list as supported coordinate reference systems of this collection.<br/><br/>Default: `[ "http://www.opengis.net/def/crs/OGC/1.3/CRS84" ]` |
| storageCrs                | URI        | The cooordinate reference system, from the list of supported CRS identifiers, in which the data is stored internally and that may be used to retrieve features from the collection without the need to apply a CRS transformation.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| storageCrsCoordinateEpoch | number     | The point in time at which coordinates in the feature collection are referenced to the dynamic coordinate reference system in storageCrs. The epoch is expressed as a decimal year in the Gregorian calendar; for example, March 25th, 2017, in the Gregorian calendar is epoch 2017.23.                                                                                                                                                                                                                                                                                                                                                                  |


## Link relation types

The following link relation types are commonly used in links from an OGC
Collection:

| Link relation type | Description                                                                                                                                                                                                                                                                                                                                                       |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| items              | *REQUIRED*. Refers to the items in the collection, for example, a Features resource, if the itemType is "feature".<br/><br/>This link relation type will not be registered with IANA. In the future, it may be superseded by the search link relation type.                                                                                                       |
| search             | *RECOMMENDED*. Refers to the items in the collection, for example, a Features resource, if the itemType is "feature", with support for filtering features using spatial, temporal and thematic selection criteria.<br/><br/>This link relation type will in the future supersede the items link relation type, so it is recommended to already include this link. |
| self               | *REQUIRED*. Link to the resource in the current representation.                                                                                                                                                                                                                                                                                                   |
| alternate          | *REQUIRED*. Link to the resource in every other media type supported by the server.                                                                                                                                                                                                                                                                               |
| license            | *RECOMMENDED*. Refers to the license associated with the data.                                                                                                                                                                                                                                                                                                    |
| type               | *RECOMMENDED*. Refers to the canonical URI of the OGC Collection resource type and identifies the resource as an OGC Collection.<br/><br/>No OGC API resource types have currently been registered by the OGC Naming Authority, a proposal is in preparation. A tentative URI could be http://www.opengis.net/def/type/ogc/0/ogc-collection.                      |
| describedby        | Refers to a resource providing information about the data, for example, a separate metadata resource.                                                                                                                                                                                                                                                             |
| enclosure          | Refers to a distribution of the data that is available for download as a single file.                                                                                                                                                                                                                                                                             |
| item               | Refers to an item in this collection, for example, a link:../features/json-features.adoc [Feature resource], if the itemType is "feature".                                                                                                                                                                                                                        |

The following link relation types are commonly used in links to an OGC
Collection:

| Link relation type | Description                                                                                        |
|--------------------|----------------------------------------------------------------------------------------------------|
| `collection`       | Used in items of the collection, for example, a [Feature resource](../features/json-feature.adoc). |

### Coordinate reference system (CRS) identifiers

It is common practice to use CRS identifiers using the following
template:

`http://www.opengis.net/def/crs/{authority}/{version}/{code}`

In this template, the token `{authority}` is a placeholder for a value
that designates the authority responsible for the definition of this
CRS. Typical values include "EPSG" and "OGC".

The token `{version}` is a placeholder for the specific version of the
CRS definition or `0` for un-versioned CRS definitions.

The token `{code}` is a placeholder for the authority’s code for the
CRS. Some frequently used coordinate reference systems are:

  - <http://www.opengis.net/def/crs/OGC/1.3/CRS84> - WGS84 longitude,
    latitude

  - <http://www.opengis.net/def/crs/EPSG/0/4326> - WGS84 latitude,
    longitude

  - <http://www.opengis.net/def/crs/OGC/0/CRS84h> - WGS84 longitude,
    latitude, ellipsoidal height

  - <http://www.opengis.net/def/crs/EPSG/0/4979> - WGS84 latitude,
    longitude, ellipsoidal height

  - <http://www.opengis.net/def/crs/EPSG/0/3857> - Web Mercator (used in
    Web Mapping)

  - <http://www.opengis.net/def/crs/EPSG/0/4258> - ETRS89 latitude,
    longitude
# Examples

## Collection example

```json
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
```

# Schema

[schema.yaml](https://raw.githubusercontent.com/avillar/bblocks/master/registereditems/geo/common/data_types/ogc_collection/schema.yaml)
# Sources

* [OGC API - Features, Part 1, 7.14.2 Feature collection Response](http://www.opengis.net/doc/IS/ogcapi-features-1/1.0#_response_5)
