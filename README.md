# U.S. State of the State transcripts

This repository contains a dataset of 1'198 speeches from U.S. politicians between 1995 and 2022. Raw text files and metadata are also provided.

`speech_parser.py` contains the code to append all text files, merges it with `metadata.csv`, then stores the output in `dataset_parsed.csv`. As a preprocessing step, I only delete new lines `\n` and tabulations `\t`.

List of variables from `dataset_parsed.csv`:

Variable | Definition
-------|-----------
`file_id` | Name of the text file from `speeches_raw/`
`state_id` | U.S. State unique identifier (ISO 2-digit)
`state_name` | U.S. State official name
`year` | Year of elocution
`speaker` | Name of the speaker
`party` | Political party of the speaker (democratic/republican/other)
`type` | Type of speech (sots/sotu/budg/inaug/other)
`quality` | Quality of the transcript (as prepared/ocr/quotes/bulletpoints/youtube cc)
`text` | Parsed speech
`source` | URL link of the speech


