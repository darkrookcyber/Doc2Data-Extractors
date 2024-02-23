"""

- Step 1: run extraction tool

python3 extract_text.py --input xxxx.pdf --output xxxxx.txt

- Step 2: run preprocessing tool

python3 preprocess.py textfile.txt

- Step 3: run clean data tool

python3 cleanData.py preprocessed.txt

- Step 4: prepare clean data for fine tuning

python3 prepForTraining.py --files /path/to/company1.txt /path/to/company2.txt --labels Company1 Company2 --output combined_data.csv

	
