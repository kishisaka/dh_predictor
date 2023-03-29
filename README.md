# dh_predictor

Run the main.py to see some output.  

The scores are calculated by adding the various attributes together for each person and dividing the sum
by 100. 

The data is in the data.json file and is loaded on start of the print_scores() function. 

An instance of Predictor is passed into the Scorer.score() so a unit test can be made here to ensure that the scorer functions properly separately from the Predictor itself with a mocked Predictor. The Predictor can be tested by itself since it is self-contained. 




