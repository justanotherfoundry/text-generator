#!/usr/bin/python2

import cgi, random, os, os.path

text_length = 3000

uppercase = u'A\xc1\xc0\xc2\xc4\u0102\u0100\xc3\xc5\u0104\u01fa\u1ea0\xc6\u01fcBC\u0106\u010a\u0108\u010c\xc7D\u010e\u0110\xd0E\xc9\xc8\u0116\xca\xcb\u011a\u0114\u0112\u0118FG\u0120\u011c\u011e\u0122H\u0124\u0126I\xcd\xcc\xce\xcf\u012c\u012a\u0128\u012eJ\u0134K\u0138\u0136L\u0139\u013f\u013d\u013b\u0141MN\u0143\u0147\xd1\u0145\u0149\u014aO\xd3\xd2\xd4\xd6\u014e\u014c\xd5\u0150\xd8\u01fe\u01a0\u0152PQR\u0154\u0158\u0156S\u015a\u015c\u0160\u015eT\u0164\u0162\xde\u0166U\xda\xd9\xdb\xdc\u016c\u016a\u0168\u016e\u0172\u0170\u01afVW\u1e82\u1e80\u0174\u1e84XY\xdd\u0176\u0178Z\u0179\u0179\u017b\u017d\u0391\u0386\u0392\u0393\u0394\u0395\u0388\u0396\u0397\u0389\u0398\u0399\u038a\u03aa\u039a\u039b\u039c\u039d\u039e\u039f\u038c\u03a0\u03a1\u03a3\u03a3\u03a4\u03a5\u038e\u03ab\u03b0\u03a6\u03a7\u03a8\u03a9\u038f\u0410\u0411\u0412\u0413\u0490\u0403\u0414\u0402\u0415\u0401\u0404\u0416\u0417\u0405\u0418\u0406\u0407\u0419\u0408\u041a\u040c\u041b\u0409\u041c\u041d\u040a\u041e\u041f\u0420\u0421\u0422\u040b\u0423\u040e\u0424\u0425\u0426\u0427\u040f\u0428\u0429\u042a\u042b\u042c\u042d\u042e\u042f'
lowercase = u'a\xe1\xe0\xe2\xe4\u0103\u0101\xe3\xe5\u0105\u01fb\u1ea1\xe6\u01fdbc\u0107\u010b\u0109\u010d\xe7d\u010f\u0111\xf0e\xe9\xe8\u0117\xea\xeb\u011b\u0115\u0113\u0119fg\u0121\u011d\u011f\u0123h\u0125\u0127i\xed\xec\xee\xef\u012d\u012b\u0129\u012fj\u0135k\u0138\u0137l\u013a\u0140\u013e\u013c\u0142mn\u0144\u0148\xf1\u0146\u0149\u014bo\xf3\xf2\xf4\xf6\u014f\u014d\xf5\u0151\xf8\u01ff\u01a1\u0153pqr\u0155\u0159\u0157s\u015b\u015d\u0161\u015ft\u0165\u0163\xfe\u0167u\xfa\xf9\xfb\xfc\u016d\u016b\u0169\u016f\u0173\u0171\u01b0vw\u1e83\u1e81\u0175\u1e85xy\xfd\u0177\xffz\u017a\u017a\u017c\u017e\u03b1\u03ac\u03b2\u03b3\u03b4\u03b5\u03ad\u03b6\u03b7\u03ae\u03b8\u03b9\u03af\u03ca\u03ba\u03bb\u03bc\u03bd\u03be\u03bf\u03cc\u03c0\u03c1\u03c2\u03c3\u03c4\u03c5\u03cd\u03cb\u03b0\u03c6\u03c7\u03c8\u03c9\u03ce\u0430\u0431\u0432\u0433\u0491\u0453\u0434\u0452\u0435\u0451\u0454\u0436\u0437\u0455\u0438\u0456\u0457\u0439\u0458\u043a\u045c\u043b\u0459\u043c\u043d\u045a\u043e\u043f\u0440\u0441\u0442\u045b\u0443\u045e\u0444\u0445\u0446\u0447\u045f\u0448\u0449\u044a\u044b\u044c\u044d\u044e\u044f\xdf\u0131'
arabic = u'\u0621\u0622\u0623\u0624\u0625\u0626\u0627\u0628\u0629\u062a\u062b\u062c\u062d\u062e\u062f\u0630\u0631\u0632\u0633\u0634\u0635\u0636\u0637\u0638\u0639\u063a\u063b\u063c\u063d\u063e\u063f\u0640\u0641\u0642\u0643\u0644\u0645\u0646\u0647\u0648\u0649'
letters = uppercase + lowercase + arabic

casedict = {}
for i in range(len(uppercase)):
	 casedict[lowercase[i]] = uppercase[i]
casedict[u'\u0131'] = u'I'

########################################################################################################################
########################################################################################################################

form = cgi.FieldStorage()

print "Content-Type: text/html" # HTML is following
print # blank line, end of headers

print '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<title>Just Another Test Text Generator</title>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	<style type="text/css">
		html { overflow-y: auto; }
	</style>
</head>
<body style="background:#eee">
	<p id="content">
'''

print "languages: "
input_languages = form.getlist("language")
for lang in input_languages:
		print lang

print "&nbsp;&nbsp;&nbsp;characters: "
if form.getvalue("characters") == "all":
		print "all characters"
		characters = u''
else:
		temp = unicode(form.getvalue("chars"), 'utf-8')
		characters = u''
		for i in range(len(temp)):
				if form.getlist("case") == ["allcaps"] and casedict.has_key(unicode(temp[i])):
						characters += casedict[temp[i]]
				else:
						if (temp[i] != u'\xdf'):
							characters += temp[i]
		print characters.encode('utf-8')

print "<br/>kerning: "
if form.getvalue("kernlevel") != "0":
	if form.getvalue("kern") == "typ":
			print "typical pairs"
	else:
			print form.getvalue("kernchars")
else: print "not affected"
if form.getvalue("kernlevel") == "s3":
	kernglobal = -1.0
	print "suppress at -3"
if form.getvalue("kernlevel") == "s2":
	kernglobal = -0.6
	print "suppress at -2"
if form.getvalue("kernlevel") == "s1":
	kernglobal = -0.3
	print "suppress at -1"
if form.getvalue("kernlevel") == "0":
	kernglobal = 0
if form.getvalue("kernlevel") == "b1":
	kernglobal = 0.3
	print "boost at 1"
if form.getvalue("kernlevel") == "b2":
	kernglobal = 0.6
	print "boost at 2"
if form.getvalue("kernlevel") == "b3":
	kernglobal = 0.9
	print "boost at 3"

print "&nbsp;&nbsp;&nbsp;letter variety: "
equalisation = 0.007 * int(form.getvalue("lettervariety"))
print " ", form.getvalue("lettervariety")

print "&nbsp;&nbsp;&nbsp;pair variety: "
equalis_pair = 0.01 * int(form.getvalue("pairvariety"))
print " ", form.getvalue("pairvariety")

print "<br><br>"

########################################################################################################################
########################################################################################################################

triplets_filename = os.path.join( 'languages', 'triplets' )
for lang in input_languages:
		triplets_filename += "_" + lang
triplets_filename += ".txt"

if not os.path.isfile(triplets_filename):
	triplets_filename = triplets_filename.replace( 'languages', 'cache' )

file_output_merged = None
if not os.path.isfile(triplets_filename):
	threshold = 4
	file_output_merged = "combined from"
	
	# these are the two values used for the average (median-ish)
	n = len(input_languages)
	averg1 = n/3
	averg2 = (n+2)/3
	
	# load all files/lists
	triplets = []
	inputs = []
	for i in range(n):
		f=open( os.path.join( 'languages', 'triplets_'+input_languages[i]+'.txt'), 'r' )
		file_output_merged += " " + input_languages[i]
		triplets.append({})
		inputs = f.readlines()
		f.close()
		del inputs[0]
		for t in inputs:
			triplets[i][t.split()[1]] = t.split()[0]
	
	# build main array
	combi = {}
	for i in range(n):
		for tri in triplets[i]:
			if combi.has_key(tri):
				combi[tri].append(int(triplets[i][tri]))
			else:
				combi[tri] = [ int(triplets[i][tri]) ]
	
	# build the averages array
	averages = {}
	for t in combi:
	
		lct = len(combi[t])
		for i in range( n - lct ):
			combi[t].append(0)
	
		sum_v = 0
		for i in combi[t]:
			sum_v += i
		
	
		if len(unicode(t,'utf-8')) == 3:  # if it is a triplet
			# this is the arithmetic average of the averg1-th most frequent and the averg2-th most frequent (most frequent: n - 1)
			averages[t] = 0.5 * ( combi[t][ averg1  ] + combi[t][ averg2 ] )
		else:   # if it is not a triplet, i.e. word length
			averages[t] = int( sum_v/n )
	
	fom = [ ]
	
	# build output strings
	for t in averages:
		if len(unicode(t,'utf-8')) == 3:
			if averages[t] > threshold:
				fom.append("\n" + str( int(averages[t]) ) + "\t" + t )
		else:
			fom.append("\n" + str( averages[t] ).rjust(20) + "\t" + t )
	
	fom.sort()
	for m in fom:
		file_output_merged += m
	
	# write output file
	try:
		f=open(triplets_filename, 'w')
		f.write(file_output_merged)
		f.close()
	except IOError:
		# no writing permissions
		pass
		
########################################################################################################################
########################################################################################################################


# initial bits and stuff
wordlen_in  = [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1 ]
wordlen_out = [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1 ]
wordmax = 6
wordsum_in  = wordmax
wordsum_out = wordmax-2
tweaklimit = 30.0
tweak_upto = 15
text_length += 10
random.seed()
file_output = (u"")
if characters != "":
	characters = "_" + characters
frequencymeter = {}
frequencytotal = 1
numberofletters = 0

frequencymeterUC = {}
frequencytotalUC = 1
numberoflettersUC = 0

pairmeter = {}
pairtotal = 1
numberofpairs = 0

# import kerning file
if kernglobal != 0:
	if form.getvalue("kern") == "typ":
		f=open('kerning.txt', 'r')
		inputs = f.readlines()
		f.close()
		del inputs[0]
		kerntweaks = {}
		for inp in inputs:
			kerntweaks[inp.split()[1]] = 1.0 * int(inp.split()[0])**kernglobal
	else:
		kerntweaks = {}
		for inp in form.getvalue("kernchars").split():
			kerntweaks[inp] = 100.0 ** kernglobal
	 
# import file
if file_output_merged:
	inputs = file_output_merged.split( '\n' )
else:
	f=open(triplets_filename, 'r')
	inputs = f.readlines()
	f.close()
del inputs[0]

# build wordlen_in
for i in range(len(wordlen_in)):
	wordlen_in[int(inputs[0].split()[1][4:7])] += int(inputs[0].split()[0])
	wordsum_in += int(inputs[0].split()[0])
	del inputs[0]
	if len( unicode(inputs[0], 'utf-8').split()[1] ) == 3: break

# build duplets
duplets = {}
for inp in inputs:
	temp = unicode(inp, 'utf-8').split()[1]
	t = u''
	for i in range(len(temp)):
		if form.getlist("case") == ["allcaps"] and casedict.has_key(unicode(temp[i])):
				t += casedict[temp[i]]
		else:
				t += temp[i]

	v = int(unicode(inp, 'utf-8').split()[0])
	# ignore all triplets that contain the wrong characters
	if characters != "":
		if not t[0] in characters : continue
		if not t[1] in characters : continue
		if not t[2] in characters : continue
	if duplets.has_key(t[0:2].encode('utf-8')):
		if duplets[t[0:2].encode('utf-8')].has_key(t[2].encode('utf-8')):
			duplets[t[0:2].encode('utf-8')][ t[2].encode('utf-8') ] += v
		else:
			duplets[t[0:2].encode('utf-8')][ t[2].encode('utf-8') ] = v
	else:
		duplets[t[0:2].encode('utf-8')] = { t[2].encode('utf-8') : v }

# clean dead ends
dead_duplets = []
for d in duplets:
	dead_letters = []
	for v in duplets[d]:
		if not duplets.has_key(unicode(d,'utf-8')[1].encode('utf-8')+v):
			dead_letters.append(v)
	for v in dead_letters:
		del duplets[d][v]
	if len(duplets[d]) == 0:
		dead_duplets.append(d)
for d in dead_duplets:
	del duplets[d]
# clean dead ends 2
dead_duplets = []
for d in duplets:
	dead_letters = []
	for v in duplets[d]:
		if not duplets.has_key(unicode(d,'utf-8')[1].encode('utf-8')+v):
			dead_letters.append(v)
	for v in dead_letters:
		del duplets[d][v]
	if len(duplets[d]) == 0:
		dead_duplets.append(d)
for d in dead_duplets:
	del duplets[d]

# build text
if characters != u"" and not "." in characters:
	current = random.choice(characters) + u"_"
else: current = u"._"
wordtmp = 0

for i in range(text_length):
	
	# check for end of word
	if current[1] in letters:
		wordtmp += 1
	else:
		if current[0] in letters:
			if wordtmp > wordmax: wordtmp = wordmax
			wordlen_out[wordtmp] += 1
			wordsum_out += 1
		wordtmp = 0
	
	# set tweakblank factor
	if wordtmp >= wordmax:
		tweakblank = ( wordtmp - wordmax + 1 ) * 60
	elif wordtmp != 0:
		tweakblank = (1.0 * (wordlen_in[wordtmp]*wordsum_out) / (wordlen_out[wordtmp]*wordsum_in))**4
		if wordtmp > tweak_upto and tweakblank < equalisation*50:
			tweakblank = equalisation * 50 + 2
		elif tweakblank > tweaklimit:
			tweakblank = tweaklimit
		elif tweakblank < 0.25:
			tweakblank = 0.25
	else:
		tweakblank = 1
		
	if duplets.has_key(current.encode('utf-8')): # and duplets[current.encode('utf-8')] != {}:
		cumulative = []
		sum = 1
		lastone = i
		for j in duplets[current.encode('utf-8')]:
			# set multiplier
			multiplier = 1 
			if characters != "":
				multiplier = 2** (characters.count(unicode(j,'utf-8'))-1)

			# set tweakletter
			if unicode(j,'utf-8') in (lowercase+arabic):
				if not frequencymeter.has_key(j):
					frequencymeter[j] = 1
					numberofletters += 1
				tweakletter = 1.0 + equalisation * ( (frequencytotal/frequencymeter[j]/numberofletters)*5 - 1) 
			elif unicode(j,'utf-8') in uppercase:
				if not frequencymeterUC.has_key(j):
					frequencymeterUC[j] = 1
					numberoflettersUC += 1
				tweakletter = 1.0 + equalisation * ( (frequencytotalUC/frequencymeterUC[j]/numberoflettersUC)*5 - 1) 
			else:
				tweakletter = tweakblank

			# set tweakpair
			currentpair = current[1].encode('utf-8')+j
			if not pairmeter.has_key(currentpair):
				pairmeter[currentpair] = 4
				numberofpairs += 1
			tweakpair = 1.0 + equalis_pair * ( (pairtotal/pairmeter[currentpair]/numberofpairs)*5 - 1) 
			if ' ' in currentpair:
				tweakpair = 1.0

			# set tweakkernpair
			if kernglobal != 0 and kerntweaks.has_key(currentpair):
				tweakkernpair = kerntweaks[currentpair]
			else:
				tweakkernpair = 1

			sum += 1.0 * duplets[current.encode('utf-8')][j] * tweakletter * tweakpair * tweakkernpair * multiplier
			cumulative.append(sum)
		correction = 55000.0 / sum
		for j in range(len(cumulative)):
				cumulative[j] = int(cumulative[j] * correction)
		randm = random.randrange(55000)
		for j in range(len(cumulative)):
			if randm < cumulative[j]:
				# new character is chosen
				current = current[1] + unicode(duplets[current.encode('utf-8')].keys()[j],'utf-8')
				if True or i > 100:
					file_output += current[1].replace("_"," ")
				if frequencymeter.has_key(current[1].encode('utf-8')):
					frequencymeter[current[1].encode('utf-8')] += 1
				if frequencymeterUC.has_key(current[1].encode('utf-8')):
					frequencymeterUC[current[1].encode('utf-8')] += 1
				if current[1] in lowercase:
					frequencytotal += 1
				if current[1] in uppercase:
					frequencytotalUC += 1
				if pairmeter.has_key(current.encode('utf-8')):
						pairmeter[current.encode('utf-8')] += 1
						pairtotal += 1
				break
	else:
		if characters != "":
			current = current[1] + random.choice(u"____"+characters)
		else:
			current = current[1] + random.choice(u"____.....,,,,!?")
		file_output += current[1].replace("_"," ")  # replace with string.join

file_output += ".</bdo>&nbsp;&#150;&nbsp;generated by the <a href='https://justanotherfoundry.com'>JAF</a> Test Text Generator [https://justanotherfoundry.com]"

if form.getlist("frequencies") == ["output"]:
		# add character frequencies lowercase
		file_output += """<br><br><br>character frequencies:<br><br>
		<table border='0'><tr><td align='right'>"""
		tobesorted = []
		for c in frequencymeter:
				if frequencymeter[c] != 1:
					line = str(frequencymeter[c]-1).rjust(6) + u"&nbsp;&nbsp;</td><td align='center'>"
					if "ar" in form.getlist("language") or "he" in form.getlist("language") or "fa" in form.getlist("language"):
						line += "<bdo dir='rtl'>"
					line += unicode(c,'utf-8') + "</bdo>"
					tobesorted.append( line )
		tobesorted.sort()
		tobesorted.reverse()
		for c in tobesorted:
				file_output += c + "</td></tr><tr><td align='right'>"
		
		file_output += "&nbsp;</td></tr><tr><td align='right'>"

		# add character frequencies uppercase
		tobesorted = []
		for c in frequencymeterUC:
				if frequencymeterUC[c] != 1:
					line = str(frequencymeterUC[c]-1).rjust(6) + u"&nbsp;&nbsp;</td><td align='center'>"
					if "ar" in form.getlist("language") or "he" in form.getlist("language") or "fa" in form.getlist("language"):
						line += "<bdo dir='rtl'>"
					line += unicode(c,'utf-8') + "</bdo>"
					tobesorted.append( line )
		tobesorted.sort()
		tobesorted.reverse()
		for c in tobesorted:
				file_output += c + "</td></tr><tr><td align='right'>"

		file_output += "</td></tr></table>"
		file_output += """<br><br>pair frequencies:<br><br>
		<table border='0'><tr><td align='right'>"""

		# add pair frequencies
		tobesorted = []
		for c in pairmeter:
				if pairmeter[c] != 4:
					line = str(pairmeter[c]-4).rjust(6) + u"&nbsp;&nbsp;</td><td align='center'>"
					if "ar" in form.getlist("language") or "he" in form.getlist("language") or "fa" in form.getlist("language"):
						line += "<bdo dir='rtl'>"
					line += unicode(c,'utf-8') + "</bdo>"
					tobesorted.append( line )
		tobesorted.sort()
		tobesorted.reverse()
		for c in tobesorted:
				file_output += c + "</td></tr><tr><td align='right'>"
		file_output += "</td></tr></table>"

# write output file
if "ar" in form.getlist("language") or "he" in form.getlist("language") or "fa" in form.getlist("language"):
	print "<bdo dir='rtl'><p align='right'>"
print file_output.encode('utf-8')

print '</p>'
print open("../shared/shared-bottom.html").read()
print '</body></html>'