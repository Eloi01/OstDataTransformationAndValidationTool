import json
import xml.etree.ElementTree as Xml

from Configuration import Configuration


def read_input(path):
    """Reads an Input-File and converts it into a List of datasets.

    At this point it only is able to read JSON-Files.

    :parameter path: Path of the input File.
    :returns: containing datasets as a list. False if the file could not be read."""

    path_string = str(path)
    if path_string.endswith(".json"):
        try:
            with open(path, "r", encoding="utf-8") as input_file:
                json_input_list = json.load(input_file)
                return json_input_list
        except ValueError as err:
            print("Could not read JSON")
            return False


def read_configuration_file_to_configuration_object_list(path):
    """Reads an input file for the configuration and converts it into a list of configuration objects.
    Asserts that the provided configuration file is in an XML-Format.

    :parameter path: Path of the configuration file.
    :returns: List of configuration-Objects."""

    list_of_configuration = []
    try:
        root_node = Xml.parse(path).getroot()
        for concept in root_node[0].findall("{http://www.w3.org/2004/02/skos/core}Concept"):
            configuration = Configuration()
            configuration.name = concept.find("{http://www.w3.org/2004/02/skos/core}prefLabel").text
            for validation in concept.findall("Validation"):
                configuration.required = validation.find("required").text
                configuration.required_element= validation.find("requiredElement").text
                configuration.wordcount = validation.find("WordCount").text
                configuration.internal_norm_vocabulary = validation.find("internalNormvokabular").text
                configuration.external_norm_vocabulary = validation.find("externalNormvokabular").text
                configuration.lod = validation.find("LOD").text
                configuration.coordinate = validation.find("Coordinates").text
                configuration.date = validation.find("Date").text
                configuration.empty_string = validation.find("emptyString").text
            if concept.find("{http://www.w3.org/2004/02/skos/core}note") is not None:
                configuration.note = concept.find("{http://www.w3.org/2004/02/skos/core}note").text
            if concept.find("Schema-ID") is not None:
                configuration.id = concept.find("Schema-ID").text
            if concept.find("{http://www.w3.org/2004/02/skos/core}altLabel") is not None:
                for concept_items in concept.findall("{http://www.w3.org/2004/02/skos/core}altLabel"):
                    alt_label = concept_items.text
                    configuration.list_of_alt_labels.append(alt_label)
            list_of_configuration.append(configuration)
        return list_of_configuration
    except ValueError as err:
        print("Could not read Configuration!")

