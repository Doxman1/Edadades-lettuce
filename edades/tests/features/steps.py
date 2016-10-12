# -*- coding: utf-8 -*-
from lettuce import step, world
from edad import Edades


@step(u'cuando consulto mi mensaje')
def cuando_consulto_mi_mensaje(step):
    pass

@step(u'Dado que ingreso la edad "([^"]*)"')
def dado_que_ingreso_la_edad_group1(step, edades):
    llamar = Edades()
    world.mensaje = llamar.verificar(int(edades))


@step(u'entonces veo, "([^"]*)"')
def entonces_veo_group1(step, mensaje_esperado):
    assert str(world.mensaje) == mensaje_esperado, 'error'

