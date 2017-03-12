We are given a sequence of n numbers a1, . . . , an, which we assume are all distinct, 
	and we define an inversion to be a pair i < j such that ai > aj.
	We motivated the problem of counting inversions as a good measure of how different two orderings are. 
	However, one might feel that this measure is too sensitive. 
	Let’s call a pair a significant inversion if i < j and ai > 2aj. 
	Give an O(n log n) algorithm to count the number of significant inversions between two orderings.