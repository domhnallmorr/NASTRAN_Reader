import os 
import pandas as pd
from nastran_reader import bdf_cards

class BdfFile:
	def __init__(self, filepath, process_includes=True, verbose=False):
		self.version = "V0.5.0"
		assert os.path.isfile(filepath) is True, f'\nThe following supplied file does not exist:\n\t"{filepath}"'
		
		self.setup_variables()
		
		self.verbose = verbose
		self.process_includes = process_includes
		self.filepath = filepath
		
		if self.verbose is True:
			print(f"Processing {self.filepath}")
		
		# READ IN THE FILE DATA
		with open(self.filepath) as f:
			if self.verbose:
				print("\tReading File")
			self.data = f.readlines()
		
		if self.process_includes:
			self.get_all_include_files()
		self.remove_comments_and_blank_lines()
		self.parse_file()

		print(f"{len(self.errors)} Errors Occured")
		for error in self.errors:
			print("\t" + error)

		self.generate_summary()

	def setup_variables(self):
		self.current_section = "excecutive control"
		self.include_files = {}
		self.summary = {}

		self.errors = []
		self.number_of_errors = 0
		
		# CARDS
		self.cbars = {}
		self.cbeams = {}
		self.celas1s = {}
		self.cord2rs = {}
		self.cquad4s = {}
		self.ctria3s = {}
		self.crods = {}
		self.forces = {}
		self.gravs = {}
		self.grids = {}
		self.mat1s = {}
		self.mat2s = {}
		self.mat8s = {}
		self.pbars = {}
		self.pbeams = {}
		self.pcomps = {}
		self.pelass = {}
		self.prods = {}
		self.pshells = {}
		self.rbe2s = {}
		self.rbe3s = {}
		self.spc1s = {}
		self.spcadds = {}

		self.cards = {
			"CBARs": self.cbars,
			"CBEAMs": self.cbeams,
			# "CELAS1s": self.celas1s,
			"CORD2Rs": self.cord2rs,
			"CQUAD4s": self.cquad4s,
			"CTRIAs": self.ctria3s,
			"CRODs": self.crods,
			"FORCEs": self.forces,
			"GRAVs": self.gravs,
			"GRIDs": self.grids,
			"MAT1s": self.mat1s,
			"MAT2s": self.mat2s,
			"MAT8s": self.mat8s,
			"PBARs": self.pbars,
			"PBEAMs": self.pbeams,
			"PCOMPs": self.pcomps,
			# "PELASs": self.pelass,
			"PRODs": self.prods,
			"PSHELLs": self.pshells,
			# "RBE2s": self.rbe2s,
			# "RBE3s": self.rbe3s,
			# "SPC1s": self.spc1s,
			# "SPCADDs": self.spcadds,

		}
	def get_all_include_files(self):
		if self.verbose is True:
			print("Searching for Input Files")
			
		self.get_include_files_in_bdf(self.data, self.filepath)
		
		for include_file in self.include_files.keys():
			for line in self.include_files[include_file]:
				self.data.append(line)
		
		if self.verbose is True:
			print(f"{len(self.include_files.keys())} Include Files Added")
			
	def get_include_files_in_bdf(self, data, filepath):
		file_includes = []
		for idx, line in enumerate(data):
			if line.lower().startswith("include"):
				path = line[7:].lstrip().rstrip().replace("'", "")
				# find ending line 
				end_idx = None
				
				if line.rstrip().endswith("'") is False:
					for i in range(100):
						
						path = path + data[idx+i+1].lstrip().rstrip().replace("'", "")
						if data[idx+i+1].rstrip().endswith("'"):
							break
				
				filename = os.path.join(os.path.dirname(filepath), path)	
				
				if os.path.isfile(filename) is False:
					self.errors.append(f"The following include file does not exist\n\t{filename}")
					self.number_of_errors += 1
				elif filename.endswith(".pch") is False: # IGNORE PUNCH FILES
					print(f"\tAdding {filename}")
					
					with open(filename) as include_file:
						include_data = include_file.readlines()
					
					self.include_files[filename] = include_data
					self.get_include_files_in_bdf(include_data, filepath)
				
				
	def remove_comments_and_blank_lines(self):
		if self.verbose is True:
			print("Removing Comments and Blank Lines")
		
		data = []
		for line in self.data:
			if line.strip().startswith("$") is False and len(line.strip()) > 0:
				data.append(line.rstrip().ljust(80))
				
		self.data = data
		
	def parse_file(self):
		if self.verbose is True:
			print("\tParsing File")

		for idx, line in enumerate(self.data):
			field_format = self.identify_format_type(line)

			# ---------------- CBAR ----------------
			if line.lower().startswith("cbar ") or line.lower().startswith("cbar*") or line.lower().startswith("cbeam,"):
				self.process_card(idx, "cbar", bdf_cards.process_cbar, field_format)
				
			# ---------------- CBEAM ----------------
			elif line.lower().startswith("cbeam ") or line.lower().startswith("cbeam*") or line.lower().startswith("cbeam,"):
				self.process_card(idx, "cbeam", bdf_cards.process_cbeam, field_format)

			# ---------------- CORD2R ----------------
			elif line.lower().startswith("cord2r ") or line.lower().startswith("cord2r*") or line.lower().startswith("cord2r,"):
				self.process_card(idx, "cord2r", bdf_cards.process_cord2r, field_format)

			# ---------------- CTRIA3 ----------------
			elif line.lower().startswith("ctria3 ") or line.lower().startswith("ctria3*") or line.lower().startswith("ctria3,"):
				self.process_card(idx, "ctria3", bdf_cards.process_ctria3, field_format)
				
			# ---------------- CQUAD ----------------
			elif line.lower().startswith("cquad4 ") or line.lower().startswith("cquad4*") or line.lower().startswith("cquad4,"):
				self.process_card(idx, "cquad4", bdf_cards.process_cquad4, field_format)

			# ---------------- CROD ----------------
			elif line.lower().startswith("crod ") or line.lower().startswith("crod*") or line.lower().startswith("crod,"):
				self.process_card(idx, "crod", bdf_cards.process_crod, field_format)
				
			# ---------------- FORCE ----------------
			elif line.lower().startswith("force ") or line.lower().startswith("force*") or line.lower().startswith("force,"):
				self.process_card(idx, "force", bdf_cards.process_force, field_format)

			# ---------------- GRAV ----------------
			elif line.lower().startswith("grav ") or line.lower().startswith("grav*") or line.lower().startswith("grav,"):
				self.process_card(idx, "grav", bdf_cards.process_grav, field_format)

			# ---------------- GRID ----------------
			elif line.lower().startswith("grid ") or line.lower().startswith("grid*") or line.lower().startswith("grid,"):
				self.process_card(idx, "grid", bdf_cards.process_grid, field_format)

			# ---------------- MAT1 ----------------
			elif line.lower().startswith("mat1 ") or line.lower().startswith("mat1*") or line.lower().startswith("mat1,"):
				self.process_card(idx, "mat1", bdf_cards.process_mat1, field_format)

			# ---------------- MAT8 ----------------
			elif line.lower().startswith("mat8 ") or line.lower().startswith("mat8*") or line.lower().startswith("mat8,"):
				self.process_card(idx, "mat8", bdf_cards.process_mat8, field_format)
				
			# ---------------- PBAR ----------------
			elif line.lower().startswith("pbar ") or line.lower().startswith("pbar*") or line.lower().startswith("pbar,"):
				self.process_card(idx, "pbar", bdf_cards.process_pbar, field_format)
				
			# ---------------- PBEAM ----------------
			elif line.lower().startswith("pbeam ") or line.lower().startswith("pbeam*") or line.lower().startswith("pbeam,"):
				self.process_card(idx, "pbeam", bdf_cards.process_pbeam, field_format)

			# ---------------- PCOMP ----------------
			elif line.lower().startswith("pcomp ") or line.lower().startswith("pcomp*") or line.lower().startswith("pcomp,"):
				self.process_card(idx, "pcomp", bdf_cards.process_pcomp, field_format)

			# ---------------- PSHELL ----------------
			elif line.lower().startswith("pshell ") or line.lower().startswith("pshell*") or line.lower().startswith("pshell,"):
				self.process_card(idx, "pshell", bdf_cards.process_phsell, field_format)

	def identify_format_type(self, line):
		field_format = "short"
		if "," in line:
			field_format = "free"
		elif "*" in line:
			field_format = "long"
			
		return field_format

	def get_card_lines(self, idx, field_format):
		i = 1
		while True:
			if idx + i < len(self.data):
				if field_format == "short":
					if self.data[idx + i].startswith(" ") is False:
						if self.data[idx + i][0].startswith("+") is False:
							break
							
				elif field_format == "free":
					if self.data[idx + i].startswith(",") is False:
						break
						
				elif field_format == "long":
					if self.data[idx + i][0] != "*":
						break
			else:
				break
			i += 1	
		
		return ''.join(self.data[idx:idx+i])

	def process_card(self, line_idx, card_type, card_func, field_format):
		data = self.get_card_lines(line_idx, field_format)
		data = self.process_data_into_fields(data, field_format)
		
		card_func(self, data, field_format)

	def process_data_into_fields(self, line, field_format):
		line = line.replace("\t", "   ")
		data = []
		if field_format == "short" or field_format == "long":
			res = []
			if field_format == "short":
				chunk_len = 8
				for idx in range(0, len(line), chunk_len):
					res.append(line[idx : idx + chunk_len])
						
			elif field_format == "long":
				line = line.replace("*", " ")
				res.append(line[:8])
				chunk_len = 16
				for idx in range(8, len(line), chunk_len):
					res.append(line[idx : idx + chunk_len])
			
			for idx, field in enumerate(res):
				if field.strip() == "-.":
					res[idx] = ""
			return res
			
		elif field_format == "free":
			return line.split(",")	
				
	def generate_summary(self):
		self.summary = {}
		for card in self.cards.keys():
			self.summary[card] = len(self.cards[card])

if __name__ == "__main__":

	bdf = BdfFile(r"C:\Users\ev662f\Desktop\NEW_UPP_ATT_POS_FLT_new(1).bdf", verbose=True)
	# bdf = BdfFile(r"C:\Users\ev662f\Desktop\test.bdf", verbose=True)
	print(bdf.mat8s)