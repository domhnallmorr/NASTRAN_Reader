import pandas as pd

def summary_comparison(baseline_bdf, updated_bdf):
	assert [baseline_bdf, updated_bdf] != [None, None], "Both Baseline and Updated BDFs are of type None, provide at least 1 BDF"

	if baseline_bdf is not None:
		cards = list(baseline_bdf.summary.keys())
	elif updated_bdf is not None: 
		cards = list(updated_bdf.summary.keys())

	df = pd.DataFrame(index=cards)

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

if __name__ == "__main__":
	from nastran_reader import bdf_reader
	bdf = bdf_reader.BdfFile(r"C:\Users\ev662f\Desktop\NEW_UPP_ATT_POS_FLT_new.bdf")

	summary_comparison(bdf, None)