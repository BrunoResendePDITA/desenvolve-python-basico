urls = ["www.google.com", 
       "www.gmail.com", 
       "www.github.com", 
       "www.reddit.com", 
       "www.yahoo.com"]
dominios = []

for i in urls:
    dominios.append(i[4:-4])

print('Domínios:', dominios)
