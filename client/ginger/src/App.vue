<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav>
  <router-view/>
</template>

<script>
export default {
	created(){
    // const http = require("http")
    // const io = require("socket.io")
    const io = require('socket.io-client')
    this.conn = io.connect('http://localhost:8080');
    // console.log(socket)

    this.conn.on('hui', (e) => {
                console.log(e)
            })

    this.conn.on("connect", () => {
      console.log('conn is connected')
      this.conn.emit('my_event', {data: 'I\'m connected!'});
    })

    this.conn.on("sqware", (msg) => {
      console.log(msg)
      
    })

    this.conn.on("message", (msg) => {
      console.log(msg)
    })

    this.conn.emit("template")
    // socket.on('pong',function(){
    //   console.log('session is alive')
    // })
    // this.conn = new WebSocket("ws://127.0.0.1:5000/shared")
    // console.log(this.conn)

    // this.conn.onopen = function(event) {
    //   console.log(event)
    //   console.log("Succes")
    // }

    // this.conn.onmessage = function(event){
    //   console.log(event)
    // }

  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

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
</style>
