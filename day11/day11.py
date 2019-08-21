challenge1_url = 'http://www.pythonchallenge.com/pc/def/0.html'
challenge2_url = 'http://www.pythonchallenge.com/pc/def/%d.html' % pow(2,38)
challenge2_string = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
challenge2_dict = {'m':'k', 'q':'o', 'g':'e'}
tem = challenge2_string
for key in challenge2_dict.keys():
    challenge2_string_translated = challenge2_string_translated.replace(key, challenge2_dict[key])
c2_filtered = ''.join(c for c in challenge2_string if c in challenge2_dict.keys())
temp = c2_filtered
for key in challenge2_dict.keys():
    temp = temp.replace(key, challenge2_dict[key])
print(challenge2_string_translated)