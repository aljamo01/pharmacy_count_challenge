import sys


def count_sum (f):
    file = open(f)
    dic = {}
    first_line= True
    for line in file:
        if not first_line:

            l = line.rstrip().split(",")
            drug_name= l[-2]
            drug_cost= int(l[-1])
            prescriber = l[-4]+','+l[-3]
            if drug_name in dic.keys():

                count = set()
                if prescriber not in dic[drug_name]['count']:
                    dic[drug_name]['perscribers'] += 1
                    dic[drug_name]['count'].add(prescriber)

                dic[drug_name]['sum'] += drug_cost
            else:
                dic[drug_name] = {'perscribers':1, 'count':set([prescriber]), 'sum':drug_cost}
        else:
            first_line =False
    return dic


def create_outline(f):
    outline = [["drug_name","num_prescriber","total_cost"]]
    for i in f:
        outline.append([i,f[i]['perscribers'],f[i]['sum']])
    return outline

def lines_to_string(f):
    stringlines = []
    for i in f:
        text = str(i[0])+ ',' + str(i[1]) + ',' + str(i[2])
        stringlines.append(text)
    return stringlines

def write_line(f, l):
    with open(f, "w") as outfile:
        linenum= 0
        numlines= len(l)
        for line in l:
            linenum +=1
            outfile.write(line)
            if linenum < numlines:
                outfile.write('\n')

if __name__ == '__main__':
    infile= sys.argv[1]
    outfile = sys.argv[2]
    raw = count_sum(infile)
    outlines= create_outline(raw)
    outstrings= lines_to_string(outlines)
    write_line(outfile,outstrings)

#print('Number of arguments:', len(sys.argv), 'arguments.')
#print('Argument List:', str(sys.argv))