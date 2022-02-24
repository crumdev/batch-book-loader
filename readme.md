# Kindle Unlimited History Archive

- Navigate to the [Kindle Unlimited](https://www.amazon.com/gp/kindle/ku/ku_central?ref_=nav_AccountFlyout_ku) management page.
- Scroll to the bottom of the page to reveal all of the books in you history
- Open the developer tools console (CTRL+SHIFT+I on firefox)
- Paste in the Javascript code into the console and run it to return a list of book title, image url, and product links.

    ```js
    var items = document.getElementsByClassName('a-column a-span2 a-spacing-base');

    Array.from(items).forEach(v => {
    
    console.log('\n')
    
    // Get Each book Title
    console.log(v.firstChild.nextSibling.lastElementChild.attributes[0].value);
    
    // Get book image
    console.log(v.firstChild.nextSibling.lastElementChild.attributes[1].value);
    
    // Get Each book URL
    console.log("https://amazon.com" + v.firstChild.nextSibling.attributes[1].value);
    
    console.log('\n---')
    });
    ```

- Right click the results and export out to a file.
- Check the api for your table to match whatever fields you have created and format your list into an array of json objects to match. For my table the results looked like `example.json`
- Create the following environment variables and run `loadbooks.py`
  - AIRTABLE_API_KEY
  - AIRTABLE_TABLE_ID
  - AIRTABLE_TABLE_NAME
  - BOOK_JSON_FILE
