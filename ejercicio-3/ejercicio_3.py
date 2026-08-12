costoPasaje = float (input ("costo estimado del pasaje:"))
costoAlejamiento = float (input ("costo de alojamiento por noche:"))
cantNoches = float (input ("cantidad de noches que dura el viaje:"))
dineroDisponible = float (input ("dinero disponible:"))

costoTotal = costoPasaje + (costoAlejamiento * cantNoches)
alcanza = dineroDisponible >= costoTotal

print (f"\ncosto total del viaje: $ {costoTotal}")
print (f"dinero disponible: $ {dineroDisponible}")
print (f"¿alcanza el dinero disponible?: {alcanza}")

