from pyDatalog import pyDatalog

pyDatalog.create_terms('W, P, parcel, price_for')
for grams in [200, 500, 501, 1000, 1001, 1500, 1501]:
    +parcel(grams)

price_for(W, 4) <= parcel(W) & (W <= 500)
price_for(W, 7) <= parcel(W) & (W > 500) & (W <= 1000)
price_for(W, P) <= (parcel(W) & (W > 1000)
                    & (P == 7 + (W - 1000 + 499) // 500 * 2))

print(sorted(price_for(W, P).data))
