import xml.etree.ElementTree as ET
import json
from datetime import datetime, timedelta
import pytz
import re  # Import the regular expression module

# Define the date range (7 days ago from today) in UTC timezone
current_date = datetime.now(pytz.utc)
date_limit = current_date - timedelta(days=7)

# Parse the local sitemap.xml file
tree = ET.parse("sitemap.xml")
root = tree.getroot()

# List to store recent product URLs
recent_product_urls = []

# Namespace for sitemaps (if present in the XML)
ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

# Regular expression to match URLs without paths (subdirectories)
url_pattern = re.compile(r'^https://www.mytek.tn/[^/]+\.html$')

# Iterate through URL elements in the sitemap
for url in root.findall(".//ns:url", namespaces=ns):
    loc = url.find('ns:loc', namespaces=ns).text
    lastmod_element = url.find('ns:lastmod', namespaces=ns)

    if lastmod_element is not None:
        lastmod = lastmod_element.text

        # Convert the lastmod date to a datetime object in UTC timezone
        lastmod_date = datetime.fromisoformat(lastmod).replace(tzinfo=pytz.utc)

        # Check if the lastmod date is within the last 7 days
        if lastmod_date >= date_limit:
            # Check if the URL matches the pattern for URLs without paths
            if url_pattern.match(loc):
                recent_product_urls.append(loc)

# Save the recent product URLs to a JSON file
with open("recent_products_urls.json", "w", encoding="utf-8") as json_file:
    json.dump(recent_product_urls, json_file, ensure_ascii=False, indent=4)

print(f"Total of {len(recent_product_urls)} recent products found.")

