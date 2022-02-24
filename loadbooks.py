import json, os
from pyairtable import Table

# Set these environment variables to match your table
api_key = os.environ['AIRTABLE_API_KEY']
airtable_database_id = os.environ['AIRTABLE_TABLE_ID']
table_name = os.environ['AIRTABLE_TABLE_NAME']
book_load_file = os.environ['BOOK_JSON_FILE']

table = Table(api_key, airtable_database_id, table_name)

with open(book_load_file,'r') as file:
    book_list = json.load(file)

print("Books to load =>", str(len(book_list[:])))

# Upload all the books in a batch
table.batch_create(book_list)