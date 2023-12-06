#!/bin/bash

for i in {1..3}; do
    awk '
        BEGIN {
            # Initialize variables as arrays
            split("", port_security);
            split("", mode_access);
            split("", trunk_encapsulation);
            split("", native_vlan);
            split("", allowed_vlan);
        }

        /interface/ {
            interface_name = $2;
            inside_interface_block = 1;
        }

        inside_interface_block && /port-security/ {
            port_security[interface_name] = "port-security";
        }

        inside_interface_block && /mode access/ {
            mode_access[interface_name] = "mode access";
        }

        inside_interface_block && /encapsulation/ {
            trunk_encapsulation[interface_name] = $4;
        }

        inside_interface_block && /native vlan/ {
            native_vlan[interface_name] = $5;
        }

        inside_interface_block && /allowed vlan/ {
            allowed_vlan[interface_name] = $5;
        }

        /!/ {
            inside_interface_block = 0;
        }

        END {
            print FILENAME;
            # Affiche les résultats
            print "Interface Port_Security Mode_Access Trunk_Encapsulation Native_VLAN Allowed_VLAN";
            for (interface in port_security) {
                if (mode_access[interface] != "") {
                    trunk_encapsulation_status = (trunk_encapsulation[interface] == "") ? "Not Implemented" : "Implemented";
                    native_vlan_status = (native_vlan[interface] == "") ? "Not Implemented" : "Implemented";
                    allowed_vlan_status = (allowed_vlan[interface] == "") ? "Not Implemented" : "Implemented";
                    print interface, port_security[interface], mode_access[interface], trunk_encapsulation_status, native_vlan_status, allowed_vlan_status;
                }
            }
        }
    ' cat$i.unix
done
