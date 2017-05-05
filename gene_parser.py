import string
import sys
import pprint

if sys.version_info[0] < 3:
	from StringIO import StringIO
else:
	from io import StringIO 

import time 
import pandas as pd 
import numpy as np 
from pandas import Series, DataFrame 

## The next imports are for the visualizations


# %matplotlib inline
import random
import matplotlib.pyplot as plt
import seaborn as sns
# Parser to clean up and prepare data to make visualization of
# my genome. 

class Parser():
	# returns gene_array, a numpy array with all of the genomic code
	# like this: [rsid, chromosome, position, genotype] 
	# does not print anything, just returns the gene_array,
	# but you can uncomment print(df.head()) in the last function of the class
	# if you are not sure it's working.
	# As a side note, I wanted to put the columns in this order:
	# chromosome, rsid, genotype, position
	# but for some reason, as of 2/17/17 4:50PM
	# the order is chr, gen, pos, rsid.
	# I think this has something to do with the permutation, but I wasn't
	# bothered enough to spend more time trying to fix it. 

	def __init__(self, **args):
		self.filename = filename 
		self.genes = Parser.create_array(self, **args)  
		# self.f = f 
		self.read_data = Parser.open_file(self, **args)
		self.RLEN = Parser.row_length(self, **args) #row length ( constant )
		self.CLEN = Parser.col_length(self, **args) #col length ( constant )
		self.gene_array = Parser.reshape_array(self, **args)
		self.df = Parser.create_df(self, **args)

	def open_file(self, **args):
		# opens & reads file of genome, returns string read_data 
		with open('genome.txt') as read_data:
			read_data = read_data.read()
			return read_data

	def create_array(self, **args):
		# creates and shapes an array for the genomic data so that each row contains
		# rsid, chromosome, ?, and alleles 
		genes = Parser.open_file(self, **args) # split into list
		genes = genes.split() 
		genes = np.array(genes) # list into numpy array
		return genes 

	def row_length(self, **args):
		# returns row length constant RLEN 
		genes = Parser.create_array(self, **args)
		RLEN = len(genes) # row length, use to reshape
		return RLEN

	def col_length(self, **args):
		# returns column length constant CLEN 
		RLEN = Parser.row_length(self, **args)
		CLEN = RLEN/4 # column length, use to reshape 
		return int(CLEN) 

	def reshape_array(self, **args):
		# returns gene_array 
		CLEN = Parser.col_length(self, **args)
		genes = Parser.create_array(self, **args)
		genes = genes.reshape(CLEN,4) #CLEN must be integer or else gives deprecation warning
		# now we want to put the columns in the correct order
		# !!! As of 2/17/17 4:51PM this is not the order it's in, so I'll have to
		# figure out later how to get the order how I want it.
		# 0 rsid		 -> 1 
		# 1 chromosome 	 -> 0
		# 2 position 	 -> 3
		# 3 genotype	 -> 2

		# so the new order should be chromosme, rsid, genotype, position
		permu = [1,0,3,2]
		i = np.argsort(permu)
		genes = genes[:,i]
		gene_array = genes 
		# print(gene_array[0:30])
		return gene_array 

	## !!! FIX : 2/17/17 3:56PM 
	##     FIXED 2/17/17 4:49PM 
	## ??? Still want columns in a different order, but this isn't a dealbreaker
	## need to make a pandas dataframe from the numpy array. 

	def create_df(self, **args):
		# creates a pandas dataframe with 4 columns
		CLEN = Parser.col_length(self, **args)
		gene_array = Parser.reshape_array(self, **args)
		df = pd.DataFrame({
			'chromosome':		gene_array[:,0], 
			'rsid':				gene_array[:,1], 
			'genotype':			gene_array[:,2],
			'position':			gene_array[:,3] })
		# print(df.head())
		return df 


class MakeThing(Parser):
	# this is supposed to be for making graphs and stuff but I haven't done anythign yet
	def __init__(self, genes):
		self.genes = Parser.create_df(self, **args)

	def tryplot(self, genes):
		genes = Parser.create_df(self, **args)

		sns.lmplot('x', 'y', 'a', 'b', data=genes, fit_reg=False)


if __name__ == '__main__':
	#specifies filename & names
	filename = 'genome.txt'
	parser = Parser() 
	genes = parser.create_array()
	RLEN = parser.row_length()
	CLEN = parser.col_length()
	read_data = parser.open_file()
	gene_array = parser.reshape_array()
	df = parser.create_df()


