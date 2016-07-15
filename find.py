text = "X-DSPAM-Confidence:    0.8475";
pos = text.find("0")
content = text[pos:]
content1 = float(content)
print(content1)
