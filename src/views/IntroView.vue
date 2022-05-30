<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title >Lerninseln
        <img alt="logo" height="40" style="vertical-align:middle"  src="/assets/img/logo.png" > 
        </ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="true" >
    <div ref="tab1" class="swiping">
    
     <ion-loading
    :is-open="loading"
    cssClass="loader-class"
    message="Bitte warten..."
    >
    </ion-loading>

    <IntroText></IntroText>
    <!--    
    <LoginForm></LoginForm>
    -->

    <!--
    <IntroSlides v-if="!loading" ></IntroSlides>
    -->

    <ProviderList></ProviderList>

    <ImPrint></ImPrint>

    </div>
    </ion-content>
  </ion-page>
</template>

<script lang="js">
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent,  } from '@ionic/vue';

import { IonLoading } from '@ionic/vue';

import { defineComponent, ref } from 'vue'; 

//import ExploreContainer from '@/components/ExploreContainer.vue';
//import LoginForm from '@/components/LoginForm.vue';
import IntroText from '@/components/IntroText.vue';
import IntroSlides from '@/components/IntroSlides.vue';
import ProviderList from '@/components/ProviderList.vue';
import ImPrint from '@/components/ImPrint.vue';

import { Storage } from '@ionic/storage';

import { createGesture } from '@ionic/vue';
import router from "../router";

import axios from 'axios';
const getConfig = { headers: {'access-control-allow-origin': '*'}}


export default  defineComponent ({
  name: 'IntroView',
  components: { //LoginForm, 
    IntroText, ProviderList, IonHeader, IonToolbar, IonTitle, 
    IonContent, IonPage, ImPrint, //IntroSlides,
    IonLoading
  },
  data: function() {
    return {
    } 
  },
  methods : {
    onSwipe(detail) {
      const type = detail.type;
      const cx = detail.currentX;
      const dx = detail.deltaX;
      const vx = detail.velocityX;
      //console.log(type,cx,dx,vx)
      //if ((type == "pan") && (dx > 100) && (vx > 1)) router.push("/tabs/tab3")
      if ((type == "pan") && (dx < -100) && (vx < -1)) router.push("/map")
    },
  },
  async beforeMount() {
    const dt = new Date()
    const date = dt.toISOString().split("T")[0]
    const tm = dt.toLocaleTimeString('de-DE')
    const time = tm.split(":")[0] + ":" + tm.split(":")[1]
    console.log("date: ",date, time)

    try {
      const store = new Storage();
      await store.create();
      this.ds = store
    } catch (e) {
        console.log("Store failed:",e.message)
    }


    this.loading = true
    // load data
    //const baseUrl = "https://lerninseln.karlsruhe.de/simpleSrv.php"
    const baseUrl = "https://lerninseln.ok-lab-karlsruhe.de/simpleSrv.php"
    //const baseUrl = "http://localhost:9000/simpleSrv.php"
    const baseGetUrl = baseUrl + "?table=";

    const tables = ["config","provider","event","ticket","feature","category","audience"]
    for (const ti in tables) {
      const t = tables[ti]
      console.log("Get data for table ",t);
      const url = baseGetUrl + t
      try {
          const r = await axios.get(url,getConfig)
          console.log("Status",r.status)
          if (r.status == 200) {
            const result = await r.data.data
            console.log("Data loaded",result)

            if (t == "event") {
              // filter only future events
              const dt = new Date()
              const date = dt.toISOString().split("T")[0]
              //console.log("date: ",date)
              // filter for new events
              //const events = result.filter(e => e.date >= date)
              const events = result.filter(e => e.date >= "2021-07-01")
              await this.ds.set(t, JSON.stringify(events))
            } else {
              await this.ds.set(t, JSON.stringify(result))
            }


        } else {
            console.log("failed")
        }
      } catch (e) {
        console.log("Error:",e.message)
        return
      }
    }

    console.log("Loading complete")
    this.loading = false
  },
  async mounted(){
    const gest = this.$refs.tab1 //ref();
    // const r = router.currentRoute.value.path // value is important!
    //console.log("Current: ",r,"ref2:",gest)
    //setTimeout(function(){console.log(r.path)},2000)
    const gesture = createGesture({
      onMove: (detail) => { this.onSwipe(detail);},
      gestureName: 'swipe',
      el: gest,
    })
    gesture.enable();
  },
  setup() {
    const loading = ref(true);
    const df = ref(null)
    const ds = ref(null)
    return { df, loading };
  }
})

</script>


<style scoped>

ion-toolbar {
  /* https://ionicframework.com/docs/api/toolbar */
  /* background color from app.vue */
  --border-color:#048500;
  --border-width:3px;
  --border-style:solid none none none;
}

/* https://stackoverflow.com/questions/54956372/how-to-change-the-toolbar-color-in-ionic-4 

*/

.loader-class {

}

/* can overwrite here ... **
ion-content {
    --background: url('/assets/img/bg/backIcons_white.png');
    --background-repeat: repeat;
}
*/

/*
.ion-page {
  max-width:960px;
  margin-left:auto;
  margin-right:auto;
}
*/
.swiping {
  min-height:90%;
}

</style>
