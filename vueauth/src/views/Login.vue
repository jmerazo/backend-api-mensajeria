
<template>
<div id="app">
  <h1>login</h1>
  <form @submit.prevent="login">
    <div>
      <label for="email">Usuario</label>
      <input type="text" v-model="email" id="email" />
    </div>
    <div>
      <label for="password">Contraseña</label>
      <input type="password" v-model="password" id="password" />
    </div>
    <div style="color: red" v-if="error">
      las credenciales no son validas
    </div>
    <button type="submit">ingresar</button>
  </form>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      email: "",
      password: "",
      error: false,
    };
  },
  methods: {
    login() {
      this.error = false;
      fetch("http://localhost:8000/api-auth/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: this.email,
          password: this.password,
        }),
      })
        .then(async(response) =>{
          if(!response.ok) throw await response.json();
          return response.json();
        })       
        .then((data) => {
          this.$router.push('/consulta')
        }).catch((err) =>{ 
          this.error = true;
          
          });
    },
  },
};
</script>

