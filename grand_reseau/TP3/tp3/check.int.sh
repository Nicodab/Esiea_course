#!/usr/bin/awk -f

BEGIN {
    inside_interface_block = 0;
}

/interface/ {
    if (inside_interface_block) {
        if (!found_access_group && ip_address !~ /^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$/) {
            print "./" FILENAME " interface " interface_name " missing ip access-group";
        }
    }

    interface_name = $2;
    ip_address = "";
    found_access_group = 0;
    inside_interface_block = 1;
    next;  # Passe à la ligne suivante sans exécuter les instructions restantes
}

inside_interface_block && /ip address/ {
    ip_address = $3;
    next;
}

inside_interface_block && /!/ {
    if (!found_access_group && ip_address !~ /^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$/) {
        print "./" FILENAME " interface " interface_name " missing ip access-group";
    }
    inside_interface_block = 0;
    next;
}

inside_interface_block && /ip access-group/ {
    found_access_group = 1;
    next;
}

END {
    if (inside_interface_block && !found_access_group && ip_address !~ /^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$/) {
        print "./" FILENAME " interface " interface_name " missing ip access-group";
    }
}
