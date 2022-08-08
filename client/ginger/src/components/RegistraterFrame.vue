<template>
	<div class="rule">
		<div class="login">

			

			

			<template v-if="pesik">
				<div class="title">
					<p>Login</p>
				</div>

				<div class="data">
					<input class="inp" :class="{'inp-error': isActiveLog}" type="text" placeholder="Login" v-model="login">
					<input class ="inp" :class="{'inp-error': isActivePass}" type="password" placeholder="Password" v-model="password">
					<div 
						class="error"
						:style="{height: returnErrorWidth, marginTop: returnErrorMargin}"
					>
						<p>{{err_txt}}</p>
					</div>
				</div>

				

				<div class="conf-bar">
					<div class="checker">
						<input type="checkbox" id="check">
						<label for="check">Remember me</label>
					</div>
					<!-- <div class="forgot">
						<p>Forgot password?</p>
					</div> -->
				</div>

				<div class="main-button">
					<button @click="printLogin">Login</button>
				</div>

				<div class="sec-button" @click="singerUp">
					<p>Dont have an account? <b class="conf">Create new one</b></p>
					
				</div>				
			</template>
			<template v-else>
				<div class="title">
					<p>Registration</p>
				</div>

				<div class="data">
					<input class="inp" :class="{'inp-error': isActiveLog}" type="text" placeholder="Login" v-model="login">
					<input class ="inp" :class="{'inp-error': isActivePass}" type="password" placeholder="Password" v-model="password">
					<input class ="inp" :class="{'inp-error': isActivePassConf}" type="password" placeholder="Confirm Password" v-model="password_confirm">
					<div 
						class="error"
						:style="{height: returnErrorWidth, marginTop: returnErrorMargin}"
					>
						<p>{{err_txt}}</p>
					</div>
				</div>

				

				<div class="conf-bar">
					<div class="checker">
						<input type="checkbox" id="check">
						<label for="check">Accept the Privacy Policy</label>
					</div>
				</div>

				<div class="main-button">
					<button @click="printRegistration">Sing up</button>
				</div>

				<div class="sec-button" @click="singerUp">
					<p>Already have an account? <b class="conf">Login</b></p>
					
				</div>
			</template>
		</div>
	</div>
</template>

<script>
export default {
	name: 'RegistraterFrame',
	data(){
		return{
			login: "",
			password: "",
			showError: false,
			isActiveLog: false,
			isActivePass: false,
			isActivePassConf: false,
			pesik: true,
			conn: null,
			err_txt: "",
			password_confirm: "",
		}
	},
	created(){
		// const http = require("http")
		// const io = require("socket.io")
		let item = localStorage.getItem("auth")
		if (item != null){
			this.$router.push({name: "app"})
		} else {
			const io = require('socket.io-client')
			this.conn = io.connect('http://192.168.0.101:8080/login');

			this.conn.on("connect", () => {
				console.log('conn is connected')
			})

			this.conn.on("try_to_login", (data) => {

				console.log('try_to_login' + " " + data.succes)

				switch(data.succes) {
					case 404:  // if (x === 'value1')
						this.err_txt = "User with this login not found"
						this.showErrorSet()
						this.password = ""
						break
					case 402:  // if (x === 'value2')
						this.err_txt = "Nepraviny login or password"
						this.showErrorSet()
						this.password = ""
						break
					case 100:
						this.err_txt = ""
						this.showErrorDel()
						this.conn.disconnect()
						this.$router.push({name: "app"})
						// localStorage.setItem("login", this.login)
						// localStorage.setItem("password", this.password)
						localStorage.setItem("auth", JSON.stringify({succes: true, data:{login: this.login, password: this.password}}))
						
						break
					}
				
				
			})
			this.conn.on("try_to_registrate", (data) => {

				console.log('try_to_registrate' + " " + data.succes)

				switch(data.succes) {
					case 401:  // if (x === 'value1')
						this.err_txt = "User uzhe est takoy"
						this.showErrorSet()
						this.password = ""
						this.password_confirm = ""
						break
					case 101:
						this.err_txt = ""
						this.showErrorDel()
						this.conn.disconnect()
						this.$router.push({name: "app"})
						localStorage.setItem("auth", JSON.stringify({succes: true, data:{login: this.login, password: this.password}}))
						break
					}
				
				
			})
		}
	},
	
	methods: {
		singerUp(){
			this.pesik = !this.pesik
			this.err_txt = ""
			this.showErrorDel()
		},
		printLogin(){
			let pesa = false
			let err_text = "Vvedite "
			if (this.login == ''){
				pesa = true
				this.errLog()
				err_text += "login "
			}
			
			if (this.password == ''){
				pesa = true
				this.errPass()
				err_text += "password "
			}
			
			if (pesa == false){
				// this.showErrorDel()
				this.conn.emit("login", this.login, this.password)
				
			} else {
				this.showErrorSet()
				err_text += "please."
				this.err_txt = err_text
				
			}
		},

		printRegistration(){
			let pesa = false
			let err_text = "Vvedite "
			if (this.login == ''){
				pesa = true
				this.errLog()
				err_text += "login "
			}
			if (this.password_confirm == ''){
				pesa = true
				this.errPassConf()
				err_text += "password_conf "
			}
			if (this.password == ''){
				pesa = true
				this.errPass()
				err_text += "password "
			}
			if (pesa == false){
				// this.showErrorDel()
				if (this.password != this.password_confirm){
					this.err_txt = "passwordy ne sovpadaut"
					this.showErrorSet()
					this.errPassConf()
					this.errPass()
					this.password = ""
					this.password_confirm = ""
				} else {
					this.conn.emit("registration", this.login, this.password)
				}
				
			} else {
				this.showErrorSet()
				err_text += ""
				this.err_txt = err_text
				
			}
		},

		errPass(){
			this.isActivePass = true
			setTimeout(() => { this.isActivePass = false }, 1000);
		},
		errPassConf(){
			this.isActivePassConf = true
			setTimeout(() => { this.isActivePassConf = false }, 1000);
		},
		errLog(){
			this.isActiveLog = true
			setTimeout(() => { this.isActiveLog = false }, 1000);
		},
		showErrorSet(){
			if (this.showError == false){
			this.showError = true
			}
		},
		showErrorDel(){
			if (this.showError == true){
				this.showError = false
			}
		}
	},
	computed:{
		returnErrorWidth(){
			if (this.showError == false){
				return "0px"
			}
			return "20px"
		},
		returnErrorMargin(){
			if (this.showError == false){
				return "0px"
			}
			return "20px"
		}
	},
}
</script>

<style scoped>
.conf-bar{
	display: flex;
	justify-content: space-between;
	color: #514879;
	font-size: 14px;
	align-items: center;
	height: 30px;
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
.login{
	width: 100%;
	max-width: 400px;
	/* height: 500px; */
	background-color: #181e41;
	padding: 30px 40px 36px 40px;
	box-sizing: border-box;
	display: grid;
	border-radius: 0 30px 0 30px;
	gap: 20px;
	transition: 1s;
}
.title{
	font-weight: 700;
	font-size: 38px;
	color: #dfdfdf;
	cursor: default;
}
.sec-button{
	display: flex;
	justify-content: center;
	cursor: pointer;
}
.sec-button p{
	font-size: 14px;
	color: #514879;
	line-height: 18px;
}
.sec-button .conf{
	color: #40cd79;
	margin-left: 4px;
	font-weight: normal;
}
.inp{
	background-color: #2a2d4e;
	color: #756ba3;
	font-size: 20px;
	width: 100%;
	height: 60px;
	padding: 30px;
	box-sizing: border-box;
	border-radius: 0 14px 0 14px;
	transition: 0.5s;
}
.data input+input{
	margin-top: 20px;
}
.inp::placeholder{
	color: #514879;
	transition: 1s;
}
.inp-error{
	background-color: #3e2c46;
	color: #753565;
}
.inp-error::placeholder{
	color: #753565;
}
.checker input[type="checkbox"]{
	display: none;
}
label{
	position: relative;
	left: 28px;
	top: 0px;
}
label::before{
	content: "";
	/* background-color: #fff; */
	border: 2px solid #514879;
	box-sizing: border-box;

	position: absolute;
	left: -44px;
	width: 20px;
	height: 20px;
	border-radius: 5px;
	transition: 0.5s;
	left: -28px;
	top: -1px;
}
.checker input[type="checkbox"]:checked + label::before{
	background-color: #40cd79;
	border-color: #40cd79;
}
.checker{
	cursor: pointer;
	height: 100%;
	/* width: 100%; */
	/* flex-grow: 1; */
	display: flex;
	align-items: center;
}
.forgot{
	height: 100%;
	display: flex;
	align-items: center;
	cursor: pointer;
}
.main-button button{
	cursor: pointer;
}
.error{
	display: flex;
	justify-content: center;
	color: #ff0f3f;
	font-size: 14px;
	transition: 1s;
	/* height: 100%; */
	/* height: 0; */
	overflow:hidden;
	
	/* display: flex; */
	/* align-items: end; */
}
</style>