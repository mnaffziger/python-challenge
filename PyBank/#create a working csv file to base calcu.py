  #create a working csv file to base calculations on without potential data corruption of original
    with open(pybank_out_path,'w') as pybank_out:
        pybank_write = csv.writer(pybank_out)
        
        report={"MONTHS":"months",
                "TOTAL":"total",
                "AVE_CHANGE":"ave_change",
                "MAX_DATE":"max_date",
                "MAX_PROFIT":"max_profit",
                "MIN_DATE":"min_date",
                "MIN_PROFIT":"min_profit"}
        
        
        
        headers.append('Change') #add new header
        pybank_write.writerow(headers) #write headers to new csv file
       
    
        
       

        #Start working/analyzing original csv file
        for row in pybank_in:
        
       
            
        
        report["MONTHS"]=months
        report["TOTAL"]=total
        print(f"Total = {total}")
    
        print(f"Total Months: {months}")
        
        print(report)
    
    
