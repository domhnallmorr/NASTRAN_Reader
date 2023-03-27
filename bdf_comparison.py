import pandas as pd

def summary_comparison(baseline_bdf, updated_bdf):
	assert [baseline_bdf, updated_bdf] != [None, None], "Both Baseline and Updated BDFs are of type None, provide at least 1 BDF"

	if baseline_bdf is not None:
		cards = list(baseline_bdf.summary.keys())
	elif updated_bdf is not None: 
		cards = list(updated_bdf.summary.keys())

	df = pd.DataFrame(index=cards)

	df["Card"] = cards
	df["Baseline"] = 0
	df["Updated"] = 0
	
	if baseline_bdf is not None:
		for card in baseline_bdf.summary.keys():
			df.at[card, "Baseline"] = baseline_bdf.summary[card]

	if updated_bdf is not None:
		for card in updated_bdf.summary.keys():
			df.at[card, "Updated"] = updated_bdf.summary[card]

	df["Delta"] = df["Updated"] - df["Baseline"]

	return df

def cards_comparison(baseline_bdf, updated_bdf):
	assert [baseline_bdf, updated_bdf] != [None, None], "Both Baseline and Updated BDFs are of type None, provide at least 1 BDF"
	cards = {}

	if baseline_bdf is not None:
		for card in baseline_bdf.cards:
			cards[card] = {"Altered": [], "Deleted": [], "New": [], "Unchanged": []}
	elif updated_bdf is not None:
		for card in updated_bdf.cards:
			cards[card] = {"Altered": [], "Deleted": [], "New": [], "Unchanged": []}
	
	# If only 1 model provided, just return the card IDs, no comparison required
	if None in [baseline_bdf, updated_bdf]:
		if baseline_bdf is not None:
			bdf = baseline_bdf
		else:
			bdf = updated_bdf

		for card in cards.keys():
			cards[card]["Unchanged"] = [i for i in bdf.cards[card].keys()]

	else: # do the full comparison between the models
		for card in cards.keys():
			baseline_cards = baseline_bdf.cards[card]
			updated_cards = updated_bdf.cards[card]
			
			# FIND NEW/SAME/ALTERED CARDS
			for card_id in updated_cards.keys(): 
				if card_id not in baseline_cards.keys(): # Card in updated model but not baseline model
					cards[card]["New"].append(card_id)
				else: # else card present in both models
					if baseline_cards[card_id] == updated_cards[card_id]: # card is the same in both models
						cards[card]["Unchanged"].append(card_id)
					else: # else card is different between both models
						cards[card]["Altered"].append(card_id)

			# FIND DELTETED CARDS
			for card_id in baseline_cards.keys():
				if card_id not in updated_cards.keys(): # card in baseline model but not updated model
					cards[card]["Deleted"].append(card_id)

	# Create Dataframe of Quantities of cards
	
	df_quantities = pd.DataFrame(index=list(cards.keys()))
	df_quantities["Altered"] = 0
	df_quantities["Deleted"] = 0
	df_quantities["New"] = 0
	df_quantities["Unchanged"] = 0
	
	for card in cards.keys():
		df_quantities.at[card, "Altered"] = len(cards[card]["Altered"])
		df_quantities.at[card, "Deleted"] = len(cards[card]["Deleted"])
		df_quantities.at[card, "New"] = len(cards[card]["New"])
		df_quantities.at[card, "Unchanged"] = len(cards[card]["Unchanged"])

	return cards, df_quantities

def get_card_comparison_data(baseline_bdf, updated_bdf, card_type, card_id):
	assert [baseline_bdf, updated_bdf] != [None, None], "Both Baseline and Updated BDFs are of type None, provide at least 1 BDF"

	if baseline_bdf is not None:
		fields = baseline_bdf.cards[card_type][card_id]
	else:
		fields = updated_bdf.cards[card_type][card_id]

	fields = [f for f in fields if "continuation marker" not in f.lower() and "start line" not in f.lower()]

	df = pd.DataFrame(index=fields)

	df["Baseline"] = None
	df["Updated"] = None
	df["Delta"] = None

	for field in fields:
		if baseline_bdf is not None:
			df.at[field, "Baseline"] = baseline_bdf.cards[card_type][card_id][field]
		if updated_bdf is not None:
			df.at[field, "Updated"] = updated_bdf.cards[card_type][card_id][field]
 
	df["Delta"] = df["Updated"] - df["Baseline"]
	 
	return df

if __name__ == "__main__":
	from nastran_reader import bdf_reader
	bdf = bdf_reader.BdfFile(r"C:\Users\ev662f\Desktop\NEW_UPP_ATT_POS_FLT_new.bdf")

	cards, df_quantities = cards_comparison(bdf, bdf)


