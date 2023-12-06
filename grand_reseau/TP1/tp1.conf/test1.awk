awk '
BEGIN{
    found = 0;
}
{
    if ($2 == "password-encryption"){
        print "Configured"
        found = 1;
    }
}END {
    if (!found) {
        print "Not configured"
    }
}' router.unix