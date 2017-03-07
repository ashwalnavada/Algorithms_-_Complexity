



#Ashwal Neelakanta Kalgodu
#UID:01619656

mens_list = ["victor","wyatt","xavier","yancey","zeus"]
womens_list =["amy","bertha","clare","diane","erika"]
mpref={
		'victor':["bertha","amy","diane","erika","clare"],
		'wyatt':["diane","bertha","amy","clare","erika"],
		'xavier':["bertha","erika","clare","diane","amy"],
		'yancey':["amy","diane","clare","bertha","erika"],
		'zeus':["bertha","diane","amy","erika","clare"]
	   }
wpref={'amy':["zeus","victor","wyatt","yancey","xavier"],
		'bertha':["xavier","wyatt","yancey","victor","zeus"],
		'clare':["wyatt","xavier","yancey","zeus","victor"],
		'diane':["victor","zeus","yancey","xavier","wyatt"],
		'erika':["yancey","wyatt","zeus","xavier","victor"]
	   }


matches_men = {'victor':'', 'wyatt':'', 'xavier':'', 'yancey':'', 'zeus':''}
matches_women = {'amy':'', 'bertha':'', 'clare':'', 'diane':'', 'erika':''}

men_procount= {'victor':0, 'wyatt': 0, 'xavier':0, 'yancey':0, 'zeus':0}
procount=0
count=len(mens_list)

while (any(v == '' for v in matches_men.itervalues())):
	#print "Yo"
	for c in range(count):
		#print "Yo1"
		#print mens_list[c]
		#print matches_men[mens_list[c]]
		if matches_men.get(mens_list[c]) == '':
			#print "Yo2"
			man = mens_list[c]
			for index, woman in enumerate(mpref[man]):
				#print "Yo3"
				if matches_women[woman]=='':
					#print "Yo4"
					matches_men[man] = woman
					matches_women[woman] = man
					men_procount[man]+=1
					#print matches_men
					#print matches_women
					break
				else:
					#print "Yo5"
					m_dash = matches_women[woman] # currently engaged
					m_index = wpref[woman].index(man) # new guy
					m_dash_index = wpref[woman].index(m_dash)
					#print woman, m_dash, m_dash_index
					if m_index < m_dash_index:
						matches_men[man] = woman
						matches_women[woman] = man
						matches_men[m_dash] = ''
						#print matches_men
						#print matches_women
						break
print ""			
print "The couples are:"	
print ""	
for key, val in matches_women.iteritems():
	print val + " and " + key
print ""