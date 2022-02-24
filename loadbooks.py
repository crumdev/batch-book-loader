import json, os
from pyairtable import Table

# Set these variables to match your table
api_key = os.environ['AIRTABLE_API_KEY']
airtable_database_id = "apps0zHa7K0DssXRI"
table_name = "Books"
book_load_file = 'books2.json'

table = Table(api_key, airtable_database_id, table_name)

with open(book_load_file,'r') as file:
    book_list = json.load(file)

print("Books to load =>", str(len(book_list[:])))

# Upload all the books in a batch
table.batch_create(book_list)