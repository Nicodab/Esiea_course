awk '
BEGIN {
    interface_name = "";
    ip_address = "";
    found_access_group = 0;
    inside_interface_block = 0;
    file = FILENAME;
    line = FNR
}

/interface/ {
    interface_name = $2;
    inside_interface_block = 1;
    print "interface_name: " interface_name;
}

inside_interface_block && /ip address/ {
    ip_address = $3;
}

inside_interface_block && /!/ {
    if (ip_address !~ /^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$/ && found_access_group == 0) {
        print "Not Ok"
    }
    interface_name = "";
    ip_address = "";
    found_access_group = 0;
    inside_interface_block = 0;
}

inside_interface_block && /ip access-group/ {
    found_access_group = 1;
    print "Ok"
}
' router.unix
