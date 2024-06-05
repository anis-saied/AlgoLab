import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
import csv

# Define the URL of the sitemap
sitemap_url = "https://www.mytek.tn/media/sitemap/sitemap.xml"

# Define the cutoff date (one week ago) as offset-aware datetime in UTC
cutoff_date = datetime.now(timezone.utc) - timedelta(days=60)

# Send a GET request to the sitemap URL
response = requests.get(sitemap_url)

# Check if the request was successful
if response.status_code == 200:
    # Create a list to store the new product URLs
    new_product_urls = []

    # Parse the XML content
    root = ET.fromstring(response.content)

    # Iterate through the URLs in the sitemap
    for url in root.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}url"):
        loc = url.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc").text
        lastmod_element = url.find("{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod")

        # Check if the 'lastmod' element exists
        if lastmod_element is not None:
            lastmod = lastmod_element.text

            # Update the format string to include time and timezone information
            lastmod_date = datetime.strptime(lastmod, "%Y-%m-%dT%H:%M:%S%z")

            # Check if the product is new (last modified date is within the past week)
            if lastmod_date >= cutoff_date:
                new_product_urls.append(loc)

    # Define the output CSV file name
    output_file = "all-new-products.csv"

    # Write the new product URLs to the CSV file
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows([[url] for url in new_product_urls])

    print(f"New product URLs saved to {output_file}")
else:
    print("Failed to fetch the sitemap. Status code:", response.status_code)

