#COVID-19 ESTIMATOR - CHALLENGE 1 - BUILDFORSDG2020 ASSESSMENT PHASE



def model_inputs():
    reviewRegion= region_input()
    x = reviewRegion.get("regionName")
    currentlyInfected = int(input(f"How many Covid-19 cases are currently reported for {x}? "))
    periodTypeInput=convert_period_to_days()
    typePeriod=periodTypeInput[0]
    dayConvertor=periodTypeInput[1]
    typePeriodToElapse=int(input(f" For how many {typePeriod} elapsed would you like the estimation to be done? "))
    convertedDaysToElapse = typePeriodToElapse * dayConvertor
    regionHospitalBeds = input(f" What is the total number of hospital beds in {x}? ")
    multiplierFactor = infections_by_requested_time(convertedDaysToElapse)
    fixed_data = {
                   "regionName:": x,
                   "periodType" : typePeriod,
                   "timeToElapse" : typePeriodToElapse,
                   "daysToElapse" : convertedDaysToElapse,
                   "totalHospitalBeds" : regionHospitalBeds,
                   "reportedCases" : currentlyInfected,
                   "factorForInfections" : multiplierFactor,
                   "impactMultiplier" : 10,
                   "severeImpactMultiplier" : 50,
                   "casesRequiringHospitalisation" : 0.15,
                   "casesRequiringVentilators": 0.05,
                   "casesRequiringVentilators": 0.02,
                   "hopitalBedCapacityAvailable": 0.35,
                }
    return fixed_data


def region_input():
    regionName = input("Enter the region: ")
    regionAveAge = float(input(f"Average age of the population of {regionName}? "))
    regionPopulation = int(input(f"What is the population of {regionName}? "))
    regionAveDailyIncome = int(input(f"What is the average daily income per person in USD for {regionName}? "))
    regionAveDailyIncomePercentPopulation =  float(input(f"What percentage (enter as decimal) of the population  of {regionName} earns the average daily income of USD {regionAveDailyIncome}? "))
    region = {  
               "regionName" : regionName,
               "avgAge": regionAveAge,
               "avgDailyIncomeUSD": regionAveDailyIncome,
               "avgDailyIncomePopulation": regionAveDailyIncomePercentPopulation, 
               "population": regionPopulation
              }
    return region   


def infections_by_requested_time(daysToElapse):
    daysInCylcle = daysToElapse
    daysInfectionsDouble = 3 
    powerFactor = (int(daysToElapse / daysInfectionsDouble))
    factor = 2 ** powerFactor
    return factor
    

    
def convert_period_to_days():
    periodTypes = ["days","months","weeks"]
    test=False
    while test == False:
        periodType = (input(f"Select the period type you will use: {periodTypes[0:3]}")).lower()
        if periodType == "days":
            dayConvertor=1
            test=True
        elif periodType == "weeks":
            dayConvertor=7
            test=True
        elif periodType == "months":
            dayConvertor=30
            test=True
        else: print("Invalid input")
    return periodType, dayConvertor


  
def impact_estimator(data):
    impact_data=data
    multiplier = impact_data.get("impactMultiplier")
    factor = impact_data.get("factorForInfections")
    currentInfections = impact_data.get("reportedCases")
    estimateInfectionsByRequestedTime = currentInfections * factor * multiplier
    impact = {
                "infectionsByRequestedTime" : estimateInfectionsByRequestedTime
             }
    return impact


def severe_impact_estimator(data):
    severe_impact_data=data
    multiplier = severe_impact_data.get("severeImpactMultiplier")
    factor = severe_impact_data.get("factorForInfections")
    currentInfections = severe_impact_data.get("reportedCases")
    estimateSevereInfectionsByRequestedTime = currentInfections * factor * multiplier
    severeImpact = {
                "infectionsByRequestedTime" : estimateSevereInfectionsByRequestedTime
             }
    return severeImpact
    
    
    

myResult = model_inputs()
print(f"This is my input data: {myResult}")
myImpactResult = impact_estimator(myResult)
print(f"This is my Impact output: {myImpactResult}")
mySevereImpactResult = severe_impact_estimator(myResult)
print(f"This is my Severe Impact output: {mySevereImpactResult}")
