# Wiki
Design a Wikipedia-like online encyclopedia.

Each entry is stored in Markdown language so that the entries are more human-friendly to write and edit. When a user views th encyclopedia entry, that Markdown will be converted into HTML before displaying it to the user.

## Website functionalities

### Index Page
* Each entry is stored in Markdown language so that the entries are more human-friendly to write and edit. When a user views th encyclopedia entry, that Markdown will be converted into HTML before displaying it to the user.

### Entry Page
* This page renders the contents of an encyclopedia entry by requesting `/wiki/TITLE`
* If an entry is requested that does not exist, the user is presented with an error page indicating that their requested page was not found.

### Search
* Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry
* If the query matches the name of an encyclopedia entry, the user is redirected to that entry’s page.
* If the query does not match the name of an encyclopedia entry, the user is taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring.
* Clicking on any of the entry names on the search results page takes the user to that entry’s page.

### New Page
* Clicking “Create New Page” in the sidebar takes the user to a page where they can create a new encyclopedia entry.
* Users are able to enter a title for the page, and the Markdown content for the page.
* Users are able to click a button to save their new page.
* When the page is saved, if an encyclopedia entry already exists with the provided title, the user is presented with an error message.
* Otherwise, the encyclopedia entry is saved to disk, and the user is taken to the new entry’s page.

### Edit Page
* On each entry page, the user is able to click a link to be taken to page where the user can edit that entry’s Markdown content.
* The `textarea` is pre-populated with the existing Markdown content of the page.
* The user is able to click a button to save the changes made to the entry.
* Once the entry is saved, the user is redirected back to that entry’s page.

### Random Page
* Clicking “Random Page” in the sidebar takes user to a random encyclopedia entry.

### Markdown to HTML Conversion
* The `python-markdown2` package is used to perform this conversion.
