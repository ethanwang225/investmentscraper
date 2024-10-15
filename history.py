import yfinance as yf

# Fetch historical data for eqix
eqix = yf.Ticker("EQIX")
history = eqix.history(period="3mo")
history.to_csv("eqix_3m.csv")
eqox_stats=eqix.info


sba=yf.Ticker("SBAC")
print(sba.info)



real_estate=yf.Sector('real-estate')
real_estate = yf.Industry('real-estate')




# print(eqix.analyst_price_targets)
# print(eqix.earnings_estimate)
# print(eqix.revenue_estimate)
# print(eqix.earnings_history)
# print(eqix.eps_trend)
# print(eqix.eps_revisions)
# print(eqix.growth_estimates)