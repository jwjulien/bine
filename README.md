Markdown Checklist Editor
========================================================================================================================
The idea is to create a tool that is similar to Vine, my Markdown editor, where the output is a properly formatted Markdown file but the editor adds some additional features that are calculated and displayed automatically from the text, such as counts and progress bars.

The motivation for this tool came from the packing lists that I have migrated from my online lists tool over to Markdown files in a Mercurial repo.  That move was motivated by wanting to have a single file for large lists to better facilitate searching for duplicate items but the large files are a tad cumbersome in a plain ole text editor.




Ideas/Requirements
------------------------------------------------------------------------------------------------------------------------
- Help find duplicates.
    - Fuzzy search would be nice so as to find things with words in different orders.
- Allow description to be placed at the top of the document.
- Support trees with parent automatically checking when list is complete.
    - Support drag and drop for moving items if possible.
    - Would be really nice if the tree can be collapsed.
- Spell check would be a major perc.
- Definitely support checkboxes for each item.
    - Would be kinda nice if the checkboxes support tri-state.
- Show progress bars showing percentage complete.
- Automatically sort list items in alphabetical order to better compare two lists.
