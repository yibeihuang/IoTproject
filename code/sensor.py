def ReadChannel(spi,channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

def ConvertVolts(data,places):
  volts = (data * 5.0) / float(1023)
  volts = round(volts,places)
  return volts