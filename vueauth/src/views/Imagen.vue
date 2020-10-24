<template>
    <section class="main_ingreso">
	<section class="contimage_ingreso">
		<section class = "contimage_ingre">
			<font face="Comic Sans MS,Arial,Verdana">
					<section class="conte_ingreso">Digitalizar Pruebas de Entrega</section>
				<section class="conte_ingreso2">	
						<section class="conte_ingreso3">	
								<font size=6 face="Comic Sans MS,Arial,Verdana">
								<h1>Seleccione los archivos<hr><input class="button_imag" type="submit" name="Abrir Archivo" value="Abrir Archivo"><br><br><img src="@/assets/imagenes/tif.png" width="200" height="150">
								</h1>	
								</font>
						</section>
						<section class="conte_ingreso4"></section>
				</section>	
			</font>			
		</section>
	</section>
</section> 
		<section class="aside_ingreso">
			<h1>Mensajero</h1>
			<hr>
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
import Footer from '@/components/Footer.vue'
export default {

    components: {
    Footer,
  
  }
}
</script>
<style>
    .main_ingreso{
	padding-top: 0rem;
	width: 100%; 
	width: auto;
	
}
.contimage_ingreso{
	float: left;
	width: 82%;	
	height: 520px;
	margin-right: 3%;
	border-radius: 2px;
	background: white;
	padding-top: 2rem;


}
.contimage_ingre{
	float: left;
	width: 90%;	
	height: 500px;
	background: white;
	padding-top: 0rem;
	

}
.conte_ingreso{
	float: left;
	width: 35%;	
	height: 25px;
	border-top-left-radius: 20px;
	border-top-right-radius: 20px;
	background: #909CB4;
	color: white;
	text-align: center;
	margin-left: 4rem;
    

}
.conte_ingreso2{
	float: left;
	width: 950px;	
	height: 400px;
	background: #DCE4F3;
	color: white;
	text-align: left;
	margin-left: 4rem;
	border-bottom-left-radius: 20px;
	border-bottom-right-radius: 20px;
	border-top-right-radius: 20px;
	
}
.conte_ingreso3{
	float: left;
	width: 300px;	
	height: 100%;
	background: #DCE4F3;
	color: #1F4181;
	text-align: center;
	margin-left: 2rem;
	
	
}
.conte_ingreso4{
	float: right;
	width: 500px;	
	height: 340px;
	background: #909CB4;
	color: #1F4181;
	text-align: center;
	border-radius: 20px;
	margin-top: 2rem;
	margin-right: 2rem;
	
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
.button_imag{
	border:none;
	width: 80%;
	color: white;
	font-size: 20px;
	background: #909CB4;
	padding: 3px 3px;
	border-radius: 20px;	
	cursor: pointer;
	text-align: center;
	margin-top: 0rem;
}
.imge{
	padding-left: 10rem;
	padding-top: 5rem;
}
</style>