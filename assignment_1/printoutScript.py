# Your function for calculating payment goes here
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

# Your function for calculating remaining balance goes here
def remainingLoanBal(principal, annual_interest_rate, duration, number_of_payments):
    # Calculate the montly interest rate
    monthlyIntRate = (annual_interest_rate/100)/12
    # Calculate the monthly duration
    monthlyDuration = duration*12

    return (principal*(pow(1 + monthlyIntRate,monthlyDuration) - pow(1 + monthlyIntRate, number_of_payments))
                /(pow(1 + monthlyIntRate, monthlyDuration) - 1))


# Your main program goes here
principle=float(input("Enter loan amount: "))
annual_interest_rate=float(input("Enter annual interest rate (percent): "))
duration=int(input("Enter loan duration in years: "))

monthlyPay = monthlyPayment(principle, annual_interest_rate, duration)
print('LOAN AMOUNT:', float(principle),
      'INTEREST RATE (PERCENT):', annual_interest_rate)
print('DURATION (YEARS):', duration,
      'MONTHLY PAYMENT:', int(monthlyPay))

for year in range(1, duration + 1):
    remainingBalance = remainingLoanBal(principle, annual_interest_rate, duration, year*12)
    print('YEAR:', year,
          'BALANCE:', int(remainingBalance),
          'TOTAL PAYMENT:', int(monthlyPay*year*12))
    
