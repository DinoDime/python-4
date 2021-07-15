text = "X-DSPAM-Confidence:    0.8475"
zero = text.find("0")
num = text[zero:]
num = float(num)
print(num)
