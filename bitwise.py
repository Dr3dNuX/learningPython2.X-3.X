
bin_one = 0b11010101

bin_two = 0b01100


print("bin_ONE={}\nbin_TWO={}\nbin_AND={}"
.format(format(bin_one, '08b'),format(bin_two, '08b'),format(bin_one & bin_two, '08b')))

print("\n\nbin_ONE={}\nbin_TWO={}\nbin__OR={}"
.format(format(bin_one, '08b'),format(bin_two, '08b'),format(bin_one | bin_two, '08b')))

print("\n\nbin_ONE={}\nbin_TWO={}\nbin_XOR={}"
.format(format(bin_one, '08b'),format(bin_two, '08b'),format(bin_one ^ bin_two, '08b')))

print("\n\nbin_ONE= {}\nbin_NOT={}"
.format(bin(bin_one),bin(~bin_one)))


#print("bin_one = {}\nbin_two = {}\nbin_and = {}".format(format(bin_one,'08b')))