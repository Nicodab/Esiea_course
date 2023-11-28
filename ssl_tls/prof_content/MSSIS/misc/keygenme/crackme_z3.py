import z3


CHECKSUM_PART_1_BYTE = 0x10
CHECKSUM_PART_1_INT = 0x687E7076

alphas = z3.BitVecs('alpha1 alpha2 alpha3 alpha4', 32)
digits = z3.BitVecs('digit1 digit2 digit3 digit4', 32)


solver = z3.Solver()

# only A-Z
for alpha in alphas:
    solver.add(z3.And(alpha >= ord('A'), alpha <= ord('Z')))
# end for

# only 0-9
for digit in digits:
    solver.add(z3.And(digit >= ord('0'), digit <= ord('9')))
# end for

# BYTES constraint
solver.add(CHECKSUM_PART_1_BYTE == alphas[0] ^ alphas[1] ^ alphas[2] ^ alphas[3] ^ digits[0] ^ digits[1] ^ digits[2] ^ digits[3])

# INTS constraint
alphas_v = (alphas[0] << 24) | (alphas[1] << 16) | (alphas[2] << 8) | (alphas[3])
digits_v = (digits[0] << 24) | (digits[1] << 16) | (digits[2] << 8) | (digits[3])
solver.add(CHECKSUM_PART_1_INT == (alphas_v ^ digits_v))


def get_models(solver):
    while solver.check() == z3.sat:
        m = solver.model()
        yield m
        solver.add(z3.Or([sym() != m[sym] for sym in m.decls()]))
    # end while
# end get_models



for m in get_models(solver):    
    serial = ""
    for alpha in alphas:
        serial += chr(int(str(m[alpha])))
    # end for
    serial += "-"
    for digit in digits:
        serial += chr(int(str(m[digit])))
    # end for
    
    print(serial)
# end if


