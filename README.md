# U.S. State of the State transcripts

This repository consists of speeches data used in the working paper [Political Metaphors in U.S. Governor Speeches (L. Picard & D. Stammbach)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4298372)

`dataset_parsed.csv` contains 1,296 State of the State speeches from U.S. governors, between 1995 and 2022. Raw text files and metadata are also provided.

`speech_parser.py` contains the code to append all text files, merges it with `metadata.csv`, then stores the output in `dataset_parsed.csv`. As a preprocessing step, I only delete new lines `\n` and tabulations `\t`.

List of variables from `dataset_parsed.csv`:

Variable | Definition
-------|-----------
`file_id` | Name of the text file from `speeches_raw/`
`state_id` | U.S. State unique identifier (ISO 2-digit)
`state_name` | U.S. State official name
`year` | Year of elocution
`speaker` | Speaker name
`party` | Speaker political party (democratic/republican/other)
`type` | Type of speech (sots/sotu/budg/inaug/other)
`quality` | Transcript quality (as prepared/ocr/quotes/bulletpoints/youtube cc)
`text` | Parsed speech
`source` | URL link


