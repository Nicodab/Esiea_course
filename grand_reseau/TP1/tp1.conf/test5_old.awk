awk '
BEGIN {
    # Initialize variables as arrays
    split("", defined_acls);
    split("", applied_acls);
}

/ip access-list extended/ || /access-list/ {
    # ACLs définies
    acl_name = $3;
    defined_acls[acl_name] = 1;
}

/access-class/ || /access-group/ || /snmp-server/ {
    # ACLs appliquées
    acl_name = $3;
    applied_acls[acl_name] = 1;
}

END {
    # Affiche les ACLs définies mais non appliquées
    print "\nACL defined but not applied";
    for (acl in defined_acls) {
        if (!(acl in applied_acls)) {
            print acl;
        }
    }

    # Affiche les ACLs appliquées mais non définies
    print "\nACL applied but not defined";
    for (acl in applied_acls) {
        if (!(acl in defined_acls)) {
            print acl;
        }
    }
}
' router.unix