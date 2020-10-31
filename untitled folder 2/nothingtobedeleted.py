  sh = input("enter hour: ")
  sr = input("enter rate: ")
  fh = float(sh)
  fr = float(sr)
  #print(fh;fr)
  if fh > 40:
            # print("overtime")
            reg = fr * fh
            otp = (fh - 40.0) * (fr * 0.5)
            # print(reg;opt)
            xp = reg + otp
          else:
              #  print("regular")
              xp = fr * fh
              # print("pay";xp)
