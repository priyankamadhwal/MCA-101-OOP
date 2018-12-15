def copyFileContents(file):
    newfile = 'copyfile.txt'
    try:
        fin = open(file,'r')
        fout = open(newfile,'w')
        print(fin.read())
        print()
        print()
        fin.seek(0)
        lines = fin.readlines()
        fout.writelines(lines)
        fin.close()
        fout.close()
        fin = open(newfile,'r')
        print(fin.read())
        fin.close()
        
    except:
        print('Something went wrong')
        
