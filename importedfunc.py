import csv
import webbrowser



#web browser hyper link
def webhyper(event):
	webbrowser.open_new(r"http://www.python.org")

def writedata(a,b,c,d,e):
    '''function for writing data to csv'''
    
    name = a
    domain = b
    if c:
    	gen = "Male"
    else:
    	gen = "Female"
    if e:
    	inte = 'Yes'
    else:
    	inte = 'No'
    
    with open("data_file.csv", mode="a") as csvfile:
        w = csv.writer(csvfile, delimiter=',')
    	w.writerow([name, domain, gen, inte])
    	
            
	
    	
    		
       
	
