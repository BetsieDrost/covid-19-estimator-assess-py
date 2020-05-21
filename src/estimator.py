#COVID-19 ESTIMATOR - CHALLENGE 1 - BUILDFORSDG2020 ASSESSMENT PHASE
def estimator(data):
    
    impact_data = data
        
    # Assumptions for model
    impactMultiplier = 10
    severeImpactMultiplier = 50
    casesRequiringHospitalisation = 0.15
    casesRequiringICU = 0.05
    casesRequiringVentilators= 0.02
    hospitalBedCapacityAvailable = 0.35
     
    #Challenge 1: Determine Currently Infected and Infections by Requested Time
    daysToElapse = (convert_period_to_days(impact_data.get("periodType"), \
                impact_data.get("timeToElapse")))
    casesReported = impact_data.get("reportedCases")
    multiplierFactor = int(factor_infections_by_requested_time(daysToElapse))
    
    ch1ImpactCurrentlyInfected = casesReported * impactMultiplier  
    ch1SevereImpactCurrentlyInfected = casesReported * severeImpactMultiplier
    ch1ImpactInfectionsByRequestedTime = ch1ImpactCurrentlyInfected * multiplierFactor
    ch1SevereImpactInfectionsByRequestedTime = ch1SevereImpactCurrentlyInfected * multiplierFactor
    
    
    #Output 
    output = {
            "data" : impact_data, 
            "impact": {
                    "currentlyInfected" : ch1ImpactCurrentlyInfected,
                    "infectionsByRequestedTime" : ch1ImpactInfectionsByRequestedTime
                    },
            "severeImpact": {
                    "currentlyInfected" : ch1SevereImpactCurrentlyInfected,
                    "infectionsByRequestedTime" : ch1SevereImpactInfectionsByRequestedTime
                    }
            }
    return output

def factor_infections_by_requested_time(daysToElapse):
    daysInCylcle = daysToElapse
    daysInfectionsDouble = 3 
    powerFactor = (int(daysToElapse / daysInfectionsDouble))
    factor = 2 ** powerFactor
    return factor
    
    
def convert_period_to_days(periodType,timeToElapse):
    if periodType.lower() == "days":
        dayConvertor=1
    elif periodType.lower() == "weeks":
        dayConvertor=7
    elif periodType.lower() == "months":
        dayConvertor=30
    timeInDays = timeToElapse * dayConvertor    
    return timeInDays

