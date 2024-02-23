"""

- Step 1: run extraction tool

python3 extract_text.py --input xxxx.pdf --output xxxxx.txt

- Step 2: run preprocessing tool

python3 preprocess.py textfile.txt

- Step 3: run clean data tool

python3 cleanData.py preprocessed.txt

- Step 4: prepare clean data for training

python3 prepForTraining.py --files /path/to/company1.txt /path/to/company2.txt --labels Company1 Company2 --output combined_data.csv

- Step 5: uploading formatted data to model - willy nilly

python3 uploadData.py --model_path /path/to/mistral/model --data_path /path/to/formatted/formatted_data.csv

- Step 6: fail miserably.....
back to the drawing board, lets look at some use cases here and adjust fire....

	0. Content Moderation
Content moderation is a process for detecting: nwanted user input, such as requests for unsafe or private information, or unwanted output from the LLM, such as hate speech. (Could be done outside LLM)
	
	1. Company Summary Generation
Generate concise summaries of companies from longer texts, such as business plans or pitch decks. This can help quickly grasp the essence of a potential investment opportunity.

	2. Market Analysis and Trends Identification
Analyze market reports and news articles to identify and summarize key trends and developments in sectors of interest. This can be invaluable for understanding the broader context in which a startup operates.

	3. Sentiment Analysis
Perform sentiment analysis on news articles, analyst reports, and social media mentions related to specific startups or the broader industry. Understanding sentiment can provide insights into public perception and potential market movements.

	4. Risk Assessment
Automatically assess and categorize risks from business plans or due diligence reports. This could involve identifying specific risk factors mentioned in texts and classifying them into categories like financial, regulatory, market, or operational risks.

	5. Investment Recommendation
Based on the analysis of a company's data, market conditions, and possibly comparing with historical data of successful ventures, the model could suggest whether a company might be a good investment opportunity.

	6. Question Answering
Develop a question-answering system that can extract specific information from extensive documents. This could be useful for quickly finding answers to key questions about a company or market without reading through entire documents.

	7. Deal Sourcing
Identify potential investment opportunities by analyzing news feeds, press releases, and other sources to spot emerging companies and startups that match the VC firm's investment criteria.

	8. Trend Forecasting
Use historical data and current market analysis to predict future trends in various sectors. This can help in making informed decisions about where to focus investment efforts.

	9. Competitive Analysis
Automatically compare a startup's offerings, business model, market position, and other key metrics against its competitors. This can provide a quick overview of a company's competitive landscape.

	10. Due Diligence Automation
Streamline the due diligence process by automatically extracting and summarizing key information from due diligence documents, saving time and resources in the investment evaluation process.

******NOTE: When fine-tuning the model for these tasks, it's essential to have a dataset that is representative of the task at hand. For example, for summary generation, you would need pairs of long texts and their summaries. For sentiment analysis, you would need texts labeled with their sentiment.******




