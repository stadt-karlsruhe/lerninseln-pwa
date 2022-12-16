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
        :locations="locations"
        :update="updated"
      ></LeafLet>

      </ion-card-content>

      </ion-card>

    <!--ion-content :fullscreen="true"-->
    <ion-content>
      <div ref="tab2" class="swiping">

      <ion-card>
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

// global event handling
import { inject } from 'vue'

export default defineComponent( {
  name: 'MapView',
  components: {  IonContent, IonCard, IonCardContent, 
  IonPage, LeafLet ,EventList, SingleFilter,
  IonLoading,
  },
  methods : {
    async filter(f){
      console.log("MAP filter",f)
      if (f > 0) {
        this.events = this.eventList.filter(e => e.category_id == f)
        const locString = await this.ds.get("locations") || "[]"
        this.locations = JSON.parse(locString).filter(e => e.Kategorie == f)
        console.log("Filtered:",this.locations)
        //this.emitter.emit("info","filtered")
      }
      else {
        this.events = this.eventList
        const locString = await this.ds.get("locations") || "[]"
        this.locations = JSON.parse(locString)
        console.log("All:",this.locations)
        //this.emitter.emit("info","unfiltered")
      }
      this.updated++
      console.log("map updated",this.updated)
    },
    insertEvents(locs) {
      const events = []//new Array()
      locs.forEach((item,i) => {
          item.id = i + 1
          item.latlng = [item.Lat,item.Lon]
          console.log("URL:",item.URL)
          if (item.Icon == "") item.Icon = "/assets/icon/icon.png"
          //item.iconOptions = {"iconUrl":"https://placekitten.com/50/100","iconSize":[48,48]}
          item.iconOptions = {"iconUrl":item.Icon,"iconSize":[32,32]}
          const event = {"id":item.id,
            "title":item.Titel,
            "url":item.URL,
            "category_id":item.Kategorie,
            "txt":item.Preview,
            "icon":item.Icon
          }
          events.push(event)
        }
      )
      return events
    },
    async rl(){
      console.log("RL")
      let status = true
      this.reload = true // prop to components
      // load data
      //const baseUrl = "http://localhost:9000/getProviders.php"
      const baseUrl = "/getProviders.php"
      try {
          const r = await axios.get(baseUrl,getConfig)
          console.log("Status",r.status)
          if ((r.status == 200) && (r.data) && ((typeof r.data) == "object" ))  { //startsWith("<?"))) {
            console.log("data:",typeof r.data)
            const locations = r.data
            console.log("Locations1:",locations, r.data)

            const events = this.insertEvents(locations)
            console.log("Locations loaded:",locations)
            const dt = new Date()
            const date = dt.toISOString().split("T")[0]
            await this.ds.set("date", date)
            await this.ds.set("locations", JSON.stringify(locations))
            await this.ds.set("events", JSON.stringify(events))
            this.emitter.emit("info","fetched")
          } else {
            console.log("Fetch failed, status: ",r.status)
            this.emitter.emit("info","ferror1")
            status = false
          }

      } catch (e) {
        console.log("Error:",e.message)
        this.emitter.emit("info","ferror2")
        status = false
      }
      // read from storage (always)
      try {
          const locationString = await this.ds.get("locations") || "[]"
          this.locations = JSON.parse(locationString)
          const eventString = await this.ds.get("events") || "[]"
          this.eventList = JSON.parse(eventString)
          this.events = this.eventList
          status = true
          console.log("Loaded from store",this.locations,this.events)
      } catch (e) {
        console.log("Loading from store failed:",e.message)
      }

      this.reload = false // prop to components
      this.updated++
      return status
    },
    onSwipe(detail) {
      const type = detail.type;
      const cx = detail.currentX;
      const dx = detail.deltaX;
      const vx = detail.velocityX;
      //console.log(type,cx,dx,vx)
      if ((type == "pan") && (dx > 100) && (vx > 1)) router.push("/intro")
    },
    onRefresh(detail) {
      const dy = detail.deltaY;
      const vy = detail.velocityY;
      //console.log(dy,vy)
      if ((dy > 50) && (vy > 1)) {
        this.emitter.emit("showFetching")
        this.rl()
      }
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
      if (this.resetStorage) {
        alert("Storeage cleared")
        await this.ds.clear()
      }
      await this.ds.set("loadDate",date)
    } catch (e) {
        console.log("Store failed:",e.message)
    }

    const status = await this.rl()

    console.log("Loading complete")
    this.loading = ! status //false
    
  },
  async mounted(){
    // set emitter target for refresh
    this.emitter.on("refresh",e => {
      //alert("refresh")
      this.rl()
      }) 

    const gest = this.$refs.tab2 //ref();
    console.log("gest ",gest)
    const r = router.currentRoute.value.path // value is important!
    //console.log("Current: ",r,"ref2:",gest)
    //setTimeout(function(){console.log(r.path)},2000)
    const swipeGesture = createGesture({
      onMove: (detail) => { this.onSwipe(detail);},
      gestureName: 'swipe',
      direction:"x",
      el: gest,
    })
    swipeGesture.enable();

    const refreshGesture = createGesture({
      onMove: (detail) => { this.onRefresh(detail);},
      gestureName: 'refresh',
      direction:"y",
      el: gest,
    })
    refreshGesture.enable();

  },
  inject: {
    emitter: {
      from: 'emitter'
    }
  },
  watch: {
    '$route' (to, from) {
      //console.log('Rout update2',to,from);
      if (to.path == "/map") {
        console.log('Now on map view');
        this.emitter.emit("map",true)
      } else {
        console.log('Leaving map view');
        this.emitter.emit("map",false)
      }
    },
  },
  setup() {
    const events = ref([])
    const eventList = ref([])
    const reload = ref(0);
    const updated = ref(0);
    const loading = ref(true);
    const resetStorage = ref(false); // option to clear previous data
    const ds = ref(Storage.prototype)
    return { ds, loading, reload, updated, resetStorage, eventList, events,  };
  },
})
</script>

<style scoped>
.map {
  margin-bottom:0;
}



</style>
