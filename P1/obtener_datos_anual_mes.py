# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 17:24:38 2017

@author: Mario
"""


def obtener_param_max_mes(datos_json, a, m, param):
    
    if datos_json == []:
        return '-'
    
    pmax = -10000
    for d in datos_json[a][m]:
        for h in datos_json[a][m][d]:
            if datos_json[a][m][d][h][param] > pmax:
                pmax = datos_json[a][m][d][h][param]
            #print (param,d,h,datos_json[a][m][d][h][param])
    
    return pmax


def obtener_param_min_mes(datos_json, a, m, param):
    
    if datos_json == []:
        return '-'
    
    pmin = 10000
    for d in datos_json[a][m]:
        for h in datos_json[a][m][d]:
            if datos_json[a][m][d][h][param] < pmin:
                pmin = datos_json[a][m][d][h][param]
            #print (param,d,h,datos_json[a][m][d][h][param])
    
    return pmin


def obtener_param_max_año(datos_json, a, param):
    
    if datos_json == []:
        return '-'
    
    pmax = -10000
    for m in datos_json[a]:
        for d in datos_json[a][m]:
            for h in datos_json[a][m][d]:
                if datos_json[a][m][d][h][param] > pmax:
                    pmax = datos_json[a][m][d][h][param]
                #print (param,d,h,datos_json[a][m][d][h][param])
    
    return pmax


def obtener_param_min_año(datos_json, a, param):
    
    if datos_json == []:
        return '-'
    
    pmin = 10000
    for m in datos_json[a]:
        for d in datos_json[a][m]:
            for h in datos_json[a][m][d]:
                if datos_json[a][m][d][h][param] < pmin:
                    pmin = datos_json[a][m][d][h][param]
                #print (param,d,h,datos_json[a][m][d][h][param])
    
    return pmin


if __name__ == '__main__':
    
    import obtener_valores_api as ova
    import obtener_valores_xml as ovx
    import guardar_datos as gd
    import obtener_datos_anual_mes as odam
    
    id = 18188 # Villanueva Mesia
    root = ovx.obtener_xml(id)

    provincia = ovx.obtener_localidad_provincia(root)[1]
    idema, estacion = ova.obtener_idema(provincia)
    
    datos_json = gd.leer_datos(provincia+'-'+estacion)
    
    print('max mes t:',obtener_param_max_mes(datos_json,'2017','12','t'))
    print('max mes bar:',obtener_param_max_mes(datos_json,'2017','12','bar'))
    print('max mes hr:',obtener_param_max_mes(datos_json,'2017','12','hr'))
    print('max mes v:',obtener_param_max_mes(datos_json,'2017','12','v'))
    
    print('min mes t:',obtener_param_min_mes(datos_json,'2017','12','t'))
    print('min mes bar:',obtener_param_min_mes(datos_json,'2017','12','bar'))
    print('min mes hr:',obtener_param_min_mes(datos_json,'2017','12','hr'))
    
    print('')
    
    print('max año t:',obtener_param_max_año(datos_json,'2017','t'))
    print('max año bar:',obtener_param_max_año(datos_json,'2017','bar'))
    print('max año hr:',obtener_param_max_año(datos_json,'2017','hr'))
    print('max año v:',obtener_param_max_año(datos_json,'2017','v'))
    
    print('min año t:',obtener_param_min_año(datos_json,'2017','t'))
    print('min año bar:',obtener_param_min_año(datos_json,'2017','bar'))
    print('min año hr:',obtener_param_min_año(datos_json,'2017','hr'))