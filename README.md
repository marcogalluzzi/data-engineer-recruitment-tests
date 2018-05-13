# Instructions and notes

These are the instructions for executing the programs created to solve the tests for a _Data Engineering Recruitment_ process. For each test also some notes has been provided.

In order to execute them you need to have installed __Python version 3.6__.

All the programs can be found in the folder `exercises` and can be run by executing one of the following commands:
1. `python3 <program.py> <arguments>`
2. `<program.py> <arguments>` if you make the file `program.py` executable with command `chmod +x <program.py>`.

NOTE: program arguments can be entered `--arg1=value1` or `--arg1 value1`

## Repair a poorly formatted TSV file

Running:
```
python3 exercises/repair-tsv.py --input-filename "data/data.tsv" --output-filename "data/data-repaired.tsv" --input-encoding "utf_16_le"
```
The explanation of the arguments can be retrieved running the program with `-h`:
```
usage: repair-tsv.py [-h] --input-filename INPUT_FILENAME --output-filename
                      OUTPUT_FILENAME [--input-encoding INPUT_ENCODING]
                      [--num-columns NUM_COLUMNS] [--buffer-size BUFFER_SIZE]

Repair a TSV file

optional arguments:
  -h, --help            show this help message and exit
  --input-filename INPUT_FILENAME
                        input TSV file to repair
  --output-filename OUTPUT_FILENAME
                        output file where to write the repaired TSV file
  --input-encoding INPUT_ENCODING
                        encoding of input file, e.g. "utf_16_le", or None to
                        use platform default encoding (default: None)
  --num-columns NUM_COLUMNS
                        number of columns or None to autodetect it by reading
                        first line (default: None)
  --buffer-size BUFFER_SIZE
                        size of read buffer (default: 512)
```

### Notes
The code provided is aimed to solve the type of problems found in provided file `data.tsv`, this is missing quotes for fields including the `\n` character.

The solution reads the input file in text mode using a buffer which size can be configured with parameter `--buffer-size`. Also writing to the repaired file is done using this buffer.


## Generate core business events
Running:
```
python3 exercises/generate-events.py --number-of-orders=100000 --batch-size=5000 --interval=1 --output-directory="output"
```
The explanation of the arguments can be retrieved running the program with `-h`:
```
usage: generate-events.py [-h] --output-directory OUTPUT_DIRECTORY
                          [--number-of-orders NUMBER_OF_ORDERS]
                          [--batch-size BATCH_SIZE] [--interval INTERVAL]
                          
Core Business Events Generator

optional arguments:
  -h, --help            show this help message and exit
  --output-directory OUTPUT_DIRECTORY
                        output directory for all created files
  --number-of-orders NUMBER_OF_ORDERS
                        number of orders to generate (default: 100)
  --batch-size BATCH_SIZE
                        batch size of events per file (default: 10)
  --interval INTERVAL   interval in seconds between each file being created
                        (default: 1)
```
### Notes

It handles the case when `number-of-orders` is not multiple of `batch-size` which means that the last file has less orders than `batch-size`.

It also avoids that the monitoring program can read an uncompleted file by using a temporary file name.

The creation of the JSON string for the business event could also be created using the function `json.dumps()` which I think is safer than creating a formatted string because it checks the correctness of the JSON. However, I chose using a formatted string to preserve the ordering of the JSON fields specified in the requirements, which it couldn't be assured otherwise.

## Monitor a directory and output a running count of events

Running:
```
python3 exercises/monitor-events.py  --directory output/
```
The explanation of the arguments can be retrieved running the program with `-h`:
```
usage: monitor-events.py [-h] --directory DIRECTORY [--interval INTERVAL]

Event Files Monitoring

optional arguments:
  -h, --help            show this help message and exit
  --directory DIRECTORY
                        directory to monitor for event files
  --interval INTERVAL   interval in seconds between each directory check for
                        new files (default: 5)
```

Every 5 seconds, or the interval selected by the user, the program analyze only new files, and not all the files in the folder.

The count is computed by reading the input files line by line and not entirely, which is better in terms of memory consumption.

Counting the event types on a file could also been done by reading the character 16 of each line and checking if it is 'A', 'C' or 'P', which can be faster than using `find()`. However, I preferred a more general solution.

The running count displayed has been forced to be displayed in the order shown in the requirements.
