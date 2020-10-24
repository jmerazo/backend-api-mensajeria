<template>
    	<section class="main_ingreso">
		<section class="contimage_ingreso">

			<label class="label_devo">Ingreso Centro de Operaciones</label>
			<section class="ingreso_sec_1">
				<form class="form_ingre_1">
					<label style="color: #1F4181;margin-left: 2rem;">Empresa: Cadena</label> <br>
					<label style="color: #1F4181;margin-left: 2rem;"> Cod.Emp : 100250</label><br><br><br>
					<label style="color: #1F4181;margin-left: 4.5rem;">Digite el Número de Guía</label>
					<br>
					<input style="border-radius: 20px; border: none;padding: 10px; width: 250px; margin-left: 2rem;" type="text" name="ingre_codigo"><br><br>
					<label style="color: #1F4181;margin-left: 5rem;">Información de Guía</label><br><br>
					<label class="label_ingre">Guía:</label>
					<input class="info" type="text" id="" name="" value="" readonly><br>
					<label class="label_ingre">Nombre:</label>
					<input class="info" type="text" id="" name="" value="" readonly><br>
					<label class="label_ingre">Dirección:</label> 
					<input class="info" type="text" id="" name="" value="" readonly><br>
					<label class="label_ingre">Ciudad:</label> 
					<input class="info" type="text" id="" name="" value="" readonly><br>
					<label class="label_ingre">Planilla:</label>
					<input  class="info" type="text" id="" name="" value="" readonly><br>
							
				</form>
			</section>
			<input class="cant" type="text" id="" name="" value="" readonly>
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
	</section>
</template>
<script>
import Cabecera from '@/components/Cabecera.vue'
import Footer from '@/components/Footer.vue'
export default {
    components: {
    Cabecera,
    Footer
  }
}
</script>
<style >
.label_ingre{
	color: #1F4181;
	margin-left: 1rem;
	width: 100px;
	

}
.info{
	border-radius: 20px;
	border: none;

}
.cant{
	display: block;
	margin-left: 9rem;
	background: #909CB4;
	width: 200px;
	border-radius: 20px;
	border: none;
	padding: 2px;
	margin-top: 30rem;
}
.label_devo{
	display: block;
	margin-left: 7rem;
	border-radius: 20px;
	background: #909CB4;
	width: 30%;
	text-align: center;
	color: white;
	margin-top: 1rem;
}
.main_ingreso{
	
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
	width: 100%;	
	height: 500px;
	background: white;
	padding-top: 0rem;
}
.ingreso_sec_1{
	width: 340px;
	height: 450px;
	background: #DCE4F3;
	float: left;
	margin-top: 1rem;
	margin-left: 6rem;
	border-radius: 20px;
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