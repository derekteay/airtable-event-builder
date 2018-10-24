from airtable import Airtable
from collections import defaultdict
import sys
from datetime import datetime

# AirTable API setup - replace the values with your own
airtable = Airtable('base-key', 'table-name', api_key='your-api-key')

# Get only records that are in the correct Status
records = airtable.search('Status', 'Ready to Post: All Data Provided')

# Create defaultdict structure
records_list = defaultdict(list)

# Process each record from AirTable
for record in records:

    # For ease of code writing
    record = record['fields']

    # Sanitize bad data in AirTable - Formatting the information
    event_title = record['Event Title'].replace("\n", "")
    event_date = record['Event Date']

    # Remove anything past the city name
    display_city = record['Display City'].split(',')[0]

    # URL might not be provided, catch this error
    try:
        event_url = record['Event URL']
    except KeyError:
        event_url = ""

    # Sanitize bad data in AirTable - Replace newlines, *'s, and double spaces
    event_description = record['Event Description'].replace("\n", "")
    event_description = event_description.replace("*", "")
    event_description = event_description.replace("  ", " ")

    try:
        address = record['Address'].strip()
    except KeyError:
        address = ""

    # Host might not be provided, catch this error
    try:
        host = record['Host'].strip()
    except KeyError:
        host = ""

    # Speakers might not be provided, catch this error
    try:
        speakers = record['Speakers']
    except KeyError:
        speakers = ""

    # Generate city slug
    display_city_slug = display_city.lower().replace(" ", "-")

    # Create event list dictionary
    event_list = {"event title": event_title,
                  "event date": event_date,
                  "display city": display_city,
                  "event url": event_url,
                  "event description": event_description,
                  "address": address,
                  "host": host,
                  "speakers": speakers}

    # If the event date is in the past, don't add it to the list
    present = datetime.strptime(datetime.now().strftime('%d/%b/%Y'), '%d/%b/%Y')
    
    if datetime.strptime(event_date, '%d/%b/%Y') < present:
        # DEBUG
        #print("***** past event *****", event_list)
        continue
    else:
        # Add the event to the correct city slug
        records_list[display_city_slug].append(event_list)

# Generate the php file in the most hacky way possible
#
# The counters are used to determine if we've hit the end of the list, as there
# will be no comma at the end of that line

item_counter = 1

# Write to _city-content.php file
stdout = sys.stdout
sys.stdout = open('_city-content.php','w')
print("<?php")
print("$content = array(")

# Process the record list
for item in sorted(records_list):
    print("\t\"" + item + "\"", "=> array(")

    event_counter = 1
    for event in records_list[item]:
        print("\t\tarray(")
        print("\t\t\t\"title\" => " + "\"" + event['event title'] + "\",")
        print("\t\t\t\"date\" => " + "\"" + event['event date'] + "\",")
        print("\t\t\t\"display_city\" => " + "\"" + event['display city'] + "\",")
        print("\t\t\t\"url\" => " + "\"" + event['event url'] + "\",")
        print("\t\t\t\"desc\" => " + "\"" + event['event description'] + "\",")
        print("\t\t\t\"addr\" => " + "\"" + event['address'] + "\",")

        if event['host'] != "":
            print("\t\t\t\"host\" => " + "\"" + event['host'] + "\",")
        else:
            pass

        speaker_counter = 1
        if event['speakers'] != "":
            print("\t\t\t\"speakers\" => array(")
            for speaker in event['speakers'].split(','):
                print("\t\t\t\tarray(")
                print("\t\t\t\t\t\"name\" => " + "\"" + speaker.strip() + "\"")
                if speaker_counter == len(event['speakers'].split(',')):
                    print("\t\t\t\t)")
                else:
                    print("\t\t\t\t),")
                speaker_counter += 1
            print("\t\t\t)")
        else:
            pass

        if event_counter == len(records_list[item]):
            print("\t\t)")
        else:
            print("\t\t),")
        event_counter += 1
    if item_counter == len(records_list):
        print("\t)")
    else:
        print("\t),")
    item_counter += 1
print(");")

sys.stdout = stdout

# Read _city-content.php file to make sure data is good
city_content_file = open('_city-content.php', 'r')
content = city_content_file.read()
city_content_file.close()
print(content)
