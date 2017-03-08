#Ashwal Neelakanta Kalgodu

import operator
# contestant_hash = key (name), value (array of swim time, run time, bike time)
contestant_hash = {'Rob' : [10,4,8],
				   'Tom' : [12,9,6],
				   'Dick': [9,9,4]
				   }

#creating a new hash with added run and bike times.
run_bike_added_hash = {}

for names,times_array in contestant_hash.iteritems():
	run_bike_added_hash[names] = times_array[1]+times_array[2]

print ""
print "Printing the contestants in the manner -> name: [swim time, run time, bike time]"
print ""
print "The order in which the contestents need to be sent out is as follows:"
print ""

#Sorting and printing the contestants in the most optimal order.
for key, value in sorted(run_bike_added_hash.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    print key + ": " + str(contestant_hash[key])