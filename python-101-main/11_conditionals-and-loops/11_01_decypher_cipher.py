# Decipher the message within the `secret` variable.
# Pick out only the alphabetic characters, not the numbers.

secret = ("2349h30023388281e3299371l1l3094842o0 333s6552w665e5e680t66351354651352326565i233/////e"
          "0565 6i5654181+2123 4666457d+-*0454o70053 6246t66h470453i2254s2355164 98909878f8//*o21 651"
          "2228+9u8*/+2435467778s98*6)883")
solution = ""
for i in secret:
    if i.isalpha() or i == " ":
        solution += i
print(solution)
