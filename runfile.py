import code as x 

x.create("sameer",30)

x.create("raj",65,4550) 

x.read("sameer")

x.read("raj")

x.create("sameer",60)

x.modify("sameer",65)

x.delete("sameer")

t1=Thread(target=(create or read or delete),args=(key_name,value,timeout))
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout))
t2.start()
t2.sleep()
