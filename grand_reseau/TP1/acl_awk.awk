awk '
{
    if ($1 == "access-list") acl_def[$2] = $0;

    if ($1 == "ip"  && $2 == "access-list" && $3 == "extended") acl_def[$4] = $0;

    if ($1 == "ip" && $2 == "access-group") acl_ref[$3] = $0;
    if ($1 == "access-class") acl_ref[$2] = $0;
    if ($1 == "snmp-server") acl_ref[$3] = $0;
    
}
END {
    for (id in acl_def) {
        if (!(id in acl_ref)) print acl_def[id], "def pas dans ref";
    }
    for (id in acl_ref) {
        if (!(id in acl_def)) print acl_ref[id], "ref pas dans def";
    }
}' router_no_comment.unix
