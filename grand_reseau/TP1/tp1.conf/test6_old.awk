awk '
BEGIN {
    # Initialize variables as arrays
    split("", trunk_encapsulation);
    split("", native_vlan);
    split("", allowed_vlan);
    split("", port_security);
    split("", mode_access);
}

/interface/ {
    interface_name = $2;
    inside_interface_block = 1;
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

inside_interface_block && /port-security/ {
    port_security[interface_name] = "port-security";
}

inside_interface_block && /mode access/ {
    mode_access[interface_name] = "mode access";
}

/!/ {
    inside_interface_block = 0;
}

END {
    # Affiche les résultats
    print "Interface Trunk_Encapsulation Native_VLAN Allowed_VLAN Port_Security Mode_Access";
    for (interface in trunk_encapsulation) {
        port_security_status = (port_security[interface] == "") ? "Not Implemented" : "Implemented";
        mode_access_status = (mode_access[interface] == "") ? "Not Implemented" : "Implemented";
        print interface, trunk_encapsulation[interface], native_vlan[interface], allowed_vlan[interface], port_security_status, mode_access_status;
    }
}
' cat1.unix cat2.unix cat3.unix
