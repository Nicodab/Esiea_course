awk '
BEGIN {
    found = 0;
}
{
    if ($1 == "snmp-server" && $4 == "RO") {
        print "config ok"
        found = 1;
    }
}
END {
    if (!found) {
        print "config pas ok"
    }
}' router.unix
