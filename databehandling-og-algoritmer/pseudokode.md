## Eksempel: Penger tjent på Spotify

> En algoritme som  regner ut hvor mye penger vi tjener på Spotify

### Pseudokode i *naturlig språk* 

```pseudo
Hent inn antall streams
Hvis antall streams er større enn 30 000 000:
    Returner antall streams gange 70% (0.7)
Ellers hvis antall streams er større enn 1 400 000:
    Returner antall streams gange 40% (0.4)
Ellers:
    Returner 0
```

### Pseudokode som følger UDIR sin standard

```pseudo
SET antall_streams to READ "Hvor mange streams?"
IF antall_streams GREATER THAN 
```

### Pythonkode 

```python
# Oppgave: Skriv algoritmen i vanlig python-kode:
antall_streams = int(input("Hvor mange streams"))
if antall_streams > 30 000 000:
    print(antall_streams * 0.7)
elif antall_streams >1 400 000:
    print(antall_streams * 0.4)
else:
    print(0)
```