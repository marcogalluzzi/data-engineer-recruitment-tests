# Frogtek Data Engineer Recruitment Test

This repository contains a simple test for data engineering candidates at [Frogtek](http://frogtek.org). Thank you for taking the time to do it. It consists of two parts:

* [A technical test](#technical-test)
* [A few technical questions](#technical-questions)

## Technical Test

The technical test consists of three tasks:

* Transform a [poorly formatted TSV file](https://github.com/frogtek/recruiment-tests/blob/master/data/data.tsv) into a properly formatted, machine-readable TSV file. If you clicked on the link above you may notice that GitHub complains about errors in the file. The file does not explicitly adhere to the TSV format.
* Write an app that can generate core business events in batches; then write those events to a JSON delimited file at specified intervals.
* Stream the JSON delimited files that you generated in step one into program which will output a running count of each event type to the terminal every five seconds.



1. Write a simple script to transform [data.tsv](https://github.com/frogtek/recruiment-tests/blob/master/data/data.tsv) into a properly formatted tab-separated values (TSV) file that can be read by any standard CSV/TSV parser. The resulting file should have the
following properties:

    * Each row contains the same number of fields
    * Fields are separated by tabs `\t`
    * Fields that contain reserved characters (e.g. `\t`, `\r`, `\n`) are quoted *(hint hint)*
    * The file is UTF-8 encoded (`data.tsv` is UTF-16LE encoded)
   * The solution does *not* need to be generic enough to apply to similar issues in other files; your algorithm can be designed specifically for this data set. 
    * Extra points are awarded for resource-efficient and scalable solutions.

    For bonus points, ambitious candidates can parallelize their algorithm. A parallelizable implementation will have the following properties:
    * Given an arbitrary byte `position` and `length`, the algorithm cleans a portion of the full data set and produces a unique TSV output file
    * Concatenating the outputs of multiple processes should result in a well-formed TSV file containing no duplicates
    * *It's important to note that the arbitrary `position` may not necessarily be the start of a new line.*


2. Write an app that can generate core business events:

	* Each order will produce two events namely (`OrderPlaced`, `OrderAccepted`) or (`OrderPlaced`, `OrderCancelled`).
	* For every five orders, four orders will consist of `OrderPlaced` and `OrderAccepted` events and one order of `OrderPlaced` and `OrderCancelled` events.
	* The batch of events within a given interval should be stored in a JSON delimited file named `orders-<timestamp>.json` ex. orders-2017-05-14-18-47-29-879763.json
	* The app must take 4 arguments
		* number-of-orders - Number of orders to generate which will each produce two events.
		* batch-size - Batch size of events per file.
		* interval - Interval in seconds between each file being created.
		* output-directory - Output directory for all created files.
	* How to run the app

		```bash
		generate-events --number-of-orders=1000000 --batch-size=5000 --interval=1 --output-directory=<local-dir>
		```
	* Example shows a snippet of ten events from the content of a generated file. Each event is on its own line separated by a linebreak.

		```json
		{ "Type": "OrderPlaced", "Data": { "OrderId": "3cb0f939-9398-4d29-a28f-2a1a3a6ce3b2", "TimestampUtc": "2017-05-14T19:12:32Z" } }
		{ "Type": "OrderAccepted", "Data": { "OrderId": "3cb0f939-9398-4d29-a28f-2a1a3a6ce3b2", "TimestampUtc": "2017-05-14T19:12:32Z"} }
		{ "Type": "OrderPlaced", "Data": { "OrderId": "a7d86ca5-7541-4c86-a7ad-1bec2b070b3c", "TimestampUtc": "2017-05-14T19:12:33Z" } }
		{ "Type": "OrderAccepted", "Data": {"OrderId": "a7d86ca5-7541-4c86-a7ad-1bec2b070b3c", "TimestampUtc": "2017-05-14T19:12:33Z"} }
		{ "Type": "OrderPlaced", "Data": { "OrderId": "757001d9-a454-40d3-a14b-9f0f9440be9f", "TimestampUtc": "2017-05-14T19:12:34Z" } }
		{ "Type": "OrderAccepted", "Data": { "OrderId": "757001d9-a454-40d3-a14b-9f0f9440be9f", "TimestampUtc": "2017-05-14T19:12:34Z"} }
		{ "Type": "OrderPlaced", "Data": { "OrderId": "4f3fd16c-4685-45e6-a6f9-823f5f73a7d0", "TimestampUtc": "2017-05-14T19:12:35Z" } }
		{ "Type": "OrderAccepted", "Data": {"OrderId": "4f3fd16c-4685-45e6-a6f9-823f5f73a7d0", "TimestampUtc": "2017-05-14T19:12:35Z"} }
		{ "Type": "OrderPlaced", "Data": { "OrderId": "812a8469-68d0-4c9b-8429-d46d51d63db3", "TimestampUtc": "2017-05-14T19:12:36Z" } }
		{ "Type": "OrderAccepted", "Data": { "OrderId": "812a8469-68d0-4c9b-8429-d46d51d63db3", "TimestampUtc": "2017-05-14T19:12:36Z"} }
		{ "Type": "OrderPlaced", "Data": { "OrderId": "8825cd95-f172-4132-9793-864b4dd725df", "TimestampUtc": "2017-05-14T19:12:37Z" } }
		{ "Type": "OrderCancelled", "Data": {"OrderId": "8825cd95-f172-4132-9793-864b4dd725df", "TimestampUtc": "2017-05-14T19:12:37Z"} }
		```
	* Every `OrderPlaced` event must have a `OrderAccepted` or `OrderCancelled` event with the same OrderId.

2. Write a streaming app:

	* Monitor a given directory for new files.
	* Process new files containing order events.
	* Output a running count for each event type to the terminal.
	* Keep a 5 second delay between each terminal output.

		ex. Terminal displaying a running count of each event type from the previous JSON snippet
		```bash
		"OrderCancelled": 1
		"OrderAccepted": 4
		"OrderPlaced": 5
		```

## Technical questions

Please answer the following questions in a markdown file called `Answers to technical questions.md`.

1. How long did you spend on the coding test? What would you add to your solutions if you had more time? If you didn't spend much time on the coding test then use this as an opportunity to explain what you would add.
2. Why did you choose the language you used for the coding test?
3. What was the most useful feature that was added to the latest version of your chosen language?
4. How would you track down a performance issue in production? Have you ever had to do this?
5. Please describe yourself using JSON.

## Platform Choice

You can create the solution in any language or framework of your choice.

## Task requirements

Feel free to spend as much or as little time on the exercise as you like, as long as the following requirements have been met:

- Please complete at least one of the technical tasks described above.
- You should provide clear instructions on your test setup and how to execute your tests. The clarity and precision of these instructions - and the ease with which the interviewers can execute them - will be a key part of the assessment. Please create a README file detailing said instructions. Please also use this file for listing any additional comments or observations you might want to share about your submission.

To submit the test, please complete the following steps:

1. Download this repository
2. Solve the first part with scripts in the language of your choice
3. Write a markdown file with the instructions on how to execute the scripts
3. Write a single markdown file with the answers to the technical questions
4. Upload the scripts and markdown files to a repository in Github
5. Email the link back to the contact that give you this test

#### Thanks for your time, we look forward to hearing from you!
- The [Frogtek Tech Team](https://developing,frogtek.org)

Inspiration:
https://github.com/datascienceinc/data-engineering-test
https://github.com/justeat/JustEat.RecruitmentTest/blob/master/Test.Data.Engineer.md
