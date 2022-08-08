<template>
  <router-view @loginUser="console.log(123)"/>
</template>

<script>
export default {
	created(){
		const appHeight = () => {
			const doc = document.documentElement
			doc.style.setProperty('--app-height', `${window.innerHeight}px`)
		}
		window.addEventListener('resize', appHeight)
		appHeight()
	}
}
</script>

<style>

:root {
   --app-height: 100%;
}
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;500;700;800&display=swap');
/* @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap'); */
/* @font-face {
  font-family: 'Gotham';
  src: url(assets/Gotham-Font/GothamMedium.ttf) format('truetype');
  font-weight: normal;
}
@font-face {
  font-family: 'Gotham';
  src: url(assets/Gotham-Font/GothamBold.ttf) format('truetype');
  font-weight: 800;
}
@font-face {
  font-family: 'Gotham';
  src: url(assets/Gotham-Font/GothamLight.ttf) format('truetype');
  font-weight: 300;
} */
/* @font-face {
  font-family: 'Gotham';
  src: url(assets/Gotham-Font/GothamBook.ttf) format('truetype');
  font-weight: book;
} */
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
} */

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
body{
	padding: 0;
	margin: 0;
	font-family: 'Prompt', sans-serif;
	/* font-family: 'DM Sans', sans-serif; */
	/* background-image: url(assets/BG.png); */
	background-image: url(assets/BG.png) ;
	/* background-repeat: no-repeat;
	background-size: cover; */
	/* background-size: cover; */
	padding: 0;
    margin: 0;
    overflow: hidden;
    width: 100vw;
    height: 100vh;
    height: var(--app-height);
}
p{
	margin: 0;
}
button{
	font-family: 'Prompt', sans-serif;
	/* font-family: 'DM Sans', sans-serif; */
}
input{
	font-family: 'Prompt', sans-serif;
	/* font-family: 'DM Sans', sans-serif; */
	outline: none;
	border: none;
}
h1{
	margin: 0;
}

</style>
