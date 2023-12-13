awk '{
	print "field2_length : "length($2);
	print "field3_length : "length($3);
	print "field4_length : "length($4);
	print "nb_of_fields : "NF;
} END {
	print "number_of_lines : "NR;
}' $1 | sort | uniq -c | column -t
