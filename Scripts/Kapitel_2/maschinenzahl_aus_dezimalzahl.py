import math

def machine_number_0m(val, exp_bits, man_bits):
    if val == 0:
        sign = "0"
        exponent = "0" * exp_bits
        mantissa = "0" * man_bits
        result = f"|{sign}|{exponent}|{mantissa}|"
        return sign, exponent, mantissa, result

    sign = "1" if val < 0 else "0"
    bias = (1 << (exp_bits - 1)) - 1

    m, e = math.frexp(abs(val))

    E = e + bias
    if E <= 0 or E >= (1 << exp_bits) - 1:
        raise ValueError("Underflow/Overflow for this format (no subnormals/inf handled).")

    exponent = format(E, f"0{exp_bits}b")

    frac = m
    bits = []
    for _ in range(man_bits):
        frac *= 2
        if frac >= 1:
            bits.append("1")
            frac -= 1
        else:
            bits.append("0")

    mantissa = "".join(bits)

    result = (
        f"Vorzeichen: {sign}\n"
        f"Exponent (biased): {exponent}\n"
        f"Mantisse: 0.{mantissa}\n"
        f"|{sign}|{exponent}|{mantissa}|"
    )
    return sign, exponent, mantissa, result

# ----------------------------------------------------------

value = 2.0
e_bits = 4
m_bits = 7

print(machine_number_0m(value, e_bits, m_bits)[3])
