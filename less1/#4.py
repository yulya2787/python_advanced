#4

'''4) Реализовать функцию bank, которая приннимает следующие
аргументы: сумма депозита, кол-во лет, и процент. Результатом
выполнения должна быть сумма по истечению депозита'''

def bank(amount, years, percent):
    percent = percent / 100
    month_pay = (amount * percent * (1 + percent) ** years) / (12 * ((1 + percent) ** years - 1))
    return month_pay * years * 12


amount = int(input('how much money do you want to put into bank? '))
years = int(input('for how many years? '))
percent = int(input('put the percent value '))

bank_result = bank(amount, years, percent)
print(bank_result)
