<template>
	<header class="header">
		<div class="">
			<div class="container">
				<nav class="navbar navbar-expand-lg navbar-light">
				<a class="navbar-brand" href="#"><img src="@/assets/imagenes/logorage.jpeg" width="50" height="50" >  RAGE</a>
					<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
						<span class="navbar-toggler-icon"></span>
					</button>
					<div class="collapse navbar-collapse" id="navbarNavAltMarkup">
						<div class="navbar-nav w-100 justify-content-center">
						<a class="nav-item nav-link active" href="" style="color:#1F4181;">Inicio </a>
						<a class="nav-item nav-link" href="/Ingreso" style="color:#1F4181;">IngresoCO</a>
						<a class="nav-item nav-link" href="/Devoluciones" style="color:#1F4181;">Devoluciones</a>
						<a class="nav-item nav-link" href="/Consulta" style="color:#1F4181;">Consulta</a>
						<a class="nav-item nav-link" href="/Imagen" style="color:#1F4181;">Imagenes</a>
						<a class="nav-item nav-link" href="/Registro" style="color:#1F4181;">Registro</a>

						</div>
					</div>
				</nav>
			</div>
		</div>
	</header>
</template>
<script>
export default {
    name: 'Cabecera'
}
</script>
<style>
.header{
	background-color: #F8F8F9;
	color:#1F4181;
	border-bottom: 1px solid gray;
	border-bottom-right-radius: 20px;
	border-bottom-left-radius: 20px;
}


</style>