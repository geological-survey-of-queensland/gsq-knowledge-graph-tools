import pandas as pd
import uuid
import json

# Function to validate the existence of source and target nodes for edges
def validate_nodes(nodes, edges):
    node_ids = set(nodes['node'])
    missing_sources = edges[~edges['source'].isin(node_ids)]
    missing_targets = edges[~edges['target'].isin(node_ids)]
    
    if not missing_sources.empty or not missing_targets.empty:
        error_message = "The following source or target nodes do not exist in the nodes tab:\n"
        if not missing_sources.empty:
            error_message += "Missing source nodes: {}\n".format(missing_sources['source'].tolist())
        if not missing_targets.empty:
            error_message += "Missing target nodes: {}\n".format(missing_targets['target'].tolist())
        raise ValueError(error_message)

# Load data from Excel
nodes_df = pd.read_excel('lpg_template.xlsx', sheet_name='nodes')
edges_df = pd.read_excel('lpg_template.xlsx', sheet_name='edges')

# Assign UUIDs for edges with blank ID
edges_df['edge'] = edges_df['edge'].apply(lambda x: str(uuid.uuid4()) if pd.isnull(x) else x)

# Validate node IDs
validate_nodes(nodes_df, edges_df)

# Convert nodes dataframe to JSON
nodes_list = nodes_df.to_dict('records')
nodes_json = [{"id": node['node'], "label": node['label'], "properties": {k: v for k, v in node.items() if pd.notnull(v) and k not in ['node', 'label', 'add properties -->']}} for node in nodes_list]

# Convert edges dataframe to JSON
edges_list = edges_df.to_dict('records')
edges_json = [{"id": edge['edge'], "source": edge['source'], "label": edge['label'], "target": edge['target'], "properties": {k: v for k, v in edge.items() if pd.notnull(v) and k not in ['edge', 'source', 'label', 'target', 'add properties -->']}} for edge in edges_list]

# Combine nodes and edges into a graph
lpg_graph = {
    "nodes": nodes_json,
    "edges": edges_json
}

# Save JSON graph to file
with open('lpg_graph.json', 'w') as json_file:
    json.dump(lpg_graph, json_file, indent=2)

# Output summary to console
print(f"Graph creation completed with {len(nodes_json)} nodes and {len(edges_json)} edges.")