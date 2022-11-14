<template>
  <ion-app>
    <ion-router-outlet/>
  </ion-app>
</template>

<script lang="ts">
import { IonApp, IonRouterOutlet } from '@ionic/vue';
import { defineComponent, ref } from 'vue';

// global event handling
import mitt, { Emitter }  from 'mitt'
import { provide } from 'vue'

type Events = {
  info: string,
  refresh: null
}
/*
const showInfo = function(i:string){
  console.log("App info:",i)
  alert("App Info " + i)
}
*/

export default defineComponent({
  name: 'App',
  components: {
    IonApp,
    IonRouterOutlet
  },
  // ---------------------
  // add stuff for pwa installation
  setup() {
    const emitter: Emitter<Events> = mitt<Events>()
    //emitter.on("info", e => showInfo(e))
    provide("emitter",emitter)

    const deferredPrompt:any = ref(null)
    return {deferredPrompt}
  },
  created() {
    window.addEventListener("beforeinstallprompt", e => {
      e.preventDefault();
      // Stash the event so it can be triggered later.
      this.deferredPrompt = e;
      console.log("before install")
      alert("before install")
    });window.addEventListener("appinstalled", () => {
      this.deferredPrompt = null;
      console.log("after install")
      alert("after install")
    });
  }, 
  // ---------------------
});
</script>
<style>
/*
https://ionicframework.com/docs/theming/themes
*/
/*
KA Colors:
#048500   green 4,133,0   hsv: 118,100,52    shade:#037300;, tint: #05aa00
#f7f9f5   light green 247,249,245  hsv: 90,2,98
#404040   gray 
#000000   black 64,64,64

shadows
Big
0px 16px 14px rgba(0,0,0,.2)
umgedreht: 0px -16px 14px
Small
0px 3px 6px rgba(0,0,0,.16)
umgedreht: 0px -3px 6px

*/


:root {
  --ion-background-color:#f7f9f5;
  --ion-text-color: #404040; /* so far, affects only toolbar header */
  --ion-card-color: #404040;
  /*--ion-item-color: #f0f000; */
  --color: #404040;
  --ion-font-family:roboto,sans-serif;
  --ion-tab-bar-color:#404040;  /* default color for icon and label */
  --ion-tab-bar-color-selected:#048500; /* selected  color for icon and label */

}


.ion-page {
  max-width:960px;
  margin-left:auto;
  margin-right:auto;
}

/* global defs */
ion-content {
  /*
    --background: url('/assets/img/bg/backIcons_white.png');
    --background-repeat: repeat;
    */
    --background: #05aa00;
}

</style>
