#!/bin/bash

for i in {1..3}; do
    awk '
        BEGIN {
            # Initialize variables
            inside_access_list = 0;
        }

        # Function to check if an IP address belongs to class C
        # On vérifie si le premier octet est entre 192 et 224;
        function isClassC(ip, mask) {
            split(ip, octets, ".");
            return octets[1] >= 192 && octets[1] <= 223 && mask == "255.255.255.0";
        }

        # Check access-list entries
        /access-list 110 permit ip/ {
            source_ip = $5;
            source_mask = $6;
            destination_ip = $7;
            destination_mask = $8;

            print "-------------------"
            
            if (isClassC(source_ip, source_mask) && isClassC(destination_ip, destination_mask)) {
                print "OK - Configuration", FILENAME ".unix", "implements access-list 110 with Class C addresses:", source_ip, source_mask, destination_ip, destination_mask;
            } else {
                print "Not OK - Configuration", FILENAME ".unix", "does not implement access-list 110 with Class C addresses";
            }
            inside_access_list = 1;
        }

        # Check if the access-  list entry ends
        inside_access_list && /!/ {
            inside_access_list = 0;
        }
    ' conf$i.unix
done
