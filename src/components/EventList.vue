<template>

  <div>
  <ion-button 
    v-if="hasEvent" 
    @click="buy()"
    >Zur Buchung
  </ion-button>
  <div class="navigate" v-if="hasEvent">
  <ion-button
    :href=osmUrl
    target="_blank"
    >Hinkommen
  </ion-button>
  </div>

  </div>
  <div v-for="item in selIitems"  :key="item.id" class="listItem">
          <SingleEvent class="eventItem" 
          :date=item.date 
          :time=item.time 
          :title=item.title 
          :text=item.provider 
          :id=item.id  
          :icon=item.category_id
          :url=item.url 
          ></SingleEvent>

          <ion-checkbox class="eventCheck" 
            @ionChange="select(item.id)"
            @update:modelValue="item.checked = $event"
            :modelValue="item.checked"
          ></ion-checkbox>


          <ion-item>
            <ion-thumbnail 
              slot="start">
              <img :src="item.icon"/>
            </ion-thumbnail>
            <ion-text class="previewText">
            {{item.txt}}
            </ion-text>
          </ion-item>

  </div>


</template>

<script> 

import { 
  cartOutline,
 } from 'ionicons/icons';

import { IonButton, IonCheckbox,IonThumbnail, IonText, IonItem, } from '@ionic/vue';

// storage 
import { Storage } from '@ionic/storage';

import { defineComponent, ref } from 'vue'; 
import SingleEvent from '@/components/SingleEvent.vue';

import router from "../router";

const dummyText = [
  "GloW Karlsruhe e.V. - au\u00dferschulischer Lernort, mit Workshops aus der Bildung f\u00fcr nachhaltige Entwicklung (BNE), vor allem Globales Lernen.",
  "Wir sind f\u00fcr Sie da: Wir bieten Dienstleistungen im sozialen, p\u00e4dagogischen und pflegerischen Bereich in Stadt- und Landkreis Karlsruhe.",
  "ROCK YOUR LIFE! ist ein Netzwerk aus ehrenamtlich engagierten Studierenden in 52 Vereinen, motivierten Sch\u00fcler*innen, verantwortungsvollen Unternehmen."
]

export default defineComponent({
  name: "EventList",
  components: {SingleEvent, IonButton, IonCheckbox, IonThumbnail, IonText, IonItem,},
  data () {
    return {
    items : [],
    providers: [],
    osmUrl: ""
    /*
    chk1: 1, 
    chk2: 0, 
    chk3: 1,
    */ 
    }
  },
  methods:{
    buy() {
      router.push("/shop")
    },
    async select(e) {
      const item = this.items.find(i => (i.id == e))
      // for button:
      /*
      if (item.checked != true) 
        item.checked = true
      else
        item.checked = false
      */
      console.log("Checked: ",item.id, item.checked)
      if (item.checked) {
        //this.filter = item.id
        const dest = JSON.parse((this.providers.find(p => p.id == item.provider_id)).latlon)
        const src = this.ds.get("position")
        console.log("Pos: ",src.lat,src.lon,dest.lat,dest.lon)
        // example https://routing.openstreetmap.de/?z=16&center=48.992228%2C8.391194&loc=48.992228%2C8.391194&loc=48.996931%2C8.387783&hl=de&alt=0&srv=2
        //         https://routing.openstreetmap.de/?z=16&center=48.998874%2C8.477733&loc=48.998867%2C8.477738&hl=en&alt=0&srv=2
        const osmBaseUrl = "https://routing.openstreetmap.de/"
        this.osmUrl = osmBaseUrl + "?z=12&center=" + 
          src.lat + "%2C" + src.lon + 
          "&loc=" + src.lat + "%2C" + src.lon +
          "&loc=" + dest.lat + "%2C" + dest.lon +
          "&hl=de&alt=0&srv=2"


      } else {
        //this.filter = 0;
        this.osmUrl = "/map"
      }
    },
  },
  async beforeMount() {
    try {
      const store = new Storage();
      await store.create();
      this.ds = store
      console.log("LL store:",store)
    } catch (e) {
        console.log("Store failed:",e.message)
        return
    }

    const providerString = await this.ds.get("provider") || "[]"
    // we need providers later on
    this.providers = JSON.parse(providerString)
    const ticketString = await this.ds.get("ticket") || "[]"
    const tickets = JSON.parse(ticketString)
    const itemString = await this.ds.get("event") || "[]"
    const items = JSON.parse(itemString)
    const validItems = []
    for (let i=0; i < items.length; i++){
      // cechk if we have any tickets on this event
      const tick = tickets.find(t => t.event_id == items[i].id) || 0
      console.log("Tick: ",tick)
      if (tick == 0) continue
      const pid = items[i].provider_id
      const name = (this.providers.find(p => p.id == pid)).name
      //console.log("i: ",i,", id: ",id, ", name: ",name)
      items[i].provider = name
      items[i].checked = 0
      validItems.push(items[i])
    }
    this.items = validItems
    this.storeAvail = true

    
    //console.log("befMount: ",items,validItems)
  },
  computed: {
    selIitems() {
      // https://v3.vuejs.org/guide/computed.html#computed-properties
      //console.log("Filter on:", this.filter,"length: ",this.items.length)
      if (!this.storeAvail) return []
      console.log("computed: ",this.items, this.items.length)
      const evtFilter = this.ds.get("selectedEventId")
      const catFilter = this.ds.get("filterCatId")
      //const catFilter = 0 // should get it from store this.store.state.selection.eventId
      console.log("Event filter on:", evtFilter,"length: ",this.items.length)
      console.log("Category filter on:", catFilter)
      const i = []
      if (evtFilter == 0) {
        this.items.forEach(item => { 
          item.checked = 0
          item.icon = "/assets/img/thumbs/" + ((item.id % 3) + 1) + ".png"
          item.txt = dummyText[item.id % 3]
          // filter by category
          if ((catFilter == 0) || (item.category_id == catFilter)) {
            i.push(item)
          } 
        })
      } else {
        const item = this.items.find(x => x.id == evtFilter) || 0
        if (i != 0)
        item.checked = 1
        item.icon = "/assets/img/thumbs/" + ((item.id % 3) + 1) + ".png"
        item.txt = dummyText[item.id % 3]
        i.push(item)
      }
      /*
      this.items.forEach(item => { 
        //console.log(item)
        //if ((this.filter == 0) || (item.category_id == this.filter)) 
        //if ((this.filter == 0) || (item.id == this.filter)) 
        if ((filter == 0) || (item.id == filter)) 
          i.push(item)
        })
        */
      return i
    },
    hasEvent() {
      if (!this.storeAvail) return false
      return (this.ds.get("selectedEeventId") != 0)
    },
  },
    // store
  setup() {
    const storeAvail = ref(false)
    const ds = ref(null)
    return { cartOutline, ds };
  },
}
); 
</script>

<style scoped>


.list {
  list-style: none;
  padding: 0 2% 0 2%;
}

.listItem {
  padding-top: .3rem;
  padding-bottom: 1rem;
  border-bottom: solid 1px;
  border-bottom-color: #444;
}

h2 {
  padding-bottom: .2rem;
}

button {
  margin-top: .5rem;
}

.navigate {
  display: inline-block;
}



.eventItem {
  display: inline-block;
  width:85%;
}

.eventCheck {
  display: inline-block;
  max-width:10%;  
  margin-left:5%;
  margin-bottom: 2em;
  width: 2em;
  height: 2em;
  border: solid 4px #048500;
  border-radius: 5px;
}

input.eventCheck  {
  width:1em;
}

.previewText {
  max-height: 4rem;
  white-space: normal; 
  overflow: hidden;
  /* ellispis only with nowrap which gives only 1 line */
  text-overflow: ellipsis;
}
</style>

