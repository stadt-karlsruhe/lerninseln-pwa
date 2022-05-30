<template>
    <ion-card>
    <ion-card-header>
      <ion-card-title class="hdr">Lerninseln Karlsruhe</ion-card-title>
      <ion-card-subtitle class="fake">Dies ist nur ein Prototyp!!!</ion-card-subtitle>
    </ion-card-header>

    <ion-card-content>
      Lerninseln sind schulische und außerschulische Orte im Stadtgebiet Karlsruhe, 
      an denen junge Menschen in Eigeninitiative oder mit Betreuung lernen können. 
      Die Lerninseln ermöglichen allen Kindern und Jugendlichen jeder 
      Schulform sowie Studierenden, auch unabhängig von Unterrichts- und Lehrbetrieb, 
      unter besten Voraussetzungen zu lernen, allein oder in einer Gemeinschaft 
      zu arbeiten und eigenen Interessen vertieft nachzugehen. 
      <br>
      Eine Lerninsel kann ein Arbeitsplatz mit Computer und Internetanschluss sein. 
      Sie kann ein Raum sein, in dem Gruppen arbeiten können. 
      Zudem kann eine Lerninsel pädagogische Unterstützung anbieten.
      <br>

      Die Stadt Karlsruhe sammelt geeignete Angebote und stellt mit 
      einer interaktiven Karte einen Rahmen bereit, 
      in dem diese übersichtlich dargestellt und unkompliziert gebucht werden können.
      <br>

      Die einzelnen Angebote finden in den Räumen und unter der Verantwortung 
      der jeweiligen Anbieter statt.

        <ion-img class="intro-image" src="/assets/img/front/1.jpg"></ion-img>


        <div>
          <div>
          <ion-button  :href="moreUrl" target="_blank">
            <ion-icon icon="/assets/icon/li-icon.svg" alt="Impressum"/>
          <ion-label>Mehr Infos</ion-label>
          </ion-button>
          <ion-button  href="mailto:lerninseln@ok-lab-karlsruhe.de">
            <ion-icon :icon="mailOutline" />
          <ion-label>Schreib uns</ion-label>
          </ion-button>
          </div>
        </div>

    </ion-card-content>
  </ion-card>


</template>

<script lang="ts">
import {IonCard, IonCardContent, IonCardHeader, IonCardTitle, IonButton, 
IonIcon, IonImg, IonLabel,
IonCardSubtitle,
 } from '@ionic/vue';
import { defineComponent } from 'vue';



import { 
  shareSocialOutline,
  mailOutline,
 } from 'ionicons/icons';


export default defineComponent ({
  name: "IntroText",
  components: { IonCard, IonCardContent, IonCardHeader, IonCardTitle,  
     IonButton, IonIcon, IonImg, IonLabel,
     IonCardSubtitle,
  },
  setup() {
    const moreUrl = "https://lerninseln.com"
    return {
      moreUrl,
      mailOutline,shareSocialOutline,
    }
  },

});
</script>

<style scoped>
#container {
  text-align: center;
}

#container strong {
  font-size: 20px;
  line-height: 26px;
}

#container p {
  font-size: 16px;
  line-height: 22px;
  color: #8c8c8c;
  margin: 0;
}

#container a {
  text-decoration: none;
}

.extLink {
  text-align: left;
  /* with position: fixed adjust size */
  display: block;
  text-decoration-line: underline;
  text-decoration-color: #048500; 
  color: #048500;
}

.extLink:hover {
    cursor:pointer;
}

.hdr {
  color: unset;  
}

.intro-image {
  padding-top: 1.5rem;
  padding-bottom: 1.5rem;
}

.fake {
  color: #f00;
  font-size: 150%;
}
</style>
