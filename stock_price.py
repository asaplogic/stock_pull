import urllib.request
import urllib.parse
import string


#name of stock to pull
stock_to_pull= "AAPL"
#function pull data of 'stock' from URL

def pull_data(stock):
    file_line = stock+ '.txt'
    save_file = open(file_line, 'w')
    
    urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1m/csv'
    sourceCode = urllib.request.urlopen(urlToVisit)
    split_source = sourceCode.split('\n')
    split_source = split_source[18:] # cut off the header

    for i, each_line in enumerate(split_source):
        if each_line:
            date,close_price,high,low,open_price,volume = each_line.split(',')
            line_to_write = str(i)+ ','+ high +'\n'
            save_file.write(line_to_write)
            #print line_to_write, len(line_to_write)
 
pull_data(stock_to_pull)