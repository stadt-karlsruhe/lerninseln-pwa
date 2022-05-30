<template>
    <ion-card>
    <ion-card-header>
    <ion-card-subtitle>Filter
    </ion-card-subtitle>
    </ion-card-header>
    <ion-card-content>

    <ion-grid>
      <ion-row>
        <ion-col size="10">
            <FilterItem v-for="n in 4" :key="n" 
              :name=labels[n-1]
              :icon=icons[n-1]
              :check=check[n-1]
              :info=infos[n-1]
              @filter="onFilter(n-1,$event)"
            />
        </ion-col>
        <ion-col size="2">
              <ion-spinner v-show="isLoading" class="spinner" ></ion-spinner>
              <ion-icon v-show="!isLoading" :icon="syncOutline" class="syncIcon" @click="sync"/>
        </ion-col>
      </ion-row>
    </ion-grid>

    </ion-card-content>
  </ion-card>

</template>

<script lang="ts">
import {IonCard, IonCardContent, IonCardHeader,IonCardSubtitle,
      IonGrid, IonRow, IonCol, IonSpinner } from '@ionic/vue';
import { defineComponent, ref } from 'vue';

import FilterItem from '@/components/FilterItem.vue';

// storage 
import { Storage } from '@ionic/storage';


import { 
  volumeMuteOutline,
  //wifiOutline,
  medkitOutline,
  constructOutline,
  peopleOutline,
  syncOutline,
 } from 'ionicons/icons';

const icons=[ volumeMuteOutline,
  //wifiOutline,
  medkitOutline,
  constructOutline,
  peopleOutline]

const labels = ["F1","F2","F3","F4"]
const infos = [
  "Ruhe","Unterstützung","Werkstatt","Gemeinschaft"
  ]

export default defineComponent ({
  name: "SingleFilter",
  components: { IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, 
  FilterItem,
  IonGrid, IonRow, IonCol,
  IonSpinner,
  },
  data () {
    return {
      check: [false,false,false,false],
      update: 0,
      icons: icons,
      labels: labels,
      filterOff: true,
      infos: infos,
      isLoading: false
    }
  },
  methods: {
    async sync() {
      console.log("Sync")
      this.isLoading = true
      setTimeout(()=>{this.isLoading=false},2000)
    },
    async onFilter(x: number, y: boolean) {
        console.log("On Filter")
        try {
          var filter = await this.ds.get("filterCatId") || 0
        } catch (e: any) {
          console.log("SF - read store failed:",e.message)
          // this is only when we start with the map ...
          try {
            const store = new Storage();
            await store.create();
            this.ds = store
            console.log("New SF store:",store)
          } catch (e: any) {
              console.log("SF - Store failed:",e.message)
          }

        }
        console.log("Filter event: ",x,y,filter)
        //"Store filter: ",this.store.state.filter.catId)
        if (y) {
          for (let i=0;i<this.check.length;i++){
            this.check[i] = (i == x)
            console.log("Check on:",x)
          }
          filter = x + 1 // categories run from 1
          await this.ds.set("filterCatId",filter)
        } else {
          if (this.check[x]) {
            filter = 0
            console.log("Check off:",x)
            await this.ds.set("filterCatId",filter)
          }
        }
        //console.log(this.check)
    },
    async beforeMount() {
      try {
        const store = new Storage();
        await store.create();
        this.ds = store
        console.log("SF store:",store)
      } catch (e: any) {
          console.log("SF - Store failed:",e.message)
      }
    }
  },
  setup() {
    const ds = ref(Storage.prototype)
    return {
      ds,
      volumeMuteOutline,
      //wifiOutline,
      medkitOutline,
      constructOutline,
      peopleOutline,
      syncOutline,
    }
  },

});
</script>

<style scoped>

.hdr {
  color: unset;  
}


ion-card {
  margin: 0;
}

ion-card-content {
  padding: 0;
  text-align: center;
}


ion-card-header {
  padding: 0;
}

ion-card-subtitle {
  text-align:center;
}

ion-card-content {
  line-height: 1.2em;
}

ion-card-content .card-content-ios {
  padding-inline-start: 5px;
  padding-inline-end: 5px;
  padding-top: 5px;
  padding-bottom: 5px;
}


.label {

}

.inactive {
  --background: #50c8ff;
}

.syncIcon {
  width: 80%;
  height: 80%;
  /*
  background: #fff;
  border-bottom: solid 4px #5260ff; 
  */
}

.spinner {
  width: 80%;
  height: 80%;
}

</style>
