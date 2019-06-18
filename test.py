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

n = jpfund.Nikko("944432", "G33")
print(n)
print(n.get())
nikko_list = jpfund.Nikko.get_list()
print(nikko_list[0])
print(nikko_list[-1])
print(nikko_list[-1].get())
