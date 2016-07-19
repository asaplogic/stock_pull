import requests

#using request library

#name of stock to pull
stock_to_pull= "AAPL"
#function pull data of 'stock' from URL

def pull_data(stock):
    file_line = stock+ '.txt'
    save_file = open(file_line, 'w')
    
    urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1m/csv'
    split_code = requests.get(urlToVisit).text #stores the text into variable
    split_code = split_code.splitlines()[18:] #cuts off first 18 lines and returns the rest


    #checks to see if working        
    print("Pulling:"+stock_to_pull+ "\n"+urlToVisit)

    for i, each_line in enumerate(split_code):
        if each_line:
            date, close_price,high,low,open_price,volume = each_line.split(',')
            line_to_write = str(i) + ','+high + '\n'

            #save_file.write(line_to_write)
    
    print(split_code)


        
pull_data(stock_to_pull) 