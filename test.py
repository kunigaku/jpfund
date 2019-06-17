import jpfund
import sys

print(sys.version)

m = jpfund.Morningstar("2017092908", "Rakuten VTI")
print(m)
print(m.get())
