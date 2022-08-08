<template>
  <div class="rule">
	<div class="cont">
		<div class="welcome">
			<!-- <button @click="$router.push({name: 'registration'})">Get Started</button> -->
			<div class="title">
				<p>Welcome to <b>Ginger</b></p>
			</div>
			<div class="description">
				<p>Ginger is a quiz game for best friends</p>
			</div>
			<div class="main-button">
				<button @click="$router.push({name: 'registration'})">Get started</button>
			</div>
		</div>
		
	</div>
  </div>
</template>

<script>
export default {
	name: 'HomeFrame',
	created(){
		let item = localStorage.getItem("auth")
		if (item != null){
			this.$router.push({name: "app"})
		} 
	},
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.cont{
	/* display: grid; */
	/* gap: 40px; */
	/* column-gap: 100px; */
	/* row-gap: 1000px; */
	/* align-items: center; */
	/* justify-content: center; */
	/* gap: 14px; */
	width: 100%;
	max-width: 400px;
	min-width: 200px;
}
.title b{
	color: #756ba3;
	/* font-size: 30px; */
	font-weight: 700;
}
.welcome{
	background-color: #181e41;
	border-radius: 0 26px;
	padding: 24px 30px;
	box-sizing: border-box;
	display: grid;
	gap: 14px;
}
.description{
	/* margin-top: 14px; */
	/* text-align: center; */
	color: #fff;
	display: flex;
	justify-content: center;
	line-height: 20px;
	color: #514879;
}
.title{
	/* text-align: center; */
	line-height: 30px;
	font-size: 30px;
	font-weight: 500;
	color: #fff;
	display: flex;
	/* align-items: center; */
	justify-content: center;
}
.rule{
	/* background-color: #000; */
	width: 100vw;
	height: 100%;
	display: flex;
	align-items: center;
	justify-content: center;
	
	/* background-repeat: no-repeat; */
	/* background-size: cover; */
	padding: 30px;
	box-sizing: border-box;
}
.button button{
	outline: none;
	border:none;
	color: #fff;
	background-color: #40cd79;
	/* width: 360px; */
	width: 100%;
	height: 70px;
	font-weight: 700;
	font-size: 26px;
	border-radius: 0 26px 0 26px;
}
.main-button button{
	width: 100%;
	height: 60px;
	border: none;
	outline: none;
	background-color: #40cd79;
	font-size: 20px;
	color: #202342;
	/* font-weight: 700; */
	/* border-radius: 0 10px 0 10px; */
	border-radius: 0 14px;
	cursor: pointer;
}
</style>
