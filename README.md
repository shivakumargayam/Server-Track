# Server-Track
Server track implementaion using Python3.3
*In real world operation this server track opration will be pretty big so for simplicity sake i am taking below assumtions.
*For simplicity sake I am assuming that Client is sending the operation name that he would like to perform(Read/Write),server name,Timestamp,CPU and RAM.
*Example input for write operation is 'write shiva 1000 1.0 1.0'i.e opreration name,server name,current timestamp since epoch,cpu and ram.
*Example input for Read operation is 'read shiva 60(or)24 3500'i.e opration name, server name,60 minuts or 24 hours,and current timestamp.
*server will read the inputs and according to the input it will perform either read or write operation.
*In this program i am assuming that data is storing in dictionary. But, in real world it will be a No sql.And the read and write operations will exposed as REST API.
*The current implementation does not persist the data during server failures.for example if the server program crashes all the memory will delete.
*The memory management algorithm to limit maximum memory per server stored is not implemented. It could be resticted to number of samples per minute*60*24.

STEPS TO RUN THIS PROGRAM
1.You have to run server and client programs in differnt command windows.
2.First run server program by running 'Python Api_server.py' command.
3.Then run client program by running 'Python Client.py' command.
4.Enter the input in client program.
5.you will get the result from the serer.


NOTE: I implemented these programs in Python 3.3. If you have Python 2.x in your machine this program will not work. It will work only in python 3.x version.

