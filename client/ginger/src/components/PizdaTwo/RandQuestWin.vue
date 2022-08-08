<template>
	<div class="win">
		<div class="container">
			<div class="main-quest">
				<div class="text">
					<p>{{rand_quest.quest}}</p>
				</div>
			</div>
			<div class="answer-cont">
				<div class="answers">
					<div for="1" class="lbl-quest" @click="check(1)" :class="{'checked': checked_id==1, 'opc': isOpc(1)}">
						<div class="quest-box">
							<div class="checkbox">
								<div class="checker"></div>
							</div>
							<div class="quest-txt">
								<div class="label">
									<p>A:</p>
								</div>
								<div class="txt">
									<p>{{rand_quest.answers[1]}}</p>
								</div>
							</div>
						</div>
					</div>
					<div for="2" class="lbl-quest" @click="check(2)" :class="{'checked': checked_id==2, 'opc': isOpc(2)}">
						<div class="quest-box">
							<div class="checkbox">
								<div class="checker"></div>
							</div>
							<div class="quest-txt">
								<div class="label">
									<p>B:</p>
								</div>
								<div class="txt">
									<p>{{rand_quest.answers[2]}}</p>
								</div>
							</div>
						</div>
					</div>
					<div for="3" class="lbl-quest" @click="check(3)" :class="{'checked': checked_id==3, 'opc': isOpc(3)}">
						<div class="quest-box">
							<div class="checkbox">
								<div class="checker"></div>
							</div>
							<div class="quest-txt">
								<div class="label">
									<p>C:</p>
								</div>
								<div class="txt">
									<p>{{rand_quest.answers[3]}}</p>
								</div>
							</div>
						</div>
					</div>
					<div for="4" class="lbl-quest" @click="check(4)" :class="{'checked': checked_id==4, 'opc': isOpc(4)}">
						<div class="quest-box">
							<div class="checkbox">
								<div class="checker"></div>
							</div>
							<div class="quest-txt">
								<div class="label">
									<p>D:</p>
								</div>
								<div class="txt">
									<p>{{rand_quest.answers[4]}}</p>
								</div>
							</div>
						</div>
					</div>
				</div>
				<div class="answer-info" @click="pidor">
					<div class="answ-time">
						<p>0:{{timer}}</p>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	// watch:{
	// 	conn(){
	// 		console.log(this.conn)
	// 		this.conn.on("rand_quest", (data)=>{
	// 			console.log(data)
	// 		})
	// 		console.log(this.conn)
	// 	}
	// },
	data(){
		return{
			quest:{
				1: true,
				2: false,
				3: false,
				4: false,
			},
		}
	},
	props:{
		timer: Number,
		checked_id: Number,
		conn: Object,
		rand_quest: Object,
		locked: Boolean,
	},
	methods: {
		pidor(){
			let obj = this.rand_quest.answers
			for (var prop in obj){
				console.log(parseInt(prop))
			}
		},
		check(id){
			
			if(this.locked != true){
				this.$emit("cangeCheckId", id)
			}
		},
		isOpc(id){
			if(this.locked == false){
				return false
			}
			// if(this.quest[id] == false){
			// 	return true
			// }

			let obj = this.rand_quest.answers
			for (var prop in obj){
				if(prop == id){
					if(prop != this.rand_quest.correct){
						return true
					}
				}
			}
			
			return false
		}
	},
}
</script>

<style scoped>
.opc{
	opacity: 0.5;
}

.answer-info{
	background-color: #1d1f38;
	display: flex;
	align-items: center;
	justify-content: center;
}

.lbl-quest{
	overflow: hidden;
	cursor: pointer;
}
.quest-box{
	display: flex;
	/* background-color: #fff; */
	width: 100%;
	height: 100%;
	padding: 10px 30px;
	box-sizing: border-box;
	align-items: center;
	background-color: #1d1f38;
	overflow: hidden;
}
.quest-txt{
	display: flex;
	overflow: hidden;
	
}
.quest-txt p{
	color: #fff;
	font-size: 22px;
}
.checkbox{
	width: 30px;
	height: 30px;
	/* background-color: #fff; */
	border-radius: 0 9px;
	border: 4px solid #fff;
	box-sizing: border-box;
	margin-right: 20px;
	display: flex;
	align-items: center;
	justify-content: center;
}
.checker{
	width: 0px;
	height: 0px;
	background-color: #fff;
	border-radius: 0 2px;

}
.label{
	margin-right: 6px;
}
.nonebox{
	display: none;
}
.main-quest .text{
	color: #fff;
	font-size: 20px;
	text-align: center;
}
.win{
	width: 100%;
	height: 604px;
	display: flex;
	align-items: center;
	justify-content: center;
	box-sizing: border-box;
}
.container{
	width: 100%;
	height: 100%;
	display: grid;
	grid-template-rows: 3fr 2fr;
	/* grid-template-columns: 1fr 1fr; */
	padding: 40px;
	box-sizing: border-box;
	gap: 40px;
}
.main-quest{
	/* grid-column-start: 1;
	grid-column-end: span 2; */
	display: flex;
	align-items: center;
	justify-content: center;
}
.answers{
	grid-template-columns: 1fr 1fr;
	grid-template-rows: 1fr 1fr;
	display: grid;
	gap: 20px;
	width: 100%;
	height: 100%;
	gap: 20px;
}
.answer-cont{
	display: grid;
	grid-template-columns: 6fr 2fr;
	gap: 20px;
}
.answ-time{
	font-size: 30px;
	color: #fff;
}
.checked .quest-box .checkbox .checker{
	/* background-color: #286ab0; */
	width: 12px;
	height: 12px;
}
</style>