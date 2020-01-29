def remainingLoanBal(principal, annual_interest_rate, duration, number_of_payments):
    # Calculate the montly interest rate
    monthlyIntRate = (annual_interest_rate/100)/12
    # Calculate the monthly duration
    monthlyDuration = duration*12

    return (principal*(pow(1 + monthlyIntRate,monthlyDuration) - pow(1 + monthlyIntRate, number_of_payments))
                /(pow(1 + monthlyIntRate, monthlyDuration) - 1))
