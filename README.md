# StringPPI

[中文版](README_zh.md)

This repository is used to process PPI data from the STRING website.

### Solving the 2000 Protein Input Limitation on STRING
Since the STRING website (https://string-db.org/) allows a maximum of 2000 proteins as input at a time, `string_input_limiter.py` processes PPI-related data from STRING (https://string-db.org/cgi/download), enabling the input of any number of proteins.

Note: This script only processes the data and does not provide functionality for plotting PPI networks. Please use other tools like Cytoscape for plotting.

### Using the STRING API to Retrieve PPI
`string_API.py` calls the STRING API and is suitable for batch processing.
