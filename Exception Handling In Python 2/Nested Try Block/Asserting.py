def KelvinToFahrenheit(Temperature) :
    assert (Temperature >= 0), "Colder than Obsulates"
    return ((Temperature-273)*1.8) +32
try:
    print(KelvinToFahrenheit(273))
    print(KelvinToFahrenheit(505.78))
    print(KelvinToFahrenheit(-5))
except(AssertionError) :
    print("Can not Convert")