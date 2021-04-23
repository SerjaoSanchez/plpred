setup:
	conda env create --file environment.yml  || conda env update --file environment.yml
run_exploratory_data_analysis:
	cd notebooks/ && \
ipython Exploratory_Data_Analysis.ipynb && \
jupyter nbconvert --to html '../notebooks/Exploratory_Data_Analysis.ipynb'
