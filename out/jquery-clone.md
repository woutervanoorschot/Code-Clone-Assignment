## run jsinpsect on jquery codebase

Only the `jquery.js` files are the 'true' source code of jquery, complete but not minified. As such these files need to be compared across versions.

`jsinspect -I -L -t 20 /usr/jquery-data/*/jquery.js`

## Matches

with command `jsinspect -t 30 /usr/jquery-data/*/jquery.js` (default):

`1181 matches found across 39 files`

### comparison

On two versions with default params:

`jsinspect /usr/jquery-data/1.10.0/jquery.js /usr/jquery-data/1.10.1/jquery.js`

output

`34 matches found across 2 files`

with `-r json` the output is stored in output.json for later analysis


## lines of code

`find . -iname 'jquery.js' -exec cloc --csv --quiet {} \; > /out/lines.csv`