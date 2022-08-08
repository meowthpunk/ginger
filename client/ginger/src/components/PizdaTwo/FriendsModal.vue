<template>
	<div class="modal-win">
		<div class="main">
			<div class="container">
				<input type="text" placeholder="Enter your friend login" v-model="send_login">
				<div class="inp-button" @click="sendInvite">
					<p>click</p>
				</div>
			</div>
			<div class="error" :style="{ height: setError}">
				<p>Poshel NahuYY</p>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'FriendsModal',
	methods: {
		sendInvite(){
			// this.$emit('closeModal')
			this.conn.emit("send_friend_invite", {user: this.user.login, friend_invite: this.send_login})
			this.$emit('closeModal')
		}
	},
	data(){
		return {
			error: "",
			send_login: "",
		}
	},
	props: {
		conn: Object,
		user: Object,
	},
	computed: {
		setError(){
			let setError = "40px"
			let delError = "0px"
			if (this.error != ""){
				return setError
			} else {
				return delError
			}
		}
	}
}
</script>

<style scoped>
.error{
	height: 0px;
	display: flex;
	align-items: flex-end;
	justify-content: center;
	overflow: hidden;
	transition: 1s;
}
.modal-win{
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	display: flex;
	align-items: center;
	justify-content: center;
	background-color: rgba(0,0,0,0.7);
}
.container{
	height: 80px;
	display: flex;
	align-items: center;
	justify-content: space-between;
}
.main{
	border-radius: 0 34px;
	padding: 30px;
	box-sizing: border-box;
	background-color: #202342;
	width: 500px;

}
input{
	background-color: #1d1f38;
	height: 80px;
	border-radius: 0 0 0 24px;
	width: 330px;
	color: #fff;
	padding-left: 30px;
	box-sizing: border-box;
	font-size: 20px;
}
input::placeholder{
	color: #514879;
}
.inp-button{
	background-color: #40cd79;
	height: 80px;
	width: 90px;
	border-radius: 0 24px 0 0;
	cursor: pointer;
	display: flex;
	align-items: center;
	justify-content: center;
}

</style>
