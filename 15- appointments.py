import pickle

class Date:
    def __init__(self,day,month,year):
        print('date')
        self.day = day
        self.month = month
        self.year = year

class Time:
    def __init__(self, hour, minute):
        print('time')
        self.hour = hour
        self.minute = minute
        
class Appointment(Date,Time):
    def __init__(self,day,month,year,hour,minute):
        Date.__init__(self,day,month,year)
        Time.__init__(self,hour,minute)
    def __str__(self):
        return self.day+' '+self.month+' '+self.year+' '+self.hour+' '+self.minute

def main():
    try:
        fin = open('appointments.txt','r')
        fout = open('appointments.bin','wb')
    except:
        print("Can't open files")
        sys.exit()

    allAppointments = fin.readlines()

    for currAppointment in allAppointments:
        curr = currAppointment.split()
        currobj = Appointment(curr[0],curr[1],curr[2],curr[3],curr[4])
        pickle.dump(currobj,fout)

    fout.close()

    try:
        fin = open('appointments.bin','rb')
    except:
        print('Error in opening file')
        sys.close

    value = pickle.load(fin)
    while(value):
        print(value)
        try:
            value = pickle.load(fin)
        except EOFError:
            break

    fin.close()

if __name__ == '__main__':
    main()
