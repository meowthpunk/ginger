<template>
	<div class="img">
		<img
			:src="avatar"
			alt=""
		/>
	</div>
	<div class="login">
		<p>{{login}}</p>
	</div>
	<div 
		class="status"
		:class="{'friend-invite': isFriendInvite}"
	>
		<p>{{status_text}}</p>
	</div>
	<div class="buttons">
		<div v-if="status == 'invite'" class="button" @click="acceptFriend">
			<i class="uil uil-check"></i>
		</div>
		<div v-if="status == 'invite'" class="button" @click="declineFriend">
			<i class="uil uil-times"></i>
		</div>
		<div v-if="status == 'friend'" class="button" @click="removeFriend">
			<i class="uil uil-trash-alt"></i>
		</div>
	</div>
</template>

<script>
export default {
	data(){
		return{
			status_text: "unnown",
			isFriendInvite: false,
		}
	},
	props:{
		login: String,
		status: String,
		avatar: String,
	},
	created(){
		switch(this.status){
			case "friend":
				this.status_text = "Friend"
				break
			case "invite":
				this.status_text = "Suggest friendship"
				this.isFriendInvite = true
				break
			case "not_accepted":
				this.status_text = "Wait for accept"
				break
		}
	},
	methods:{
		removeFriend(){
			this.$emit('removeFriend')
		},
		declineFriend(){
			this.$emit('declineFriend')
		},
		acceptFriend(){
			this.$emit('acceptFriend')
		},
	}
}
</script>

<style scoped>
.login {
    display: flex;
    align-items: center;
    padding-left: 20px;
    font-size: 24px;
    color: #fff;
}
.status {
    display: flex;
    padding-left: 20px;
    font-size: 14px;
    color: #fff;
}
.img {
    grid-row-start: 1;
    grid-row-end: span 2;
}
.img img {
    height: 100%;
}
.friend-invite{
	color: #ffdd65;
}
.buttons{
	grid-row-start: 1;
    grid-row-end: span 2;
	grid-column-start: 3;
	display: flex;
	align-items: center;
	justify-content: flex-end;
}
.button{
	background-color: #000;
	color: #fff;
	width: 30px;
	height: 30px;
	display: flex;
	align-items: center;
	justify-content: center;
	border-radius: 6px;
	cursor: pointer;
}
.button + .button{
	margin-left: 6px;
}
</style>