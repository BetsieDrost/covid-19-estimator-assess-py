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
    
    #Challenge2: Determine Cases Requiring Hospitalisation by requested time and
    # hospital beds available for COVID-19 patients
    
    allHospitalBeds = impact_data.get("totalHospitalBeds")
    
    ch2ImpactSevereCasesByRequestedTime = \
        int(ch1ImpactInfectionsByRequestedTime * casesRequiringHospitalisation)
        
    ch2SevereImpactSevereCasesByRequestedTime = \
        (ch1SevereImpactInfectionsByRequestedTime * casesRequiringHospitalisation )
        
    ch2BedsAvailableforCovid19 = \
       allHospitalBeds * hospitalBedCapacityAvailable
        
    ch2ImpactOpenHospitalBeds = \
        ch2BedsAvailableforCovid19 - ch2ImpactSevereCasesByRequestedTime
    
    ch2SevereImpactOpenHospitalBeds = \
        (ch2BedsAvailableforCovid19 - ch2SevereImpactSevereCasesByRequestedTime)
    
    # Challenge 3 - Part 1:  Determine cases requiring ventilators and cases requiring ICU
    
    ch3ImpactICUCasesByInfectedTime = \
        (ch1ImpactInfectionsByRequestedTime * casesRequiringICU)
    ch3SevereImpactICUCasesByInfectedTime = \
        (ch1SevereImpactInfectionsByRequestedTime * casesRequiringICU)
    ch3ImpactVentilatorCasesByInfectedTime = \
        (ch1ImpactInfectionsByRequestedTime * casesRequiringVentilators)
    ch3SevereImpactVentilatorCasesByInfectedTime = \
        (ch1SevereImpactInfectionsByRequestedTime * casesRequiringVentilators)
    
    #  Challenge 3 - Part 2 : Determine the DollarsInFlight
    
    avgDailyDollars = impact_data["region"]["avgDailyIncomeInUSD"]
    popEarnAveDollars = impact_data["region"]["avgDailyIncomePopulation"]
    ch3ImpactDollarsInFlight = \
        int(avgDailyDollars * popEarnAveDollars * ch1ImpactInfectionsByRequestedTime)
    ch3SevereImpactDollarsInFlight = \
        int(avgDailyDollars * popEarnAveDollars * ch1ImpactInfectionsByRequestedTime)
    
    #Output 
    output = {
            "data" : impact_data, 
            "impact": {
                    "currentlyInfected" : ch1ImpactCurrentlyInfected,
                    "infectionsByRequestedTime" : ch1ImpactInfectionsByRequestedTime,
                    "severeCasesByRequestedTime" : ch2ImpactSevereCasesByRequestedTime,
                    "hospitalBedsByRequestedTime" : ch2ImpactOpenHospitalBeds,
                    "casesForICUByRequestedTime"  : ch3ImpactICUCasesByInfectedTime,
                    "casesForVentilatorsByRequestedTime" : ch3ImpactVentilatorCasesByInfectedTime,
                    "dollarsInFlight": ch3ImpactDollarsInFlight
                    },
            "severeImpact": {
                    "currentlyInfected" : ch1SevereImpactCurrentlyInfected,
                    "infectionsByRequestedTime" : ch1SevereImpactInfectionsByRequestedTime,
                    "severeCasesByRequestedTime" : ch2SevereImpactSevereCasesByRequestedTime,
                    "hospitalBedsByRequestedTime" : ch2SevereImpactOpenHospitalBeds,
                    "casesForICUByRequestedTime"  : ch3SevereImpactICUCasesByInfectedTime,
                    "casesForVentilatorsByRequestedTime" : ch3SevereImpactVentilatorCasesByInfectedTime,
                    "dollarsInFlight": ch3ImpactDollarsInFlight
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

