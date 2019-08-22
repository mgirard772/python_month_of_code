import re

JPEG_SOF = b'\xFF\xD8\xFF\xE0'
JPEG_EOF = b'\xFF\xD9'

if __name__ == "__main__":
    #Read the raw file
    raw_file = open('challenge16_file.raw', 'rb')
    data = raw_file.read()
    raw_file.close()

    #Get locations of SOF and EOF for each JPEG
    SOF_list = [match.start() for match in re.finditer(re.escape(JPEG_SOF),data)]
    EOF_list = [match.start() for match in re.finditer(re.escape(JPEG_EOF),data)]

    #Create a list of SOF and EOF pairs, ensuring that EOF index is greater than SOF
    pairs = []
    while(SOF_list.__len__() > 0):
        start = SOF_list.pop(0)
        end = None
        while(EOF_list.__len__() > 0):
            end_temp = EOF_list.pop(0)
            if(end_temp > start):
                end = end_temp
                break
        if(end):
            pairs.append((start,end))

    #Save each JPEG using the SOF and EOF pairs
    for start, end in pairs:
        subdata = data[start:end+2]
        carve_filename="Carve1_"+str(start)+"_"+str(end)+".jpg"
        carve_obj=open(carve_filename,'wb')
        carve_obj.write(subdata)
        carve_obj.close()
        print("Found an image and carving it to %s" % (carve_filename))
