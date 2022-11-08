<template>

  <ion-card ion-fixed>
    <ion-card-header >
      <ion-card-title class="hdr">Anbieter</ion-card-title>
      <!--
      <ion-card-subtitle class="hdr">Kategorien </ion-card-subtitle>
      -->
    </ion-card-header>

    <ion-card-content>
      Die beteiligten Anbieter stellen ganz verschiedene Möglichkeiten zur 
      Verfügung, auch in ganz unterschiedlichen Umgebungen. 
      <br>
      Wir haben alle Angebote mit Eigenschaften versehen, nach denen Ihr filtern könnt. 
      Manche Angebote passen natürlich auf mehrere Eigenschaften.
    <ul class="list">
      <li v-for="item in items"  :key="item.id" class="listItem">
            <ion-icon class="icon" :icon="item.icon" :alt="item.alt"/>
            <h2>{{item.hdr}}</h2>
            <p>{{item.text}}</p>
      </li>
    </ul>
    Auf der nächsten Seite könnt Ihr in allen Angebote stöbern. 
            <ion-button @click="toMap()" class="ka-tab-btn">
              <ion-icon :icon="albumsOutline" />
              <ion-label>Los!</ion-label>
        </ion-button>

    </ion-card-content>

  </ion-card>


</template>


<!-- check https://forum.ionicframework.com/t/css-position-fixed/2969/4 -->

<script> 

import { defineComponent } from 'vue'; 

import { IonCard, IonCardContent, IonCardHeader,
IonIcon, IonLabel, IonButton,
//IonCardSubtitle, 
IonCardTitle, } from '@ionic/vue';

import { 
  volumeMuteOutline,
  medkitOutline,
  constructOutline,
  peopleOutline,
  syncOutline,
  albumsOutline,
  telescopeOutline,
  wifiOutline,
  desktopOutline,
  contractOutline,
  trophyOutline,
  rocketOutline,
 } from 'ionicons/icons';

import router from "../router";

export default defineComponent({
  // ----------------------
  components: {  IonCard, IonCardContent, IonCardTitle, IonCardHeader, 
  IonIcon, IonLabel, IonButton,
  //IonCardSubtitle, 
  },
  setup() {
    return {   
      volumeMuteOutline,
      medkitOutline,
      constructOutline,
      peopleOutline,
      albumsOutline,
      telescopeOutline,
      wifiOutline,
      desktopOutline,
      contractOutline,
      trophyOutline,
      rocketOutline,
    }
  },

  // ---------------------
  data: function() {
    return {
      items: [{
      'hdr': 'Digitale Teilhabe',
      'text': 'Hier finden die Lernenden freies WLAN und ggf. bei Bedarf und Verfügbarkeit ExpertInnen, z.B. Studierende der Pädagogischen Hochschule in Karlsruhe, die den Lernenden bei technischen, aber auch fachlichen Fragen weiterhelfen.' ,
      "id":1,
      "alt":"alt",
      "icon":this.desktopOutline,
    }, 
    { "hdr":"MINT-Spaces",
      "text": "Sie beinhalten zahlreiche Karlsruher Initiativen und Aktivitäten, die im Rahmen von AGs an Schulen, aber auch außerhalb der Schulen stattfinden.",
      "id":2,
      "alt":"alt",
      "icon":this.constructOutline,
    },
    {
      'hdr': 'Digitale Dritte Orte',
      'text': 'An diesen Orten kann offen und partizipativ, auch in Gruppen, gelernt werden. Eigene Initiativen sind möglich.',
      "id":3,
      "alt":"alt",
      "icon":this.peopleOutline,
    },
    {
      'hdr': 'Beteiligungsorte + MINT-Ausstellungsräume',
      'text': 'Orte, an denen Einzelaktionen (Hackathons, Kunstaktionen, Fischertechnik-Challenges usw.) stattfinden.',
      "id":4,
      "alt":"alt",
      "icon":this.rocketOutline,
    }, 
    {
      'hdr': 'Wissensräume',
      'text': 'Orte an denen IT- und MINT-Wissenstransfers stattfinden oder an denen sich Role Models vorstellen.',
      "id":5,
      "alt":"alt",
      "icon":this.telescopeOutline,
    },
    ],
    }
  },
  methods:{
    zoom(e) {
      console.log(e)
    },
    toMap(){
      router.push("/map")
    },

  }
}); 
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

.event {
  text-align: left;
  white-space: normal;
}
.eventDate {
  text-align: left;
  /* with position: fixed adjust size */
  flex-basis: 150px;
}

.footer {
  height: 1rem;
  background-color: primary;

}

.hdr {
  --color: --ka-text-color;  
}

.icon {
  width:3rem;
  height:2rem;
}

</style>

