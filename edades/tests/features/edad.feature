Feature: Devuelve mensaje por edad
	Como usuario del sistema edades
	quiero ingresar una edad y me regresa un mensaje según mi edad
	para tener siempre presente mis años.

	Scenario: Con edad menor a cero
	Dado que ingreso la edad "-1"
	cuando consulto mi mensaje
	entonces veo, "no existes"

	Scenario: Con edad menor a 13 y mayor a cero
	Dado que ingreso la edad "8"
	cuando consulto mi mensaje
	entonces veo, "eres nino"

	Scenario: Con edad menor a 18 y mayor a 13
	Dado que ingreso la edad "15"
	cuando consulto mi mensaje
	entonces veo, "eres adolescente"

	Scenario: Con edad menor a 65 y mayor a 18
	Dado que ingreso la edad "50"
	cuando consulto mi mensaje
	entonces veo, "eres adulto"

	Scenario: Con edad menor a 120 y mayor a 65
	Dado que ingreso la edad "119"
	cuando consulto mi mensaje
	entonces veo, "eres adulto mayor"

	Scenario: Con edad mayor a 120
	Dado que ingreso la edad "121"
	cuando consulto mi mensaje
	entonces veo, "eres mumm-ra"