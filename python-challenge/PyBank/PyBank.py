import csv, os

previousRow = None 
currentRow = None
greatestGain = {"value": 0, "date": ""}
greatestLoss = {"value": 0, "date": ""}
totalMonths = 0
totalProfits = 0
totalChange = 0


with open('Resources/budget_data.csv', 'r') as f:
    next(f)
    
    for row in f:                   
        totalMonths += 1            
        row = row.split(',')        
        totalProfits += int(row[1]) 
        if previousRow is None:    
            previousRow = row      
            continue                
                                         
        
        currentRow = row            
        currentDelta = int(currentRow[1]) - int(previousRow[1])         
        totalChange += currentDelta                                    
        
        if currentDelta < 0 and currentDelta < greatestLoss["value"]:   
            greatestLoss["value"] = currentDelta                       
            greatestLoss["date"] = currentRow[0]                        
        elif currentDelta > 0 and currentDelta > greatestGain["value"]: 
            greatestGain["value"] = currentDelta                        
            greatestGain["date"] = currentRow[0]                        
            
        previousRow = currentRow                                       
    
    avrchange = totalChange/(totalMonths-1)

    
Financial_Analysis = (
    f"\nFinancial Analysis\n"
    f"------------------------------------------------\n"
    f"Total Months: {totalMonths}\n"
    f"Total Profits: {totalProfits:,}\n"
    f"Total Profits: {avrchange:,.2f}\n"
    f"Greatest Increase in Profits: {greatestGain['date']} {greatestGain['value']:,}\n"
    f"Greatest Decrease in Profits: {greatestLoss['date']} {greatestLoss['value']:,}\n"
    f"------------------------------------------------\n")

print(Financial_Analysis)

