<template>
    <form action="php/registro_usuario.php" method="POST" class="formulario">
		<h1>Registrar Usuario</h1>
		<div class="contenedor"></div>
		<div class="input-contenedor">
			<i class="fas fa-user"></i>
			<input type="text" placeholder="Usuario" name="usuario_regis">		
		</div>
		<div class="input-contenedor">
			<i class="fas fa-key"></i>
			<input type="password" placeholder="Contraseña" name="contra_regis">
			
		</div>
		<div class="input-contenedor">
			<i class="fas fa-envelope"></i>
			<input type="email" placeholder="Correo" name="correo_regis">
			
		</div>
		<div class="input-contenedor">
			<i class="fas fa-mobile-alt"></i>
			<input type="number" placeholder="Celular" name="cel_regis">
			
		</div>
		<div>
			<input type="submit" value="Registrar" class="button_form">

		</div>
    </form>
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
    .contenedor{
	width: 100%;
	padding: 10px;
	border-radius: 20px;

}
.formulario{
	background: #E3E5EA;
	padding: 5px;
	border-radius: 20px;

}
.input-contenedor{
	margin-bottom: 20px;
	border:none;
	border-radius: 20px;
	height: 35px;
	margin-left: 2rem;

}
input[type="text"],
input[type="password"],
input[type="email"],
input[type="number"]{
	font-size: 20px;
	width: 85%;
	padding: 3.5px;
	border: none;
}
h1{
	text-align: center;
	color: #1a2537;
	font-size: 40px;
}
.button_form{
	border:none;
	width: 60%;
	height: 40px;
	color: white;
	font-size: 20px;
	background:#1F4181;
	padding: 3px 3px;
	border-radius: 20px;	
	cursor: pointer;
	text-align: center;
	margin-top: 0rem;
	margin-left: 4.5rem;
}
@media(min-width: 800px)
{
.formulario{
	margin:auto;
	width: 355px;
	right: 600px;
	margin-top: 20px;
	border-radius: 20px;
	margin-bottom: 2rem;
}
}
</style>