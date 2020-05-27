# threatcrowd
Simple python script that queries the threatcrowd API to find subdomains for a provided top level domain.
The results are printed to stdout in a readable format, as well as being written to a text file in the working directory.
A log file is also written of all information from the lookup, not just the results.

Usage: python3 threatcrowd.py example.com
