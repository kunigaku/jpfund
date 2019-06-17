import jpfund
import sys

print(sys.version)

m = jpfund.Morningstar("2017092908", "Rakuten VTI")
print(m)
print(m.get())

e = jpfund.EMaxis("250874", "eMaxis Nikkei 225 Index")
print(e)
print(e.get())

emaxis_list = jpfund.EMaxis.get_list()
print(emaxis_list[0])
print(emaxis_list[0].get())
