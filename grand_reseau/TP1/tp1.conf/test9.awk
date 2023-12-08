#!/bin/bash

for i in {1..3}; do
    awk '
        BEGIN {
            # Initialize variables
            crypto_map_defined = 0;
            crypto_map_applied = 0;
            inside_crypto_map = 0;
            inside_interface_block = 0;
            current_crypto_map = "";
        }

        # Check crypto map definition
        /crypto map/ {
            crypto_map_defined = 1;
            inside_crypto_map = 1;
            # Save the current crypto map name
            current_crypto_map = $4;
        }

        inside_crypto_map && /set peer/ {
            peer_defined = 1;
        }

        inside_crypto_map && /set transform-set/ {
            transform_set_defined = 1;
        }

        inside_crypto_map && /match address/ {
            access_list_defined = 1;
        }

        inside_crypto_map && /!/ {
            inside_crypto_map = 0;
        }

        # Check crypto map application to FastEthernet interfaces
        /interface FastEthernet/ {
            inside_interface_block = 1;
            # Reset the flag for each interface block
            crypto_map_applied = 0;
            # Reset the current crypto map for each interface block
            current_crypto_map_in_interface = "";
        }

        inside_interface_block && /crypto map/ {
            # Save the crypto map applied to the current interface block
            current_crypto_map_in_interface = $4;
        }

        inside_interface_block && /!/ {
            inside_interface_block = 0;

            if (crypto_map_defined && access_list_defined && transform_set_defined && peer_defined) {
                if (current_crypto_map_in_interface == current_crypto_map) {
                    crypto_map_applied = 1;
                }
            }
        }
        

        END {
            if (crypto_map_defined) {
                if (!crypto_map_applied) {
                    print FILENAME ": Not OK - Crypto map is defined but not applied to FastEthernet interfaces.";
                }
            } else {
                print "Not OK - Crypto map is not defined.";
            }
        }
    ' conf$i.unix
done
