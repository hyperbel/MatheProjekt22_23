import re

def extract_terms(equation):
    terms = re.findall(r"[+-]?\d*x?\^?\d*", equation)
    return terms

equation = "3x^4-4x^3+4x-5"
print(extract_terms(equation))
