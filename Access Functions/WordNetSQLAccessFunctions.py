# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:          WordNetAccessFunctions
# Purpose:       providing access functions for manipulating WordNet
#
# Authors:       Benchanaa Meriem & Khadir Ahlem Chérifa(meriem.benchanaa[at]gmail.com & khadir.ahlem[at]gmail.com)
# Institution:   University of Science and Technologies Houari Boumediene
#
# Created:       17-05-2015
# Last Modified: 15-04-2018 
# Copyright:     (c) 
# Licence:       GPL
#-------------------------------------------------------------------------------

import sqlite3
import sys
import math
from math import*
import codecs
import fileinput
import os
import string
from cPickle import dump
from cPickle import load	
import re
from collections import defaultdict
	  
	
class WordNetAccessFunctionsClass:
	"""
	WordNet Access Functions Class
	"""

	def __init__(self):
		print "start WordNet Access Functions"

	def getHyponym (self, synsetID, cursor):
		"""
		Return the sons of a given arabic synset.
		@param synsetID: input synsetID the identifier of a synset from WordNet.
		@type synsetID: String.
		@param cursor: the pointer on the WordNet database.
		@type cursor: operator.
		@return: the query answer, the set of the son(s).
		rtype: list.
		"""
		
		#query the database on the link table to get the father(s) synset
		t=(synsetID,)
		cursor.execute(''' SELECT link2 FROM link WHERE link1 =? and type = 'has_hyponym' ''', t); 
										
		rows = cursor.fetchall()

		hyponyms = [row[0] for row in rows]
		
		return hyponyms
	
		
	def getHypernym (self, synsetID, cursor):
		"""
		Return the direct father(s) of a given arabic synset.
		@param synsetID: input synsetID the identifier of a synset from WordNet.
		@type synsetID: String.
		@param cursor: the pointer on the WordNet database.
		@type cursor: operator.
		@return: the query answer, the set of the father(s).
		rtype: list.
		"""
		
		#query the database on the link table to get the father(s) synset
		t=(synsetID,)
		cursor.execute(''' SELECT link1 FROM link WHERE link2 =? and type = 'has_hyponym' ''', t); 
										
		rows = cursor.fetchall()

		hypernyms = [row[0] for row in rows]
		
		return hypernyms

	def getHyponymEN (self, synsetID, cursor):
		"""
		Return the sons of a given english synset.
		@param synsetID: input synsetID the identifier of a synset from WordNet.
		@type synsetID: String.
		@param cursor: the pointer on the WordNet database.
		@type cursor: operator.
		@return: the query answer, the set of the son(s).
		rtype: list.
		"""
		
		#query the database on the link table to get the son(s) synset
		t=(synsetID,)
		cursor.execute(''' SELECT link1 FROM link WHERE link2 =? and type = 'hyponym' ''', t); 
										
		rows = cursor.fetchall()

		hyponyms = [row[0] for row in rows]
		
		return hyponyms
				

	def getHypernymEN (self, synsetID, cursor):
		"""
		Return the sons of a given english synset.
		@param synsetID: input synsetID the identifier of a synset from WordNet.
		@type synsetID: String.
		@param cursor: the pointer on the WordNet database.
		@type cursor: operator.
		@return: the query answer, the set of the father(s).
		rtype: list.
		"""
		
		#query the database on the link table to get the father(s) synset
		t=(synsetID,)
		cursor.execute(''' SELECT link2 FROM link WHERE link1 =? and type = 'hyponym' ''', t); 
										
		rows = cursor.fetchall()

		hypernyms = [row[0] for row in rows]
		
		return hypernyms

	def getEquivalentARfromEN(self, synsetidEN, cursor):
		"""
		Give the arabic synset equivalent in the taxonomy, to a given english synset.
		@param synsetidEN: input synsetidEN the identifier of an english synset from WordNet.
		@type synsetidEN: String.
		@param cursor: the pointer on the WordNet database.
		@type cursor: operator.
		@return: the query answer, the arabic synset equivalent.
		rtype: String.
		"""
		t = (synsetidEN,)
		cursor.execute(''' SELECT link1 FROM link WHERE link2 =? and type ='equivalent' ''', t);
		rows = cursor.fetchall()

		synsetidAR = [row[0] for row in rows]
		#print "synsetidAR  ", synsetidAR, "\n"

		return synsetidAR


	def readFile(self, filename):
		"""
		Could be useful for reading files containing arabic caracters
		"""
		File = codecs.open(filename, mode = "r", encoding = "utf-8")
		text = File.read()
		lines = text.split("\n")
		return lines


if __name__=="__main__":

	WordNetAccessFunctions = WordNetAccessFunctionsClass();

	#Put the database in the same folder as this .py programme
	conn = sqlite3.connect('arabicwordnetExtended.sqlite')
	c = conn.cursor()

	#The roots list of the AWN taxonomy of nouns
	startersNouns = [u"HaAlap_n1AR", u"Hadav_n2AR", u"ZaAhirap_n1AR", u"jamaAEap_n5AR", u"kayonuwnap_n1AR", u"milok_n1AR", u"miyozap_nafosiy~ap_n1AR", u"tajoriyd_n1AR"]

	
	#Example of how to use the functions.
	Hypers = WordNetAccessFunctions.getHypernym("sabab_n3AR", c)

	print Hypers





	print "OK \n"

