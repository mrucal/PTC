# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 17:11:55 2017

@author: Mario
"""


import obtener_valores_api as ova
import obtener_valores_xml as ovx
import generar_html as gh
import guardar_datos as gd
import obtener_datos_anual_mes as odam
import generar_graficas as gg

from datetime import datetime, date, time, timedelta

def tercera_columna(provincia,estacion, imagenes):
    
    if imagenes:
        img = ['<img src="graficos/{0}-T.png">'.format(provincia+'-'+estacion),'<img src="graficos/{0}-H.png">'.format(provincia+'-'+estacion),'<img src="graficos/{0}-B.png">'.format(provincia+'-'+estacion),'<img src="graficos/{0}-V.png">'.format(provincia+'-'+estacion) ]
    else:
        img = ['','','','']
    tc = {
            'hora': str(datetime.now().utcnow())[:19], 
            't' : str(ova.obtener_temperatura(datos_estacion)) + ' ºC',
            'pp' : '-',
            'dv' : ova.obtener_direccion_viento(datos_estacion),
            'v' : str(ova.obtener_viento(datos_estacion)) + ' km/hr',
            'nombre' : provincia+'-'+estacion,
            'T' : img[0],
            'H' : img[1],
            'B' : img[2],
            'V' : img[3],
            }
        
    return '''
    <p>{0[hora]}</p>
    <p>Temperatura: {0[t]}</p>
    <p>Probabilidad Precipitaiones: {0[pp]}</p>
    <div style="height:30px;"></div>
    <p>Dirección del viento: {0[dv]}</p>
    <p>Velocidad del viento: {0[v]}</p>
    <div style="height:30px;"></div>
    {0[T]}
    {0[H]}
    {0[B]}
    {0[V]}
    
    '''.format(tc)
    
    
    

def modificar_parametros(estacion, root, datos_estacion):
    
    t = ova.obtener_temperatura(datos_estacion)
    h = ova.obtener_humedad(datos_estacion)
    vv = ova.obtener_viento(datos_estacion)
    icmax, stmax = ova.obtener_ic_st_max_hoy(datos_estacion)
    provincia = ovx.obtener_localidad_provincia(root)[1]
    datos_json = gd.leer_datos(provincia+'-'+estacion)
    a = str(datetime.now().utcnow())[:4]
    m = str(datetime.now().utcnow())[5:7]
    try:
        t_gg, t_dias = gg.obtener_param_7_dias(datos_json,'t')
        hr_gg, hr_dias = gg.obtener_param_7_dias(datos_json,'hr')
        bar_gg, bar_dias = gg.obtener_param_7_dias(datos_json,'bar')
        v_gg, v_dias = gg.obtener_param_7_dias(datos_json,'v')
        
        gg.dibuja(provincia+'-'+estacion+'-T',t_gg,t_dias,'Temperatura')
        gg.dibuja(provincia+'-'+estacion+'-H',hr_gg,hr_dias,'Humedad')
        gg.dibuja(provincia+'-'+estacion+'-B',bar_gg,bar_dias,'Barómetro')
        gg.dibuja(provincia+'-'+estacion+'-V',v_gg,v_dias,'Viento')
        
        tc = tercera_columna(provincia,estacion,True)
    except:
        tc = tercera_columna(provincia,estacion,False)
    
    gh.valores['prov'] = provincia
    gh.valores['est'] = estacion
    gh.valores['tablas'] = tc
    gh.valores['t_val'] = str(t) + ' ºC'
    gh.valores['h_val'] = str(h) + ' %'
    gh.valores['pr_val'] = str(ova.obtener_punto_rocio(t, h)) + ' ºC'
    gh.valores['v_val'] = '<p>' + str(vv) + ' km/hr</p><p>dir:' + ova.obtener_direccion_viento(datos_estacion) + '</p>'
    gh.valores['vm_val'] = str(ova.obtener_viento_10(datos_estacion)) + ' km/hr'
    gh.valores['b_val'] = str(ova.obtener_barometro(datos_estacion)) + ' hPa'
    gh.valores['llh_val'] = str(ova.obtener_lluvia_hoy(datos_estacion)) + ' mm'
    gh.valores['ill_val'] = str(ova.obtener_intensidad_lluvia(datos_estacion)) + ' mm'
    '''
    gh.valores['llm_val'] = ova.
    gh.valores['llan_val'] = ova.
    gh.valores['llah_val'] = ova.
    '''
    gh.valores['ic_val'] = str(ova.obtener_indice_calor(t,h)) + ' ºC'
    gh.valores['st_val'] = str(ova.obtener_sensacion_termica(t,vv)) + ' ºC'
    gh.valores['utc_val'] = str(ova.obtener_hora_UTC(datos_estacion)).replace('T',' ')
    gh.valores['tmax_val'] = str(ova.obtener_parametro_max_hoy(datos_estacion,'ta')) + ' ºC'
    gh.valores['tmin_val'] = str(ova.obtener_parametro_max_hoy(datos_estacion,'hr')) + ' ºC'
    gh.valores['hmax_val'] = str(ova.obtener_parametro_min_hoy(datos_estacion,'ta')) + ' %'
    gh.valores['hmin_val'] = str(ova.obtener_parametro_min_hoy(datos_estacion,'hr')) + ' %'
    gh.valores['vvm_val'] = str(ova.obtener_parametro_max_hoy(datos_estacion,'vv')) + ' km/hr'
    '''
    gh.valores['illmax_val'] = ova.
    gh.valores['illum_val'] = ova.
    '''
    gh.valores['icmax_val'] = str(icmax) + ' ºC'
    gh.valores['stmin_val'] = str(stmax) + ' ºC'
    gh.valores['tmaxma_val'] = '<p>' + str(odam.obtener_param_max_mes(datos_json,a,m,'t')) + 'ºC</p><p style="color: black;">' +  str(odam.obtener_param_max_año(datos_json,a,'t')) + 'ºC</p>'
    gh.valores['tminma_val'] = '<p>' + str(odam.obtener_param_min_mes(datos_json,a,m,'t')) + 'ºC</p><p style="color: black;">' +  str(odam.obtener_param_min_año(datos_json,a,'t')) + 'ºC</p>'
    gh.valores['hmaxma_val'] = '<p>' + str(odam.obtener_param_max_mes(datos_json,a,m,'hr')) + ' %</p><p style="color: black;">' + str(odam.obtener_param_max_año(datos_json,a,'hr')) + ' %</p>'
    gh.valores['hminma_val'] = '<p>' + str(odam.obtener_param_min_mes(datos_json,a,m,'hr')) + ' %</p><p style="color: black;">' + str(odam.obtener_param_min_año(datos_json,a,'hr')) + ' %</p>'
    gh.valores['bmaxma_val'] = '<p>' + str(odam.obtener_param_max_mes(datos_json,a,m,'bar')) + ' hPa</p><p style="color: black;">' + str(odam.obtener_param_max_año(datos_json,a,'bar')) + ' hPa</p>'
    gh.valores['bminma_val'] = '<p>' + str(odam.obtener_param_min_mes(datos_json,a,m,'bar')) + ' hPa</p><p style="color: black;">' + str(odam.obtener_param_min_año(datos_json,a,'bar')) + ' hPa</p>'
    gh.valores['vvmma_val'] = '<p>' + str(odam.obtener_param_min_mes(datos_json,a,m,'v')) + ' km/hr</p><p style="color: black;">' + str(odam.obtener_param_min_año(datos_json,a,'v')) + ' km/hr</p>'


if __name__ == '__main__':
    
    print('Introduce un código de población:')
    id = input()
    #id = 18188 # Villanueva Mesia
    #id = 39075 # Santander
    root = ovx.obtener_xml(id)
    
    provincia = ovx.obtener_localidad_provincia(root)[1]
    idema, estacion = ova.obtener_idema(provincia)
    datos_estacion = ova.obtener_datos_estacion(idema)
    
    while datos_estacion == -1:
        print('No hay datos para la estacion elegida.\n')
        idema, estacion = ova.obtener_idema(provincia)
        datos_estacion = ova.obtener_datos_estacion(idema)
    
    modificar_parametros(estacion, root, datos_estacion)    
    
    gd.guardar_datos(provincia+'-'+estacion,datos_estacion)
    
    gh.crear_html(provincia+'-'+estacion+ '_'+str(ova.obtener_hora_UTC(datos_estacion))[:10])
    
    print('\nSe ha generado el HTML!!')