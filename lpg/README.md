# Labelled Property Graph Tooling README

## Overview

This repository contains a series of folders dedicated to processing and visualising data from different sources into labelled property graphs (LPGs). A labelled property graph is a foundational construct in graph theory and databases. It is a flexible way to represent complex networks where both nodes (entities) and edges (relationships) can have multiple attributes associated with them.

Included in this repository is a standardised viewer tool, `2D_lpg_viewer.html`, for accessing the outputs from the various converters. This viewer tool is designed to work standalone and can be run without a webserver. Users can simply download and open it in a web browser to start interacting with the property graphs.

## 2D Labelled Property Graph Viewer

The `2D_lpg_viewer.html` tool is a web-based application that allows users to visualise labelled property graphs in a 2D format. It is designed to be intuitive and user-friendly, providing an interactive way to explore nodes and their relationships.

### Features

- Support for loading graphs from `.json` and `.xlsx` files.
- Interactive visualisation of nodes and edges in a network.
- Customisable colour palettes for nodes based on labels.
- Tooltips that appear when hovering over nodes and edges, showing detailed properties.
- Sidebar for inspecting details upon clicking a node.
- Hierarchical data layout and various graph physics settings available.
- Zoom and navigation controls for ease of graph exploration.

### Technical Information

The tool is built upon HTML, CSS, and JavaScript, utilising the `vis-network` library for rendering interactive graphs. It also uses the `xlsx` library to process Excel files.

The layout is styled to be responsive, adapting to various screen sizes for optimal usability. Tooltips and a fixed top bar with file input and colour palette choices provide a seamless user experience. The sidebar for inspection of nodes and relationships toggles visibility based on user interaction.

### Usage Guide

1. **Opening the Viewer**: Simply download the `2D_lpg_viewer.html` file and open it in your web browser.
   
2. **Loading Data**:
    - Click the file input on the top bar to select and upload a `.json` or `.xlsx` file containing the graph data.
    - The tool automatically detects the file type and processes the contents to render the graph.

3. **Interacting with the Graph**:
    - Use the provided zoom and navigation controls to adjust the view.
    - Hover over nodes or edges to see tooltips with additional details.
    
4. **Inspection Sidebar**:
    - Enable the "Inspect" checkbox to show the sidebar.
    - Click on any node in the graph to view its details and relationships in the sidebar.
    
5. **Changing Colour Palette**:
    - Use the colour palette dropdown in the top bar to change the colour scheme of the nodes in the graph.
    - The graph will automatically re-render with the chosen palette.

6. **Closing the Viewer**:
    - Simply close the browser tab or window where the `2D_lpg_viewer.html` is open.

This tool provides a powerful means for users to visualise complex graphs and derive insights from their structures and properties visually. It is an invaluable component of the LPG tooling in this repository, complementing the conversion and processing tools found in the various folders.

## Additional Information

This README should be located in the top-level directory of the LPG tooling section of the repository and should be updated as new features or tools are added to the repository.

For any technical issues or contributions to the `2D_lpg_viewer.html` or other tools in this repository, please refer to the repository's contribution guidelines or raise an issue in the repository's issue tracker.