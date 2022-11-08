<template>
  <ion-page>
    <!--
    <ion-header>
      <ion-toolbar>
        <ion-title>Map
        <img alt="logo" height="40" style="vertical-align:middle"  src="/assets/img/logo.png" > 
        </ion-title>
      </ion-toolbar>
    </ion-header>
    -->
      <ion-card slot="fixed" class="map">

      <ion-card-content>

      <ion-loading
      :is-open="loading"
      cssClass="loader-class"
      message="Bitte warten..."
      >
      </ion-loading>

      <LeafLet v-if="!loading"
        :reload="reload"
      ></LeafLet>

      </ion-card-content>

      </ion-card>

    <!--ion-content :fullscreen="true"-->
    <ion-content>
      <div ref="tab2" class="swiping">

      <ion-card >
      <ion-card-content>
        <SingleFilter  v-if="!loading"
          :reload="reload"
          @update="rl"
          @filter="filter"
        />
      </ion-card-content>
      </ion-card >


      <ion-card >
      <ion-card-content>

      <EventList v-if="!loading"
          :reload="reload"
          :events="events"
      ></EventList>
      <!--
      <div v-for="item in events"  :key="item.id" class="listItem">
            {{item.title}}
            <Event 
              :date=item.date 
              :time=item.time 
              :title=item.title 
              :text="item.text" 
              :id=item.id 
              @click="open(item.id)"
              ></Event>
      </div>
      -->
      </ion-card-content>
      </ion-card>

    </div>
    </ion-content>
  </ion-page>
</template>

<script lang="js">
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonCard, IonCardContent } from '@ionic/vue';
import LeafLet from "@/components/LeafLet.vue";
//import Events from '@/components/Events.vue';
import EventList from '@/components/EventList.vue';

import SingleFilter from '@/components/SingleFilter.vue';

import { defineComponent, ref } from 'vue'; 

import { createGesture } from '@ionic/vue';
import router from "../router";


import { IonLoading } from '@ionic/vue';

import axios from 'axios';
const getConfig = { headers: {'access-control-allow-origin': '*'}}

import { Storage } from '@ionic/storage';


export default defineComponent( {
  name: 'MapView',
  components: {  IonContent, IonCard, IonCardContent, 
  IonPage, LeafLet ,EventList, SingleFilter,
  IonLoading,
  },
  methods : {
    filter(f){
      console.log("MAP filter",f)
      if (f > 0) {
        this.events = this.eventList.filter(e => e.category_id == f)
      }
      else {
        this.events = this.eventList
      }
    },
    async rl(){
      console.log("RL")
      this.reload = true // prop to components
      // load data
      //const baseUrl = "https://lerninseln.karlsruhe.de/simpleSrv.php"
      const baseUrl = "https://lerninseln.ok-lab-karlsruhe.de/simpleSrv.php"
      //const baseUrl = "http://localhost:9000/simpleSrv.php"
      const baseGetUrl = baseUrl + "?table=";

      let status = true
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
              console.log(t, " data loaded",result)

              if (t == "event") {
                // filter only future events
                const dt = new Date()
                const date = dt.toISOString().split("T")[0]
                //console.log("date: ",date)
                // filter for new events
                //const events = result.filter(e => e.date >= date)
                const events = result.filter(e => e.date >= "2021-07-01")
                events.forEach(item => {
                    item.icon="https://lerninseln.com/wp-content/uploads/2021/07/cropped-Lerninseln-Logo-Icon-192x192.png"
                    item.txt = "Orte der (digitalen) Teilhabe \
                      Hier finden die Lernenden freies WLAN und ggf. \
                      bei Bedarf und Verfügbarkeit ExpertInnen, \
                      weiterhelfen können."
                  } 
                )
                await this.ds.set(t, JSON.stringify(events))
                this.eventList = events
                this.events = events
              } else {
                await this.ds.set(t, JSON.stringify(result))
              }


            } else {
              console.log("failed")
              status = false
            }

        } catch (e) {
          console.log("Error:",e.message)
          status = false
        }
      }
      this.reload++
      this.reload = false // prop to components
      return status

    },
    onSwipe(detail) {
      const type = detail.type;
      const cx = detail.currentX;
      const dx = detail.deltaX;
      const vx = detail.velocityX;
      //console.log(type,cx,dx,vx)
      if ((type == "pan") && (dx > 100) && (vx > 1)) router.push("/intro")
      if ((type == "pan") && (dx < -100) && (vx < -1)) router.push("/shop")
    }
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
      this.ds.set("loadDate",date)
    } catch (e) {
        console.log("Store failed:",e.message)
    }

    const status = await this.rl()

    console.log("Loading complete")
    this.loading = ! status //false
    
  },
  async mounted(){
    const gest = this.$refs.tab2 //ref();
    const r = router.currentRoute.value.path // value is important!
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
    const events = ref([])
    const eventList = ref([])
    const reload = ref(0);
    const loading = ref(true);
    const ds = ref(Storage.prototype)
    return { ds, loading, reload, eventList, events };
  },
})
</script>

<style scoped>
.map {
  margin-bottom:0;
}



</style>
