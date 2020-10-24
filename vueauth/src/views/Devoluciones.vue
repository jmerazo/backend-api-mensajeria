<template>
<font face="Comic Sans MS,Arial,Verdana">
  <section class="main_ingreso">
		<section class="contimage_ingreso">
			<label class="label_devo">Descarga de Devoluciones</label>
			<section class="devol_1">
				<form class="devol_desc">
					<label style="color: #1F4181; text-align: center;" >Seleccione el motivo de devolución</label><br><br>
          <input name="cbdireccion_E" type="radio" />Dirección Errada-DE
							<br />
							<input name="cbdireccion_I" type="radio" />Dirección Incompleta-DI
							<br />
							<input name="cbdrehusado" type="radio" />Rehusado-RH
							<br />
							<input name="cbdesconocido" type="radio" />Desconocido-DD
							<br />
							<input name="cbtraslado" type="radio" />Traslado-TL
							<br />
							<input name="cbcerrado" type="radio" />Cerrado-CD
							<br />
							<input name="cbtrocado" type="radio" />Trocado-TD
							<br />
							<input name="cbdificil" type="radio" />Dificcil Acesso-DA
							<br />
							<input name="cbotro" type="radio" />Otro
				</form>
			</section>
      <section class="devol_2">
				<br>
				<br>
					<label style="color: white;margin-left: 2rem; margin-left: 2rem;width: 90px;float: left;">
					Guía:</label>
					<input  class="info" type="text" id="" name="" value="" readonly><br>
					<label style="color: white;margin-left: 2rem; width: 90px;float: left;">
					Nombre:</label>
					<input class="info" type="text" id="" name="" value="" readonly><br>
					<label style="color: white;margin-left: 2rem;width: 90px;float: left;">Dirección:</label> 
					<input class="info" type="text" id="" name="" value="" readonly><br>
					<label style="color: white;margin-left: 2rem;width: 90px;float: left;">
					Ciudad:</label> 
					<input  class="info" type="text" id="" name="" value="" readonly><br>
					<label style="color: white;margin-left: 2rem;width: 90px;float: left;">Planilla:</label>
					<input class="info" type="text" id="" name="" value="" readonly><br><br><br>
					<label style="color: white;margin-left: 2rem;">Empresa: Cadena</label> <br>
					<label style="color: white;margin-left: 2rem;"> Cod.Emp : 100250</label><br><br><br>
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
			</div></section>
  </section>
</font>
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
<style>
.info{
  border-radius: 20px;
  border: none;
  padding: 2px;
  width: 150px;
  float: right;
  margin-right: 0.5rem;
  margin-top: 0.3rem;
}
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
.devol_1{
	width: 380px;
	height: 450px;
	background: #DCE4F3;
	float: left;
	margin-top: 2rem;
	margin-left: 6rem;
	border-top-left-radius: 20px;
	border-bottom-left-radius: 20px;
}
.devol_2{
	width: 300px;
	height: 450px;
	background:  #909CB4;
	float: left;
	margin-top: 2rem;
	border-top-right-radius: 20px;
	border-bottom-right-radius: 20px;
}
.label_devo{
	display: block;
	margin-left: 6rem;
	border-radius: 20px;
	background: #909CB4;
	width: 30%;
	text-align: center;
	color: white;
	margin-top: 1rem;
}
.devol_desc{
	text-align: left;
	margin-left: 2rem;
	color: #687795;
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