def monthlyPayment(principal, annualIntRate, duration):
    # Obtain the monthly interest rate
    monthlyRate = (annualIntRate/100)/12
    months = 12*duration
    # If the monthly interest rate is zero
    if monthlyRate == 0:
        return principal/(duration*12)
    else:
        return ( principal*(monthlyRate*pow(1 + monthlyRate, months))
                    /(pow(1 + monthlyRate, months) - 1) )
