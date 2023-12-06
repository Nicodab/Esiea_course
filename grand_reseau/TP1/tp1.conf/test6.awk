#!/bin/bash
for i in {1..3}; do
    awk '
    BEGIN {
    }
    {
        if($1 == "interface") {
            print "INTERFACE"
        interface_name = $2;
        inside_interface_block = 1;
        }
        if(inside_interface_block && $2 == "trunk" && $3 == "encapsulation") {
            print interface_name
            trunk_encapsulation[interface_name] = $4;
        }
        if(inside_interface_block && $2 == "trunk" && $3 == "native" && $4 == "vlan") {
            native_vlan[interface_name] = $5;
        }
        if(inside_interface_block && $2 == "trunk" && $3 == "allowed" && $4 == "vlan") {
            allowed_vlan[interface_name] = $5;
        }
        # port security
        (inside_interface_block && $2 == "port-security")? security_port[interface_name] = 0: security_port[interface_name] = 1;
        (inside_interface_block && $2 == "mode" && $3 == "access")? mode_access[interface_name] = 0 : mode_access[interface_name] = 1;
        
        if($1 == "!") {
            inside_interface_block = 0;
        }
    }END{
        # Affiche les résultats
        print("voici la liste des interfaces respectant les consignes\n")
        print "Interface Trunk_Encapsulation Native_VLAN Allowed_VLAN Port_Security Mode_Access";
        for (interface in trunk_encapsulation) {
            print interface "\n"
            print "------------------------"
            print "secu: " security_port[interface] ", mode_access: " mode_access[interface]
            if (security_port[interface] != 0 || mode_access[interface] != 0){
                print interface, trunk_encapsulation[interface], native_vlan[interface], allowed_vlan[interface], port_security_status, mode_access_status;
            }
        }
        print"\n"
    }' cat$i.unix
done
