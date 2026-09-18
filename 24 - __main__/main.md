# if **name** == **main**

This script can be imported OR run standalone.
Functions and classes in this module can be reused ithout the main block of code executing

## Simple analogy: "If this is not being run directly, dont run **name** = **main** "

<br>

Run script1. See how main runs
Run script2. Despite importing everything, script1's main doesn't run.
This is because dunder-name only is dunder-main if the file is run directly and not imported
