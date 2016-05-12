import socket
import threading
def calculator(name,sock):
    
    
    ServerLoadRecords={}
    global ServerLoadRecords
    def Server_read(ServerName, n, endTime):
        
        
        if(n==24):            
            startTime = endTime-(24*60*60)
            calcWindow =60*60
        elif(n==60):
            startTime = endTime-(60*60)
            calcWindow = 60
        
        tempList = ServerLoadRecords[ServerName]
        ram=0
        cpu=0
        listToReturn = []
        count=0
        for currentTuple in tempList: 
            if currentTuple[0]<endTime and currentTuple[0]>=startTime:
                   if (currentTuple[0] < (startTime + calcWindow)):
                    
                    
                        ram+= currentTuple[1]
                        cpu+=currentTuple[2]
                        count+=1
                   else: 
                        listToReturn.append((cpu/count,ram/count))
                        count=0
                        cpu=0
                        ram=0
                        startTime+=calWindow
        if(count>0):
            listToReturn.append((cpu/count,ram/count))
            
        return listToReturn
    
    
    def Server_write():
        load=data.split()
        d1=tuple()
        server=d1[0]
        if not ServerLoadRecords[server]:
            ServerLoadRecords[server]=list()
        ServerLoadRecords[server].append((long(d1[1]),float(d1[2]),float(d[3])))
        return 'success'
    
    while True:
        outputstring=''
        
        while True:            
            data=sock.recv(1)
            if ((data)== b'\n'):
                break
            outputstring+=data.decode()
        
        if data:            
            try:
                columns = outputstring.split()            
                if(columns[0]=='read') :
                    clientResponse = Server_Read(columns[1],int(columns[2]))
                    
                if(columns[0]=='write'):
                    clientResponse = Server_Write(columns[1],columns[2],columns[3],columns[4])
                
                sock.send(str(clientResponse).encode())
            except Exception as e:
               print( 'exception', str(e))
           
        
    
#sock.close()

def main():
    host='127.0.0.1'
    port=5000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s=socket.socket()
    s.bind((host,port))
    s.listen(5) 
    
    print ("server started")
    while True:
        c,addr=s.accept()
        print('client connected to ip:<' + str(addr)+'>')
        t=threading.Thread(target=calculator,args=('retrThread',c))
        t.start()
    s.close()

if __name__ == '__main__' :
    main()

    
            
   
