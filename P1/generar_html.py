# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 19:20:14 2017

@author: Mario

"""


import os


plantilla = '''
<!DOCTYPE html>
<html>
    <head>
		<meta charset="utf-8">
		<title>Datos AEMET</title>
		<style type="text/css">
			html, body{{
				width: 98%;
				height: 98%;
			}}
			#tabla {{

				width: 100%;
				border: 1px solid #000;
				border-collapse: collapse;
			}}

			th, td {{
				border: 2px solid #000;
			}}

			.titulo{{
				height: 50px;
				background-color: black;
				color: white;
			}}

			.c12_1 {{
				width: 15%;
				height: 50px;
				color: #0000CC;
			}}

			.c12_2 {{
				width: 15%;
				height: 50px;
				color: #663300;
			}}

			.c12_3 {{
				width: 15%;
				height: 50px;
				color: #006633;
			}}

			#tablas{{
				width: 50%;
				background-color: #CC9966;
			}}

		</style>
	</head>
	<body>
		<table id="tabla">
			<tr>
				<th class="titulo" style="border-bottom: 0;" colspan="2">Tiempo actual en {0[prov]} ({0[est]})</th>
				<th id="tablas" rowspan="36">{0[tablas]}</th>
			</tr>
			<tr>
				<th class="titulo" style="border-top: 0;" colspan="2"></th>
			</tr>
			<tr>
				<th class="c12_1">Temperatura</th>
				<th class="c12_1">{0[t_val]}</th>
			</tr>
			<tr>
				<th class="c12_1">Humedad</th>
				<th class="c12_1">{0[h_val]}</th>
			</tr>
			<tr>
				<th class="c12_1">Punto de rocío</th>
				<th class="c12_1">{0[pr_val]}</th>
			</tr>
			<tr>
				<th class="c12_1">Viento</th>
				<th class="c12_1">{0[v_val]}</th>
			</tr>
			<tr>
				<th class="c12_1">Viento medio (10 min)</th>
				<th class="c12_1">{0[vm_val]}</th>
			</tr>
			<tr>
				<th class="c12_1">Barómetro</th>
				<th class="c12_1">{0[b_val]}</th>
			</tr>
			<tr>
				<th class="c12_1">Lluvia hoy</th>
				<th class="c12_1">{0[llh_val]}</th>
			</tr>
			<tr>
				<th class="c12_1">Intensidad de lluvia</th>
				<th class="c12_1">{0[ill_val]}</th>
			</tr>
			<tr>
				<th class="c12_1">Lluvia mensual</th>
				<th class="c12_1">{0[llm_val]}</th>
			</tr>
			<tr>
				<th class="c12_1">Lluvia año natural</th>
				<th class="c12_1">{0[llan_val]}</th>
			</tr>
			<tr>
				<th class="c12_1">Lluvia año hidrológico</th>
				<th class="c12_1">{0[llah_val]}</th>
			</tr>
			<tr>
				<th class="c12_1">Índice de calor</th>
				<th class="c12_1">{0[ic_val]}</th>
			</tr>
			<tr>
				<th class="c12_1">Sensación térmica (TV)</th>
				<th class="c12_1">{0[st_val]}</th>
			</tr>





			<tr>
				<th class="titulo" style="border-bottom: 0;" colspan="2">Máximas y mínimas de hoy ({0[utc_val]})</th>
			</tr>
			<tr>
				<th class="titulo" style="border-top: 0;" colspan="2"></th>
			</tr>
			<tr>
				<th class="c12_2" style="border-bottom: 0;">Temperatura máxima</th>
				<th class="c12_2" style="border-bottom: 0;">{0[tmax_val]}</th>
			</tr>
			<tr>
				<th class="c12_2" style="border-top: 0;">Temperatura mínima</th>
				<th class="c12_2" style="border-top: 0;">{0[tmin_val]}</th>
			</tr>
			<tr>
				<th class="c12_2" style="border-bottom: 0;">Humedad máxima</th>
				<th class="c12_2" style="border-bottom: 0;">{0[hmax_val]}</th>
			</tr>
			<tr>
				<th class="c12_2" style="border-top: 0;">Humedad mínima</th>
				<th class="c12_2" style="border-top: 0;">{0[hmin_val]}</th>
			</tr>
			<tr>
				<th class="c12_2">Velocidad viento máx.</th>
				<th class="c12_2">{0[vvm_val]}</th>
			</tr>
			<tr>
				<th class="c12_2">Intensidad lluvia máx.</th>
				<th class="c12_2">{0[illmax_val]}</th>
			</tr>
			<tr>
				<th class="c12_2">Intensidad lluvia 1h máx.</th>
				<th class="c12_2">{0[illum_val]}</th>
			</tr>
			<tr>
				<th class="c12_2">Índice de calor máx.</th>
				<th class="c12_2">{0[icmax_val]}</th>
			</tr>
			<tr>
				<th class="c12_2">Sensación térmica mín.</th>
				<th class="c12_2">{0[stmin_val]}</th>
			</tr>





			<tr>
				<th class="titulo" style="border-bottom: 0;" colspan="2">Máximas y mínimas del año</th>
			</tr>
			<tr>
				<th class="titulo" style="border-top: 0;" colspan="2"></th>
			</tr>
			<tr>
				<th class="c12_3" style="border-bottom: 0;">Temperatura máxima</th>
				<th class="c12_3" style="border-bottom: 0;">{0[tmaxma_val]}</th>
			</tr>
			<tr>
				<th class="c12_3" style="border-top: 0;">Temperatura mínima</th>
				<th class="c12_3" style="border-top: 0;">{0[tminma_val]}</th>
			</tr>
			<tr>
				<th class="c12_3" style="border-bottom: 0;">Humedad máxima</th>
				<th class="c12_3" style="border-bottom: 0;">{0[hmaxma_val]}</th>
			</tr>
			<tr>
				<th class="c12_3" style="border-top: 0;">Humedad mínima</th>
				<th class="c12_3" style="border-top: 0;">{0[hminma_val]}</th>
			</tr>
			<tr>
				<th class="c12_3" style="border-bottom: 0;">Barómetro máxima</th>
				<th class="c12_3" style="border-bottom: 0;">{0[bmaxma_val]}</th>
			</tr>
			<tr>
				<th class="c12_3" style="border-top: 0;">Barómetro mínima</th>
				<th class="c12_3" style="border-top: 0;">{0[bminma_val]}</th>
			</tr>
			<tr>
				<th class="c12_3">Velocidad viento máx.</th>
				<th class="c12_3">{0[vvmma_val]}</th>
			</tr>


		</table>
	</body>
</html>
'''

valores = {'prov':'-','est':'-','tablas':'', 't_val':'-', 'h_val':'-', 'pr_val':'-', 'v_val':'-', 'vm_val':'-',\
 'b_val':'-', 'llh_val':'-', 'ill_val':'-', 'llm_val':'-', 'llan_val':'-', \
 'llah_val':'-', 'ic_val':'-', 'st_val':'-', 'utc_val':'-', 'tmax_val':'-', 'tmin_val':'-', \
 'hmax_val':'-', 'hmin_val':'-', 'vvm_val':'-', 'illmax_val':'-', 'illum_val':'-', 'icmax_val':'-', \
 'stmin_val':'-', 'tmaxma_val':'-', 'tminma_val':'-', 'hmaxma_val':'-', 'hminma_val':'-', \
 'bmaxma_val':'-', 'bminma_val':'-', 'vvmma_val':'-'}


def crear_html(nombre):
    
    try:
        os.stat('html/')
    except:
        os.mkdir('html/') 
        
    f = open('html/'+nombre + '.html', 'w',encoding='utf-8')
    f.write(plantilla.format(valores))
    f.close()
    
if __name__ == '__main__':
    
    s = 'hola {0[nombre]} {0[apellido]}'
    
    lista = {'nombre':'Mario', 'apellido':'Ruiz'}
    print(lista)
    print(s.format(lista))