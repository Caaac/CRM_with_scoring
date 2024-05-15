def creditProfit(loadnAmount, rate, countMonth):
        # loadnAmount = 20000
        rate = 12
        countMonth = 36
        
        ratePerMonth = (rate / 100 + 1) ** (1 / 12) - 1
        persentPaymentPerMonth = loadnAmount * (ratePerMonth) / (1 - (1 + ratePerMonth) ** (-1 * countMonth))
        totalRevenue = persentPaymentPerMonth * countMonth - loadnAmount
        totalRevenue = int(totalRevenue)
        
        return totalRevenue