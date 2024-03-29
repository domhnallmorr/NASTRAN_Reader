 
def process_cbar(bdf, data, field_format):
	if field_format == "long":
		fields = ["EID", "PID", "GA", "GB", "CONTINUATION MARKER",
					"X1", "X2", "X3", "OFFT", "CONTINUATION MARKER 2",
					"PA", "PB", "W1A", "W2A", "CONTINUATION MARKER 3",
					"W3A", "W1B", "W2B", "W3B", "CONTINUATION MARKER 3",
					]
		data_types = [int, int, int, int, str,
						float, float, float, str, str,
						int, int, float, float, str,
						float, float, float, float, str,
						]
		pass
	else:
		fields = ["EID", "PID", "GA", "GB", "X1", "X2", "X3", "OFFT", "CONTINUATION MARKER",
					"START LINE 2", "PA", "PB", "W1A", "W2A", "W3A", "W1B", "W2B", "W3B"]
		data_types = [int, int, int, int, float, float, float, str, str,
						str, int, int, float, float, float, float, float, float,]
	
	id = int(data[1])
	bdf.cbars[id] = {f: None for f in fields}
	populate_fields(bdf.cbars, data, fields, data_types, id)
	
def process_cbeam(bdf, data, field_format):
	if field_format == "long":
		fields = ["SID", "PID", "G1", "G2", "CONTINUATION MARKER",
					"X1", "X2", "X3", "OFF", "CONTINUATION MARKER 2",
					"PA", "PB", "W1A", "W2A", "CONTINUATION MARKER 3",
					"W3A", "W1B", "W2B", "W3B", "CONTINUATION MARKER 4"]
		data_types = [int, int, int, int, str,
						float, float, float, str, str,
						int, int, float, float, str,
						float, float, float, float, str]
	else:
		fields = ["SID", "PID", "G1", "G2", "X1", "X2", "X3", "OFF", "CONTINUATION MARKER",
					"START LINE 2", "PA", "PB", "W1A", "W2A", "W3A", "W1B", "W2B", "W3B"]
		data_types = [int, int, int, int, float, float, float, str, str,
						str, int, int, float, float, float, float, float, float,]
	
	id = int(data[1])
	bdf.cbeams[id] = {f: None for f in fields}
	populate_fields(bdf.cbeams, data, fields, data_types, id)

def process_cord2r(bdf, data, field_format):
	if field_format == "long":
		fields = ["CID", "RID", "A1", "A2", "CONTINUATION MARKER",
	    			"A3", "B1", "B2", "B3", "CONTINUATION MARKER",
					"C1", "C2", "C3"]
		data_types = [int, int, float, float, str,
	       				float, float, float, float, str,
						float, float, float]
	else:
		fields = ["CID", "RID", "A1", "A2", "A3", "B1", "B2", "B3", "CONTINUATION MARKER",
					"C1", "C2", "C3"]
		data_types = [int, int, float, float, str,
	       				float, float, float, float, str,
						float, float, float]
		
	id = int(data[1])
	bdf.cord2rs[id] = {f: None for f in fields}
	populate_fields(bdf.cord2rs, data, fields, data_types, id)

def process_cquad4(bdf, data, field_format):
	if field_format == "long":
		fields = ["EID", "PID", "G1", "G2", "CONTINUATION MARKER",
					"G3", "G4", "THETA/MCID", "ZOFFS", "CONTINUATION MARKER 2",
					"BLANK", "TFLAG", "T1", "T2", "CONTINUATION MARKER 3",
					"T3", "T4", "CONTINUATION MARKER",]
		data_types = [int, int, int, int, str,
				int, int, float, float, str,
				str, int, float, float, str,
				float, float]
	else:
		fields = ["EID", "PID", "G1", "G2", "G3", "G4", "THETA/MCID", "ZOFFS", "CONTINUATION MARKER",
					"START LINE 2", "BLANK", "TFLAG", "T1", "T2", "T3", "T4"]
		data_types = [int, int, int, int, int, int, float, float, str,
						str, str, int, float, float, float, float]

	id = int(data[1])
	bdf.cquad4s[id] = {f: None for f in fields}
	populate_fields(bdf.cquad4s, data, fields, data_types, id)

def process_ctria3(bdf, data, field_format):
	if field_format == "long":
		fields = ["EID", "PID", "G1", "G2", "CONTINUATION MARKER",
					"G3", "THETA/MCID", "ZOFFS", "BLANK", "CONTINUATION MARKER 2",
					"TFLAG", "T1", "T2", "T3"]
		data_types = [int, int, int, int, str,
						int, float, float, str, str,
						int, float, float, float]
	else:
		fields = ["EID", "PID", "G1", "G2", "G3", "THETA/MCID", "ZOFFS", "CONTINUATION MARKER",
					"START LINE 2", "BLANK", "TFLAG", "T1", "T2", "T3"]
		data_types = [int, int, int, int, int, float, float, str,
						str, str, int, float, float, float]
	
	id = int(data[1])
	bdf.ctria3s[id] = {f: None for f in fields}
	populate_fields(bdf.ctria3s, data, fields, data_types, id)
	
def process_crod(bdf, data, field_format):
	if field_format == "long":
		fields = ["EID", "PID", "G1", "G2"]
		data_types = [int, int, int, int]
	else:
		fields = ["EID", "PID", "G1", "G2"]
		data_types = [int, int, int, int]

	id = int(data[1])
	bdf.crods[id] = {f: None for f in fields}
	populate_fields(bdf.crods, data, fields, data_types, id)

def process_cshear(bdf, data, field_format):
	if field_format == "long":
		raise Exception("CSHEAR card is only supported for small field format at this time")
	else:
		fields = ["EID", "PID", "G1", "G2", "G3", "G4"]
		data_types = [int, int, int, int, int, int]

	id = int(data[1])
	bdf.cshears[id] = {f: None for f in fields}
	populate_fields(bdf.cshears, data, fields, data_types, id)

def process_force(bdf, data, field_format):
	if field_format == "long":
		fields = ["SID", "G", "CID", "F", "CONTINUATION MARKER", "N1", "N2", "N3"]
		data_types = [int, int, int, float, str, str, float, float, float]
	else:
		fields = ["SID", "G", "CID", "F", "N1", "N2", "N3"]
		data_types = [int, int, int, float, float, float, float]

	if len(list(bdf.forces.keys())) == 0:
		card_id = 0
	else:
		card_id = list(bdf.forces.keys())[-1] + 1

	bdf.forces[card_id] = {f: None for f in fields}
	populate_fields(bdf.forces, data, fields, data_types, card_id)

def process_grav(bdf, data, field_format):
	if field_format == "long":
		raise Exception("GRAV card is only supported for small field format at this time")
	else:
		fields = ["SID", "CID",  "A", "N1", "N2", "N3", "MB"]
		data_types = [int, int, float, float, float, float, float]

	id = int(data[1])
	bdf.gravs[id] = {f: None for f in fields}
	populate_fields(bdf.gravs, data, fields, data_types, id)

def process_grid(bdf, data, field_format):
	if field_format == "long":
		fields = ["SID", "CP",  "X1", "X2", "CONTINUATION MARKER", "X3", "CD"]
		data_types = [int, int, float, float, str, float, int]
	else:
		fields = ["SID", "CP",  "X1", "X2", "X3", "CD"]
		data_types = [int, int, float, float, float, int]

	# CP is coord system in which coordinates are defined
	# CD is coord system in which displacements are reported

	id = int(data[1])
	bdf.grids[id] = {f: None for f in fields}
	populate_fields(bdf.grids, data, fields, data_types, id)

def process_mat1(bdf, data, field_format):
	if field_format == "long":
		fields = ["MID", "E", "G", "NU", "CONTINUATION MARKER",
					"RHO", "A", "TREF", "GE", "CONTINUATION MARKER 2",
					"ST", "SC", "SS", "MCSID", "CONTINUATION MARKER 3",]
		data_types = [int, float, float, float, str,
						float, float, float, float, str,
						float, float, float, float,]
		
	else:
		fields = ["MID", "E", "G", "NU", "RHO", "A", "TREF", "GE", "CONTINUATION MARKER",
					"START LINE 2", "ST", "SC", "SS", "MCSID"]
		data_types = [int, float, float, float, float, float, float, float,
				str, float, float, float, int]

	id = int(data[1])
	bdf.mat1s[id] = {f: None for f in fields}
	populate_fields(bdf.mat1s, data, fields, data_types, id)		

def process_mat2(bdf, data, field_format):
	if field_format == "long":
		raise Exception("MAT2 card is only supported for small field format at this time")
	else:
		fields = ["MID", "G11", "G12", "G13", "G22", "G23", "G33", "RHO", "CONTINUATION MARKER",
					"START LINE 2", "A1", "A2", "A3", "TREF", "GE", "ST", "SC", "SS", "CONTINUATION MARKER",
					"MCSID"]
		data_types = [int, float, float, float, float, float, float, float, str,
					str, float, float, float, float, float, float, float, float, str,
					int]

def process_mat8(bdf, data, field_format):
	if field_format == "long":
		fields = ["MID", "E1", "E2", "NU12", "CONTINUATION MARKER",
	    			"G12", "G1Z", "G2Z", "RHO", "CONTINUATION MARKER 2",
				    "A1", "A2", "TREF", "Xt",  "CONTINUATION MARKER 3",
				    "Xc", "Yt", "Yc", "S", "CONTINUATION MARKER 4",
				    "GE", "F12", "STRN"]
		data_types = [int, float, float, float, str,
					float, float, float, float, str,
					float, float, float, float, str,
					float, float, float]
	else:
		fields = ["MID", "E1", "E2", "NU12", "G12", "G1Z", "G2Z", "RHO", "CONTINUATION MARKER",
					"START LINE 2", "A1", "A2", "TREF", "Xt", "Xc", "Yt", "Yc", "S", "CONTINUATION MARKER 2",
					"START LINE 3", "GE", "F12", "STRN"]
		data_types  = [int, float, float, float, float, float, float, float, str,
						str, float, float, float, float, float, float, float, float, str,
						str, float, float, float]
	
	id = int(data[1])
	bdf.mat8s[id] = {f: None for f in fields}
	populate_fields(bdf.mat8s, data, fields, data_types, id)		

def process_pbar(bdf, data, field_format):
	if field_format == "long":
		fields = ["PID", "MID", "A", "I1", "CONTINUATION MARKER",
					"I2", "J", "NSM", "BLANK", "CONTINUATION MARKER 2",
					"C1", "C2", "D1", "D2", "CONTINUATION MARKER 3",
					"E1", "E2", "F1", "F2", "CONTINUATION MARKER 4",
					"K1", "K2", "I12",
					]
		data_types = [int, int, float, float, str,
						float, float, float, str, str,
						float, float, float, float, str,
						float, float, float, float, str,
						float, float, float
						]
	else:
		fields = ["PID", "MID", "A", "I1", "I2", "J", "NSM", "BLANK", "CONTINUATION MARKER",
					"START LINE 2", "C1", "C2", "D1", "D2", "E1", "E2", "F1", "F2", "CONTINUATION MARKER 2",
					"START LINE 3", "K1", "K2", "I12"]
		data_types = [int, int, float, float, float, float, float, str, str,
						str, float, float, float, float, float, float, float, float, str,
						str, float, float, float]

	id = int(data[1])
	bdf.pbars[id] = {f: None for f in fields}
	populate_fields(bdf.pbars, data, fields, data_types, id)				

def process_pbeam(bdf, data, field_format):

	if field_format == "long":
		fields = ["PID", "MID", "A(A)", "I1(A)", "CONTINUATION MARKER",
					"I2(A)", "I12(A)", "J(A)", "NSM", "CONTINUATION MARKER 2",
					"C1(A)", "C2(A)", "D1(A)", "D2(A)", "CONTINUATION MARKER 3",
					"E1(A)", "E2(A)", "F1(A)", "F2(A)", "CONTINUATION MARKER 4",
					"SO", "X/XB", "A", "I1", "CONTINUATION MARKER 5",
					"I2", "I12", "J", "NSM", "CONTINUATION MARKER 6",
					"C1", "C2", "D1", "D2", "CONTINUATION MARKER 7",
					"E1", "E2", "F1", "F2", "CONTINUATION MARKER 8",
					"K1", "K2", "S1", "S2", "CONTINUATION MARKER 9",
					"NSI(A)", "NSI(B)", "CW(A)", "CW(B)", "CONTINUATION MARKER 10",
					"M1(A)", "M2(A)", "M1(B)", "M2(B)", "CONTINUATION MARKER 11",
					"N1(A)", "N2(A)", "N1(B)", "N2(B)", "CONTINUATION MARKER 12",
					]
		data_types = [int, int, float, float, str,
						float, float, float, float, str,
						float, float, float, float, str,
						float, float, float, float, str,
						str, float, float, float, str,
						float, float, float, float, str,
						float, float, float, float, str,
						float, float, float, float, str,
						float, float, float, float, str,
						float, float, float, float, str,
						float, float, float, float, str,
						float, float, float, float, str,
						]

	else:
		fields = ["PID", "MID", "A(A)", "I1(A)", "I2(A)", "I12(A)", "J(A)", "NSM(A)", "CONTINUATION MARKER",
					"START LINE 2", "C1(A)", "C2(A)", "D1(A)", "D2(A)", "E1(A)", "E2(A)", "F1(A)", "F2(A)", "CONTINUATION MARKER 2",
					"START LINE 3", "SO", "X/XB", "A", "I1", "I2", "I12", "J", "NSM", "CONTINUATION MARKER 3",
					"START LINE 4", "C1", "C2", "D1", "D2", "E1", "E2", "F1", "F2", "CONTINUATION MARKER 4",
					"START LINE 5", "K1", "K2", "S1", "S2", "NSI(A)", "NSI(B)", "CW(A)", "CW(B)", "CONTINUATION MARKER 5",
					"START LINE 6", "M1(A)", "M2(A)", "M1(B)", "M2(B)", "N1(A)", "N2(A)", "N1(B)", "N2(B)", "CONTINUATION MARKER 6"]

		data_types = [int, int, float, float, float, float, float, float, str,
						str, float, float, float, float, float, float, float, float, str,
						str, str, float, float, float, float, float, float, float, str,
						str, float, float, float, float, float, float, float, float, str,
						str, float, float, float, float, float, float, float, float, str,
						str, float, float, float, float, float, float, float, float, str,
						]
					
	id = int(data[1])
	bdf.pbeams[id] = {f: None for f in fields}

	# HANDLE IF LINE 2 IS NOT INCLUDED
	if len(data) >= fields.index("C1(A)") + 1:
		if field_format == "long":
			pass
		else:
			if "yes" in data[fields.index("C1(A)") + 1].lower() or "no" in data[fields.index("C1(A)") + 1].lower(): # +1 accounts for "PBEAM" in first line
				fields = ["PID", "MID", "A(A)", "I1(A)", "I2(A)", "I12(A)", "J(A)", "NSM(A)", "CONTINUATION MARKER",
							# "START LINE 2", "C1(A)", "C2(A)", "D1(A)", "D2(A)", "E1(A)", "E2(A)", "F1(A)", "F2(A)", "CONTINUATION MARKER 2",
							"START LINE 3", "SO", "X/XB", "A", "I1", "I2", "I12", "J", "NSM", "CONTINUATION MARKER 3",
							"START LINE 4", "C1", "C2", "D1", "D2", "E1", "E2", "F1", "F2", "CONTINUATION MARKER 4",
							"START LINE 5", "K1", "K2", "S1", "S2", "NSI(A)", "NSI(B)", "CW(A)", "CW(B)", "CONTINUATION MARKER 5",
							"START LINE 6", "M1(A)", "M2(A)", "M1(B)", "M2(B)", "N1(A)", "N2(A)", "N1(B)", "N2(B)", "CONTINUATION MARKER 6"]

				data_types = [int, int, float, float, float, float, float, float, str,
								# str, float, float, float, float, float, float, float, float, str,
								str, str, float, float, float, float, float, float, float, str,
								str, float, float, float, float, float, float, float, float, str,
								str, float, float, float, float, float, float, float, float, str,
								str, float, float, float, float, float, float, float, float, str,
								]
	
	populate_fields(bdf.pbeams, data, fields, data_types, id)


def process_pcomp(bdf, data, field_format):
	no_plies = 0

	if field_format == "long":
		raise Exception("PCOMP card is only supported for small field format at this time")
	else:
		fields = ["PID", "Z0", "NSM", "SB", "FT", "TREF", "GE", "LAM", "CONTINUATION MARKER",]
		data_types = [int, float, float, float, str, float, float, str, str,]

		ply_fields = ["START LINE", "MID", "T", "THETA", "SOUT", "MID", "T", "THETA", "SOUT", "CONTINUATION MARKER"]
		ply_fields_tpyes = [str, int, float, float, str, int, float, float, str, str]
		field_idx = 0
		
		line_count = 2

		# Add the plies
		if len(data) >= 11:
			ply_data = data[10:]

			for field in ply_data:
				if field_idx == 1 or field_idx == 5:
					no_plies += 1
				
				fields.append(f"{ply_fields[field_idx]}{no_plies}")				
				data_types.append(ply_fields_tpyes[field_idx])

				field_idx += 1
				if field_idx > 9:
					field_idx = 0

	id = int(data[1])
	bdf.pcomps[id] = {f: None for f in fields}
	populate_fields(bdf.pcomps, data, fields, data_types, id)

	# Remove any plies that have all none values
	for i in range(no_plies):
		ply = i + 1

		if [bdf.pcomps[id][f"MID{ply}"], bdf.pcomps[id][f"T{ply}"], bdf.pcomps[id][f"THETA{ply}"], bdf.pcomps[id][f"SOUT{ply}"]] == [None, None, None, None]:
			bdf.pcomps[id].pop(f"MID{ply}")
			bdf.pcomps[id].pop(f"T{ply}")
			bdf.pcomps[id].pop(f"THETA{ply}")
			bdf.pcomps[id].pop(f"SOUT{ply}")

def process_prod(bdf, data, field_format):
	if field_format == "long":
		raise Exception("PROD card is only supported for small field format at this time")
	else:
		fields = ["PID", "MID", "A", "J", "C", "NSM",]
		data_types = [int, int, float, float, float, float]
	
	id = int(data[1])
	bdf.prods[id] = {f: None for f in fields}
	populate_fields(bdf.prods, data, fields, data_types, id)	

def process_phsell(bdf, data, field_format):
	if field_format == "long":
		raise Exception("PSHELL card is only supported for small field format at this time")
	else:
		fields = ["PID", "MID", "T", "MID2", "12I/T**3", "MID3", "TS/T", "NSM", "CONTINUATION MARKER", "START LINE 2", "Z1", "Z2", "MID4"]
		data_types = [int, int, float, int, float, int, float, float, str, str, float, float, int]
	
	id = int(data[1])
	bdf.pshells[id] = {f: None for f in fields}
	populate_fields(bdf.pshells, data, fields, data_types, id)	

def populate_fields(dict, data, fields, data_types, id):	
	for idx, field in enumerate(data):
		fields_idx = idx -1
		#print(field)
		if fields_idx >= 0 and fields_idx <= len(fields) - 1:
			if field.strip() != "": # avoid blank fields:
				
				# add E to scientific format so python can convert to float
				if len(field.strip()) > 1:
					if "+" in field.strip()[1:] and "e" not in field.lower():
						field = field.replace("+", "e+")
					if "-" in field.strip()[1:] and "e" not in field.lower():
						field = list(field.strip())
						for idx, f in enumerate(field):
							if idx != 0 and f == "-":
								field[idx] = "e-"
						field = "".join(field)
				
				# Handle for double precision marker i.e De+
				if data_types[fields_idx] in [float, int]:
					if "De+" in field:
						field = field.replace("De+", "e+")
					elif "De-" in field:
						field = field.replace("De-", "e-")

				# if data type is string, remove leading and trailing space
				if data_types[fields_idx] is str:
					field = field.rstrip()
					field = field.lstrip()

				dict[id][fields[fields_idx]] = data_types[fields_idx](field)