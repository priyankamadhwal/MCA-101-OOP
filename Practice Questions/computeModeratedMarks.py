def computeModeratedMarks(file1, file2, addpercent):
    try:
        fin = open(file1,'r')
        fout = open(file2,'w')
    except IOError:
        print('Input/Output error')
        sys.exit()

    line = fin.readline()
    while line != '':
        line = line.split(',')
        try:
            rollno = int(line[0])
            name = line[1]
            marks = float(line[2])
        except IndexError:
            print('Index error')
            sys.exit()
        except ValueError:
            print('Unsuccessful conversion to int')
            sys.exit()

        maxmarks = 100
        marks = marks + (addpercent * maxmarks / 100)

        if marks > 100:
            marks = 100

        line = str(rollno)+','+name+','+str(marks)+'\n'
        fout.write(line)
        
        line = fin.readline()
        
    fin.close()
    fout.close()
        
