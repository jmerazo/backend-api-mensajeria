<template>
    <font face="Comic Sans MS,Arial,Verdana"><section class="main_ingreso">
	<section class="contimage_ingreso">
		<section class="contimage_ingre">
			<section class="conte_ingreso">Historial de Usuarios</section>
			    <section class="conte_consul">	
					<section class="conte_consul2">
							Ingrese el número de guía
							<input class="guia" type="text" name="guia">
					</section>
					<section class="conte_consul3">
							<form>
							<input name="cbdireccion" type="radio" />Dirección
							<br />
							<input name="cbnombre" type="radio" />Nombre
							<br />
							<input name="cbcodigo" type="radio" />Por Código de Barra
							<br />
							<input name="cbexacto" type="radio" />Exacto
						</form>
					</section>
					<section class="consulta_consul4">
							<input type="submit" name="buscar" value="Buscar" class="buscar">
					</section>

				</section>	
			<section class="conte_ingre_consul2">Resultado de La Busqueda</section>

				<section class="conte_consul_2">	

					<section class="conte_consul_5">
							<form action="" class="form_consul_1"> 
								
							<label class="label_cons">Nombres  </label><input class="inp_cons" type="text" id="" name="y" value="" readonly><br>
							<label class="label_cons">Apellidos</label><input class="inp_cons" type="text" id="" name="" value="" readonly><br>
							<label class="label_cons">Celular </label><input class="inp_cons" type="number" id="" name="" value="" readonly><br>
							<input  class="btvpe_cons"  type="button" value="Visualizar prueba de entrega" name="btvpe">
							</form>
					</section>
					<section class="conte_consul_6">
						<form action="" class="form_consul_1">
							<label  class="label_cons">Dirección</label><input class="inp_cons" type="text" id="" name="" value="" readonly><br>
							<label class="label_cons">Recepción</label><input class="inp_cons" type="text" id="" name="" value="" readonly><br>
							<label class="label_cons">Recepción</label><input class="inp_cons" type="text" id="" name="" value="" readonly><br>
							<label class="label_cons">Recepción</label><input class="inp_cons" type="text" id="" name="" value="" readonly>
						</form>
					</section>
				</section>
		</section>
	</section> 
</section></font>
	<section class="aside_ingreso">
			<h1>Mensajero</h1>
			<div><input onclick="location.href='registrar_mensajeros.html'" type="submit" value="Registrar" class="button_men"></div>
			<hr>
			<div><input onclick="location.href='asignar_correo.html'" type="submit" value="Asignar Correo" class="button_men"></div>
			<hr>
			<div><input onclick="location.href='reporte_correo.html'" type="submit" value="Reporte Correo" class="button_men"></div>
			<hr>
			<div><input onclick="location.href='planillas.html'" type="submit" value="Planillas" class="button_men"></div>
			<hr>
			<div><input onclick="location.href='listar_mensajeros.html'" type="submit" value="Listar Mensajeros" class="button_men">
			</div>
	</section>
</template>
<script>
import Cabecera from '@/components/Cabecera.vue'
import Footer from '@/components/Footer.vue'
export default {
    components: {
    Cabecera,
    Footer,
  
  }
}
</script>
<style>
.main_ingreso{
	
	width: 100%; 
	width: auto;
	
}
.contimage_ingreso{
	float: left;
	width: 82%;	
	margin-right: 3%;
	border-radius: 2px;
	background: white;
	padding-top: 2rem;


}
.contimage_ingre{
	float: left;
	width: 100%;	
	height: 500px;
	background: white;
	padding-top: 0rem;
	

}
.conte_ingreso{
	float: left;
	width: 35%;	
	height: 35px;
	border-top-left-radius: 20px;
	border-top-right-radius: 20px;
	background: #909CB4;
	color: white;
	text-align: center;
	margin-left: 4rem;

}
.conte_consul{
	float: left;
	width: 954px;	
	height: 150px;
	background: #DCE4F3;
	color: white;
	text-align: left;
	margin-left: 4rem;
	border-bottom-left-radius: 20px;
	border-bottom-right-radius: 20px;
	border-top-right-radius: 20px;
	
}
.conte_consul2{
	float: left;
	width: 450px;
	height: 126px;
	background: #DCE4F3;
	margin-top: 0.5rem;
	margin-left: 1rem;
	text-align: left;
	color: #1F4181;
}
.conte_consul3{
	float: left;
	width: 220px;
	height: 126px;
	background: #DCE4F3;
	margin-top: 0.5rem;
	margin-left: 3rem;
	color: #1F4181;
}
.consulta_consul4{
	float: right;
	width: 150px;
	height: 100px;
	background: #DCE4F3;
	margin-top: 2rem;
	margin-right: 1rem;
}
.conte_ingre_consul2{
	float: left;
	width: 35%;	
	height: 35px;
	margin-top: 0.91rem;
	background: #909CB4;
	color: white;
	text-align: center;
	margin-left: 4rem;
	border-top-left-radius: 20px;
	border-top-right-radius: 20px;
	border-bottom-left-radius: 0px;
	border-bottom-right-radius: 0px;

}
.conte_consul_2{
	
	width: 95%;	
	height: 300px;
	background: #DCE4F3;
	color: white;
	text-align: left;
	margin-left: 4rem;
	margin-bottom: 5rem;
	border-bottom-left-radius: 20px;
	border-bottom-right-radius: 20px;
	border-top-right-radius: 20px;
	margin-top: 14.7rem;
}
.conte_consul_5{
	float: left;
	width: 43%;
	height: 250px;
	background: #DCE4F3;
	color: #1F4181;
	border-radius: 20PX;
	margin-right: 5rem;
	margin-top: 2rem;
	margin-left: 2rem;
}
.inp_cons{
	font-size: 5px;
	width: 70%;
	padding: 12px;
	border: none;
	background: #C0C4CB;
	border-radius: 20px;
	display: block;
	float: left;
	margin-top: 0.5rem;
	text-align: center;

}
.btvpe_cons{
	border:none;
	background:#1F4181;
	color: white;
	border-radius: 20px;
	display: block;
	float: left;
	margin-top: 0.5rem;
	text-align: center;
	width: 99%;
	height: 30px;
}
.conte_consul_6{

	float: left;
	width: 43%;
	height: 250px;
	background: #DCE4F3;
	color: #1F4181;
	border-radius: 20PX;
	margin-top: 2rem;

}
.form_consul1{
	background: #ff3f;
	padding: 5px;
	border-radius: 10px;
}
.label_cons{
	display: block;
	float: left;
	width: 24%;
	border-radius: 20px;
	background: #1F4181;
	color: white;
	text-align: center;
}
.aside_ingreso{
	float: left;
	width: 15%;
	height: 650px;
	box-sizing: border-box;
	background: #C0C4CB;
	color: white;
	text-align: center;


}
.button_men{
	border:none;
	width: 100%;
	color: white;
	font-size: 20px;
	background: #909CB4;
	padding: 4px 4px;
	border-radius: 10px;	
	cursor: pointer;
	text-align: left;
}
</style>