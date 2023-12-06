awk '
BEGIN {
}
{
    if ($1 == "line") {
        LINE[$0] = FNR;
        this = $0;
    }
    if ($1 == "access-class" && $3 == "in") {
        LINE_in[this] = $0;
    }
    if ($1 == "access-class" && $3 == "out") {
        LINE_out[this] = $0;
    }
}END{
    for (id in LINE){
        if (! (id in LINE_in)) {
            print id "line not access class in"
        }
        if (! (id in LINE_out)) {
            print id "line not access class out"
        }
    }
}' router.unix
