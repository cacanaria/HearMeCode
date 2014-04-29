import sys
bread = int(sys.argv[1])
pb = int(sys.argv[2])
jelly = int(sys.argv[3])
#bread = 10
#pb = 4
#jelly = 9

# # To satisfy the first goal:
# #		If you have enough bread (2 slices), peanut butter (1), and jelly (1), print a message like "I can make a peanut butter and jelly sandwich"; 
# #		If you don't; print a message like "Looks like I don't have a lunch today"
# if bread >= 2 and pb >= 1 and jelly >= 1:
# 	print "Hooray! You can make a PB&J!  ...but really, why would you? You're allergice to PB, Christie!"
# else:
# 	print "Bummer, no PB&J for you!"

# # To satisfy the second goal:
# #		Continue from the first goal, and add:
# #		If you have enough bread (at least 2 slices), peanut butter (at least 1), and jelly (at least 1), print a message like "I can make this many sandwiches: " and then calculate the result.
# #		If you don't; you can print the same message as before

# if bread >= 2 and pb >= 1 and jelly >= 1 and pb > jelly and bread >= 2*jelly:
# 	print "You can make {0} sandwiches!".format(jelly)
# elif bread >= 2 and pb >= 1 and jelly >= 1 and pb < jelly and bread >= 2*pb:
# 	print "You can make {0} sandwiches!".format(pb)
 
# Brad helped me re-think my logic tree and we came up with this:
if bread <2 or jelly<1 or pb<1:
	print "Tough luck! No PB&J for you!" 
else:
	print "Good news! You can make a tasty (yucky) treat!"
	if bread < jelly*2 and bread < pb*2:
		print "Buy more bread for more sammiches. At least you can make {0} PB&Js".format(bread/2)
		sandwiches = bread/2
	elif jelly < pb and bread >= 2*jelly:
		print "You might want to buy more jelly! You can whip up {0} PB&Js.".format(jelly)
		sandwiches = jelly
	elif bread <= 2*pb:
		print "You might consider buying more pb, but really why would you want to? Just eat your {0} sandwiches and consider yourself lucky!".format(bread/2)	
		sandwiches = bread/2
	elif pb < jelly and bread >= 2*pb:
		print "You can make {0} PB&Js".format(pb)	
		sandwiches = pb


# To satisfy the third goal:
#		Continue from the second goal, and add:
#		If you have an odd number of slices of bread* and odd amount of peanut butter and jelly, print a message like before, but mention that you can make an open-face sandwich, too.
#		If you don't have enough ingredients; still print the same message as before
#		* To calculate whether you have an odd number, see https://github.com/shannonturner/python-lessons/blob/master/section_01_(basics)/simple_math.py
if bread <2 or jelly<1 or pb<1:
	print ""
else:	
	if bread%2 > 0 and jelly > sandwiches and pb > sandwiches:
		print "and you can have an open-face PB&J sandwich, too!"
	else:	
		print ""

# To satisfy the fourth goal:
#		Continue from the third goal, but this time if you don't have enough ingredients, print a message that tells you which ones you're missing.

# To satisfy the fifth goal:
#		Continue from the fourth goal, but this time if you have enough bread and peanut butter but no jelly, print a message that tells you that you can make a peanut butter sandwich
if bread < (sandwiches*2) + 2:
	""
else:
	if 	jelly >= sandwiches +1:
		print "AND you can have extra jelly sandwich!"
	elif pb >= sandwiches +1:
		print "ANd you can have a pb sandwich!"	


#		Or if you have more peanut butter and bread than jelly, that you can make a certain number of peanut butter & jelly sandwiches and a certain number of peanut butter sandwiches
