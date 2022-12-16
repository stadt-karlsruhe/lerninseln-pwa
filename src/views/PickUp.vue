<template>
  <ion-page>
    <ion-tabs>
      <ion-router-outlet></ion-router-outlet>
      <ion-tab-bar slot="bottom" class="ka-tabs">

        <ion-tab-button tab="intro" href="/intro" class="ka-tab-btn">
          <ion-icon :icon="homeOutline" />
          <ion-label>Intro</ion-label>
        </ion-tab-button>
          
        <ion-tab-button tab="map" href="/map" class="ka-tab-btn">
          <ion-icon :icon="albumsOutline" />
          <ion-label>Angebote</ion-label>
        </ion-tab-button>

        <ion-tab-button v-if="enableRefresh" class="ka-tab-btn" @click="refresh">
          <ion-spinner v-if="refreshing" name="lines-small"></ion-spinner>
          <ion-icon v-else :icon="refreshOutline" />
          <ion-label>Refresh</ion-label>
        </ion-tab-button>

        <!--
        <ion-tab-button class="ka-tab-btn" >
          <ion-label>{{ pwaStat }} </ion-label>
        </ion-tab-button>
        -->

        <!--
        <ion-item>
          <ion-checkbox v-model="tglState" slot="start" @ionChange="toggle"></ion-checkbox>
        </ion-item>

        -->

      </ion-tab-bar>
    </ion-tabs>
  </ion-page>
</template>

<script >
import { IonRouterOutlet, IonTabBar, IonTabButton, IonTabs, IonLabel, IonIcon, IonPage } from '@ionic/vue';
import { IonSpinner } from '@ionic/vue';
import { ref } from "vue"

//import { IonCheckbox } from '@ionic/vue';


import { refreshOutline } from 'ionicons/icons';


import { 
  homeOutline, 
  albumsOutline,
  mapOutline,
  calendarNumberOutline,
  cartOutline,
  qrCodeOutline,
 } from 'ionicons/icons';

// global event handling
import { inject } from 'vue'


export default {
  name: 'PickUp',
  components: { 
    IonLabel, IonRouterOutlet, IonTabs, IonTabBar, IonTabButton, IonIcon, IonPage,
    IonSpinner,
    //IonCheckbox,
  },
  watch: {
    '$route' (to, from) {
      if (to.path == "/intro") {
        //console.log('P: Now on intro');
        this.enableRefresh = false
      }
      if (to.path == "/map") {
        //console.log('P: Now on map');
        this.enableRefresh = true
      }
    }
  },
  methods: {
    refreshCompleted() {
      this.refreshing = false
    },
    async refresh() {
      //alert("refresh")
      this.refreshing = true
      this.pwaStat = "refreshing"
      this.emitter.emit("refresh")
      // reset after status update
      // setTimeout(this.refreshCompleted,2000)
    },
    statUpdate(stat) {
      //this.refreshing = false
      // allow some spinning time
      setTimeout(this.refreshCompleted,1000)
      this.pwaStat = stat
    },
    tabUpdate(stat) {
      console.log("Map:",stat)
      this.onMap = stat
    },
    toggle(){
      console.log("toggle changed to:",this.tglState) 
      //this.checkToggle(!ev.checked)
      this.checkToggle(this.tglState)
    },
    checkToggle(shouldCheck) {
      console.log("check:",shouldCheck)
      if (shouldCheck)
        document.body.classList.toggle('dark', true);
      else
        document.body.classList.toggle('dark', false);
      //this.toggle.checked = shouldCheck;
    },
  },
  inject: {
    emitter: {
      from: 'emitter'
    }
  },
  mounted(){
    // set emitter target
    this.emitter.on("info",e => this.statUpdate(e)) 
    this.emitter.on("showFetching",e => {
      this.refreshing = true
      this.statUpdate("Refresh")
    } )

    // enable refresh if on map, initially
    if (this.$route.path == "/map") {
      this.enableRefresh = true
    }
  },
  setup() {
    const enableRefresh = ref(false)
    const tglState = ref(0)
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');
    const refreshing = ref(false)
    const pwaStat = ref("Ready")
    const onMap = ref(false)
    return {
      onMap,
      homeOutline, 
      albumsOutline,
      mapOutline,
      calendarNumberOutline,
      cartOutline,
      qrCodeOutline,
      refreshing,
      refreshOutline,
      pwaStat,
      prefersDark,
      tglState,
      enableRefresh, 
    }
  }
}
</script>

<style scoped>


/* tab button color from app.vue */
.ka-tabs {
  background-color: #048500;
}

.ka-tab-btn {
  /* default bg
  background-color:#f7f9f5;
  */
  /*
  margin-left:2px;
  margin-right:2px;
  */
  border-left: solid 2px #404040;
  border-right: solid 2px #404040;

}


/* see https://ionic.io/ionicons/usage */
ion-icon {
  --ionicon-stroke-width: 48px;
}

ion-label {
  font-size:1em;
}


</style>