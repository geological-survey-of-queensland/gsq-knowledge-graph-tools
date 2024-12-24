# CKAN Metadata to Graph JSON Converter

This Jupyter Notebook provides a sequence of operations that convert CKAN metadata into a graph JSON structure. The converter is tailored to produce two JSON files for different visualization purposes:

- `conformed_graph.json`: A raw graph compatible with generic LPG (Labelled Property Graph) viewers. A basic 2D viewer setup is available in the LPG directory.
- `viz_graph.json`: A graph file specifically formatted for use with the Graph3d visualizer tool.

## Prerequisites

- Ensure you have Python 3 installed.
- Required Python packages: `pandas`, `requests`, `uuid`, `json`, and `os`.

## Setup

Before running the notebook, place a CSV file named `report_list.csv` in the project directory. The CSV file should contain CKAN package names and can be generated manually or through the [CKAN API Request Builder](https://geological-survey-of-queensland.github.io).

## Usage Guide

The notebook involves four main steps:

1. **Get the Metadata**
   - Reads the `report_list.csv` file to obtain package names.
   - Fetches metadata for each package from the CKAN API and merges them into a single structure.

2. **Convert to Graph Schema**
   - Defines a function to convert each metadata entry into graph format.
   - Iterates over the combined metadata and applies the conversion function.

3. **Conform to Graph Object**
   - Collates the graph objects into a singular graph.
   - Duplicates are removed, and consistent node and edge structures are ensured.
   - Outputs the `conformed_graph.json` file.

4. **Create Graph3d Visualization Format**
   - Transforms the conformed graph into a format suitable for 3D visualization.
   - Assigns group-specific visual attributes to nodes and edges.
   - Saves the resulting graph as `viz_graph.json`.

The resulting `conformed_graph.json` file can be loaded into a basic 2D viewer (available at the top of the LPG directory), or you can use the `vis_graph.json` with the 3D Graph Viewer, which can be found at [GSQ Labs](https://geological-survey-of-queensland.github.io).

## Running the Notebook

Execute each cell in order, observing output messages between steps for success or error reporting. The progress output will update you on the number of packages processed and added to the structure.

Upon completion, check the `output` directory in your working environment for the resultant JSON files.

## Issues

If you encounter any issues or have feature suggestions, please file a report in the repository's [issue tracker](https://github.com/geological-survey-of-queensland/gsq-knowledge-graph-tools/issues).

## License

Please refer to the license file provided in the repository for the terms and conditions governing the use and distribution of the code.

