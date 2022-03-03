GOAL:
To analyze how different version of jQuery evolved we first need to determine exactly why type of clones JsInspect can detect. 
After running JsInspect on this surrogate set you should discuss the ability or inability of JsInspect to correctly detect the clones. 


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

### Preprocessing

The jquery files in the github repo contain many unneeded files, and since version 2 jquery.js only contains imports of the many javascript files containing the actual source code.

As such the uncompressed jquery files are downloaded from jquery.com, the command in `prep.py` is updated to `command = f"curl --remote-name https://code.jquery.com/jquery-{release['tag']}.js"`. This downloads all versions known in the csv file. The `releases.csv` file is updated to exclude tags `1.0.0, 1.1.0, 1.2.0, 1.3.0, 1.4.0, 1.5.0, 1.6.0 and 1.7.0` as these versions only exist as 1.x (without minor version .0).

Above mentioned files are then renamed to their correct name following semantic versioning standards, with leading `.0`.0

## lines of code

`find . -iname 'jquery.js' -exec cloc --csv --quiet {} \; > /out/lines.csv`