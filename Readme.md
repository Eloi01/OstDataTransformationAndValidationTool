# OstData Transformation and Validationtool

## Table of Contents

### 1. General Purpose

### 2. General Structure

### 3. Structure of the Configuration-File

### 4. Transformation

### 5. Parameters for Validation

### 6. Input

### 7. Output

## 1. General Purpose
This Tool provides an (hopefully) easy-to-use way to transform and validate provided Meta-Datasets into the OstData Schema.
Hence, it is designed to provide the development team of OstData a script-based way to evaluate their changes of the OstData-Metadata-Schema by executing the transformation and validation process on test data sets.

## 2. General Structure
Generally is the tool divided in two separate parts. On one hand there is the script which coordinates  the task of transforming and validating the provided datasets.
On the other hand a configuration file is provided which determines how the provided datasets will be transformed and validated.
This configuration file represents each single element of the OstData schema. For each element it uses a thesaurus to coordinate the transformation process
and list of categories of possible validations to coordinate the validation process for each OstData Schema Element.

## 3. Structure of the Configuration-File
The Configuration-File represents the OstData-schema as a whole as an XML-File. Each Element of the Schema is represented as an according module of the XML-File.
Each Element consists of two parts. \
The first part is provides information to the specific element and is realised with SKOS. Furthermore, it represents a thesaurus which coordinates the transformation process.\
The second part provides a list of categories which determine how each element will be individually validated. 

## 4. Transformation
The Transformation process will be coordinated via the included thesaurus for each individual element.
A mapping of the individual data elements shall be integrated here.\
**skos:prefLabel**: specifies the name of the element according to the OstData-Schema.\
**skos:altLabel**: represents each element of source-dataset which shall be transformed in the preferred label.


## 5. Parameters for Validation

| Kategory | Content | Options |
|----------|---------|---------|
|required| defines if an element of the schema is required.| True / False|
|requiredElement| defines if another element must be given, when this element is given.| null / name of the Element|
|WordCount| specifies the maximum Wordcount which a specific element is allowed to contain.| null / int -> number of Words|
|internalNormvokabular| Normvocabular which is provided by OstData to be used for the Element.| null / [String] -> List of Normvocab|
|externalNormcokabular| Normvocabular which is used from external Souces (e.g. ISO-6393). The Normvocab needs to be stored inside the NormVocav.py file.| null / Name of the used Normvocab|
|LOD|Linked-Open-Data for which the element shall be evaluated (e.g. GND)| null / GND / Orcid / VIAF / ROR (multiple options can be combined via a list containing the options to be used|
|Coordinates| Specified coordinate for which the element shall be evaluated | null / longitude / latitude / box / polygon|
|Date| Specified date for which the element shall be evaluated | null / date / duration |
|emptyString| defines if an element is allowed to be an empty String ( it is used in some Elements which are required) | True / False|

## 6. Input
Shall be specified in the main class.\
**input_path**: defines the path of the input-file which shall be transformed and validated.
At this point it is only able to read JSON-Files.\
**configuration_path**: defines the path of the configuration-file which shall be used.
At this point no formal validation of the configuration-file is included, so be aware.

## 7. Output
Shall be specified in the main class.\
**output_path**: defines the path in which the result datasets will be written. The result-file will be in a JSON-format.\
**log_output_path**: defines the path in which the log for the transformation and validation process will be written. The log-file will be in TXT-format.\
**log_failed_items_path**: defines the path in which a separate log will be written. It only includes datasets which failed to be transformed or validated. This log will also be in a TXT-format.
