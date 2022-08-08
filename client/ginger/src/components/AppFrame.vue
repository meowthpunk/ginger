<template>
    <div class="container">
        <div class="application">
            <div class="item">
                <div class="user-menu">
                    <div class="user-pic">
                        <img
                            :src=user.avatar
                            alt=""
                        />
                    </div>
					
                    <div class="user-info">
                        <div class="user-main">
                            <div class="user-login">
                                <p>{{ user.login }}</p>
                            </div>
                            <div class="user-exp">
                                <p>{{ user.expirience }}</p>
                            </div>
                        </div>
                        <div class="user-gems">
                            <p>{{ user.gems }}</p>
                        </div>
                        <div class="user-pg-bar">
                            <div class="user-bar-progress"></div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="item bgn">
                <div class="nav-menu">
                    <div class="menu-item">
                        <p>SHOP</p>
                    </div>
                    <div class="menu-item">
                        <p>LEARNING</p>
                    </div>
                    <div class="menu-item">
                        <p>CUSTOM GAMES</p>
                    </div>
                    <div class="menu-item">
                        <p>SETTINGS</p>
                    </div>
                    <div class="menu-item" @click="logout">
                        <p>LOGOUT</p>
                    </div>
                </div>
            </div>
            <div class="item">
                <div class="item-title">
                    <div class="title-text">
                        <p>Friends</p>
                    </div>
                    <div
                        class="title-button search-friends"
                        @click="showFriendsModal"
                    >
                        <p>Search</p>
                    </div>
                </div>
                <div class="user-friends">
					<div v-for="friend in friendlist.user_not_accepted_friend_invites" class="item-friend" :key="friend">
                        <friend-win
							:avatar = friend.user.avatar
							:login = friend.user.login
							status = "invite"
							@acceptFriend="acceptFriend(friend.user.login)"
							@declineFriend="declineFriend(friend.user.login)"
						/>
                    </div>
                    <div v-for="friend in friendlist.user_friends" class="item-friend" :key="friend">
                        <friend-win
							:avatar = friend.user.avatar
							:login = friend.user.login
							
							status = "friend"
							@removeFriend="removeFriend(friend.user.login)"
						/>
                    </div>
					<div v-for="friend in friendlist.user_friend_invites" class="item-friend" :key="friend" :style="{'opacity': 0.3}">
                        <friend-win
							:avatar = friend.user.avatar
							:login = friend.user.login
							status = "not_accepted"
						/>
                    </div>
                </div>
            </div>
            <div class="item bgn">
                <div class="game-bar">
                    <div class="ranodm-quest">
                        <div class="item-title">
                            <div class="title-text">
                                <p>Random question</p>
                            </div>
                            <div class="title-button">
                                <p>200pts</p>
                            </div>
                        </div>
						<rand-quest-win
							:conn="conn"
							:rand_quest="rand_quest"
							:locked="lockQuest"
							:checked_id="checked_id"
							:timer="timer"
							@cangeCheckId="cangeCheckId"
						/>
                    </div>
                    <div class="game-chat">
                        <div class="item-title">
                            <div class="title-text">
                                <p>Game chat</p>
                            </div>
                        </div>
                        <div class="chat-frame">
                            <div class="chat-messages">
                                <p v-for="mess in chat_messages" :key="mess">
                                    {{ mess.user }}: {{ mess.message }}
                                </p>
                            </div>
                            <div class="chat-inp">
                                <input type="text" v-model="message_to_send" />
                            </div>
                        </div>
                    </div>
                    <div class="game-main-button" @click="sendMessageToChat">
                        <p>START</p>
                    </div>
                </div>
            </div>
        </div>
        <friends-modal
            :conn="conn"
            :user="user"
			
			
            v-show="show_friends_modal"
            @closeModal="show_friends_modal = false"
        />
    </div>
</template>

<script>
import FriendsModal from "@/components/PizdaTwo/FriendsModal.vue";
import FriendWin from "@/components/PizdaTwo/FriendWin.vue";
import RandQuestWin from "@/components/PizdaTwo/RandQuestWin.vue";
export default {
    components: {
        FriendsModal,
		FriendWin,
		RandQuestWin
    },
    data() {
        return {
			lockQuest: true,
			checked_id: 0,
            user: {
                login: "",
                password: "",
                gems: 0,
                expirience: 0,
				avatar: ""
            },
			friendlist: [],
            conn: null,
            message_to_send: "",
            chat_messages: [],
            show_friends_modal: false,
			rand_quest: {
				quest: "",
				answers: {
					1: "",
					2: "",
					3: "",
					4: "",
				},
				correct: 0,
			},
			timer: 0,
			
        };
    },
    name: "HelloWorld",
    mounted() {
        let item = localStorage.getItem("auth");
        if (item == null) {
            this.$router.push({ name: "registration" });
        } else {
            // console.log(item)
            let user = JSON.parse(item).data;
            this.user.login = user.login;
            this.user.password = user.password;

            const io = require("socket.io-client");
            this.conn = io.connect("http://192.168.0.101:8080/auth");
            // console.log(url_user_conn)
            this.conn.on("connect", () => {
                console.log("conn is connected");
            });

            this.conn.on("autorizate", (data) => {
                this.user.gems = data.user.gems;
                this.user.expirience = data.user.expirience;
                this.user.avatar = data.user.avatar;
				this.friendlist = data.friendlist

				console.log(this.friendlist)
            });

            this.conn.on("send_message_to_all_chat", (data) => {
                this.chat_messages.push(data);
            });

			this.conn.on("send_friend_invite", (data) => {
                if (data.user == this.user.login){
					this.friendlist.user_not_accepted_friend_invites.push(data.friend_invite)
				}
            });

			this.conn.on("send_friend_invite_answ", (data) => {
				this.friendlist.user_friend_invites.push(data.friend_invite)
            });

			this.conn.on("accept_friend_invite", (data) => {
                if(data.user == this.user.login){
                    this.friendlist.user_friends.push(data.friend)
					for (var i = 0; i < this.friendlist.user_friend_invites.length; i++) {
						if (this.friendlist.user_friend_invites[i].user.login === data.friend.user.login) {
							this.friendlist.user_friend_invites.splice(i, 1);
						}
					}
				}
            });
			
			this.conn.on("accept_friend_invite_answ", (data) => {
                this.friendlist.user_friends.push(data.friend)
				for (var i = 0; i < this.friendlist.user_not_accepted_friend_invites.length; i++) {
					if (this.friendlist.user_not_accepted_friend_invites[i].user.login === data.friend.user.login) {
						this.friendlist.user_not_accepted_friend_invites.splice(i, 1);
					}
				}
            });

			this.conn.on("decline_friend_invite", (data) => {
                if(data.user == this.user.login){
					for (var i = 0; i < this.friendlist.user_friend_invites.length; i++) {
						if (this.friendlist.user_friend_invites[i].user.login === data.login) {
							this.friendlist.user_friend_invites.splice(i, 1);
						}
					}
				}
            });

			this.conn.on("decline_friend_invite_answ", (data) => {
                for (var i = 0; i < this.friendlist.user_not_accepted_friend_invites.length; i++) {
					if (this.friendlist.user_not_accepted_friend_invites[i].user.login === data.login) {
						this.friendlist.user_not_accepted_friend_invites.splice(i, 1);
					}
				}
            });

			this.conn.on("remove_friend_invite", (data) => {
				if (data.user_frst_login == this.user.login){
                    console.log(data.user_sec_login)
					// let user = this.friendlist.user_friends.filter(user => user.user.login == data.user_sec_login)
					// this.friendlist.user_friends.remove()
					for (var i = 0; i < this.friendlist.user_friends.length; i++) {
						if (this.friendlist.user_friends[i].user.login === data.user_sec_login) {
							this.friendlist.user_friends.splice(i, 1);
						}
					}

					console.log(user)
				}
            });
			
			this.conn.on("remove_friend_invite_answ", (data) => {
				for (var i = 0; i < this.friendlist.user_friends.length; i++) {
					if (this.friendlist.user_friends[i].user.login === data.login) {
						this.friendlist.user_friends.splice(i, 1);
					}
				}
            });

            this.conn.emit("autorizate", this.user.login, this.user.password);


			this.conn.on("rand_quest", (data)=>{
				console.log(data)
				console.log("rand_quest")
				this.rand_quest = data.data
				this.unlockAnswers()
				this.timer = 20
				let timer = setInterval(() => {this.timer -= 1; console.log(this.timer); if(this.timer == 0){clearInterval(timer)}},1000);
			})
			this.conn.on("rand_quest_answ", ()=>{
				this.lockAnswers()
			})
        }
    },
    methods: {
		cangeCheckId(id){
			this.checked_id = id
		},
		lockAnswers(){
			this.lockQuest = true
		},
		unlockAnswers(){
			this.lockQuest = false
			this.checked_id = null
		},
		acceptFriend(user_sec_login){
			this.conn.emit("accept_friend_invite", {user_frst_login: this.user.login, user_sec_login: user_sec_login});
		},
		declineFriend(user_sec_login){
			this.conn.emit("decline_friend_invite", {user_frst_login: this.user.login, user_sec_login: user_sec_login});
		},
		removeFriend(user_sec_login){
			this.conn.emit("remove_friend", {user_frst_login: this.user.login, user_sec_login: user_sec_login});
		},
        logout() {
            localStorage.removeItem("auth");
            this.$router.push({ name: "home" });
        },
        sendMessageToChat() {
            let message = {
                message: this.message_to_send,
                user: this.user.login,
            };
            this.conn.emit("send_mess_to_all_chat", message);
            this.message_to_send = "";
        },
        showFriendsModal() {
            this.show_friends_modal = true;
        },
    },
};
</script>
<style scoped>
.search-friends {
    cursor: pointer;
}
.chat-messages {
    overflow-y: scroll;
}
.chat-messages {
    color: #fff;
    font-size: 20px;
    line-height: 25px;
    word-break: break-all;
}
.chat-frame {
    padding: 14px;
    box-sizing: border-box;
    height: 422px;
    display: grid;
    gap: 14px;
    grid-template-rows: 1fr 60px;
}
.chat-inp input {
    background-color: #1d1f38;
    color: #fff;
    font-size: 20px;
    font-weight: 500;
    width: 100%;
    height: 100%;
    box-sizing: border-box;
    border-radius: 14px;
    padding-left: 20px;
}
.item-title {
    background-color: #1c1c1c;
    color: #fff;
    font-size: 20px;
    display: flex;
    justify-content: space-between;
    padding: 4px 14px;
}
.item-friend {
    display: grid;
    grid-template-columns: 100px 1fr 80px;
    grid-template-rows: 1fr 1fr;
    /* height: 90px; */
    height: 100px;
    width: 100%;
}


.user-login {
    font-weight: 700;
    font-size: 28px;
}
.user-exp {
    font-weight: 500;
    font-size: 18px;
}
.application {
    width: 100%;
    height: 100%;
    display: grid;
    grid-template-columns: 460px auto;
    grid-template-rows: 140px auto;
    gap: 30px;
    /* overflow: hidden; */
}
.container {
    width: 100%;
    height: 100%;
    padding: 60px;
    box-sizing: border-box;
}
.game-bar {
    width: 100%;
    box-sizing: border-box;
    height: 100%;
    display: grid;
    grid-template-rows: 460px 1fr;
    grid-template-columns: 900px 1fr;
    gap: 34px;
}

.user-friends {
    width: 100%;
	height: 100%;
    max-height: 576px;
    box-sizing: border-box;
    padding: 0 14px;
    overflow-y: scroll;
    margin: 14px 0 6px 0;
}
.item-friend + .item-friend{
	margin-top: 14px;
}
.nav-menu {
    width: 100%;
    box-sizing: border-box;
    height: 100%;
    display: flex;
    justify-content: space-between;
    padding: 0 40px;
    box-sizing: border-box;
    align-items: center;
}

.menu-item {
    color: #fff;
    background-color: #202342;
    box-sizing: border-box;
    padding: 26px 60px;
    font-size: 20px;
    font-weight: 700;
}
.user-menu {
    display: flex;
    /* grid-template-columns: ; */
    padding: 10px;
    width: 100%;
    height: 100%;
    box-sizing: border-box;
    color: #fff;
}
.user-pic img {
    height: 100%;
}
.user-pic {
    height: 100%;
}
.user-info {
    width: 100%;
    display: grid;
    grid-template-columns: auto 1fr;

    padding: 0 0 0 10px;
    box-sizing: border-box;
}
.user-gems {
    display: flex;
    /* align-items: end; */
    /* align-items: center; */
    justify-content: flex-end;
    padding-top: 12px;
    padding-right: 12px;
    font-weight: 700;
    font-size: 20px;
}
.user-pg-bar {
    grid-column-start: 1;
    grid-column-end: span 2;
    background-color: #fff;
    padding: 2px;
    box-sizing: border-box;
}
.ranodm-quest {
    grid-row-start: 1;
    grid-row-end: span 2;
    background-color: #202342;
}
.game-chat {
    background-color: #202342;
}
.game-main-button {
    background-color: #202342;
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 40px;
    font-weight: 800;
    cursor: pointer;
}
.user-bar-progress {
    background-color: #000;
    height: 100%;
    width: 40%;
}
.item {
    background-color: #202342;
    height: 100%;
    width: 100%;
}
.bgn {
    background-color: rgba(255, 255, 128, 0);
}
</style>
