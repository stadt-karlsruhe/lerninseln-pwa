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
        
       
      </ion-tab-bar>
    </ion-tabs>
  </ion-page>
</template>

<script >
import { IonRouterOutlet, IonTabBar, IonTabButton, IonTabs, IonLabel, IonIcon, IonPage } from '@ionic/vue';
import { 
  homeOutline, 
  albumsOutline,
  mapOutline,
  calendarNumberOutline,
  cartOutline,
  qrCodeOutline,
 } from 'ionicons/icons';

export default {
  name: 'PickUp',
  components: { IonLabel, IonRouterOutlet, IonTabs, IonTabBar, IonTabButton, IonIcon, IonPage },
  setup() {
    return {
      homeOutline, 
      albumsOutline,
      mapOutline,
      calendarNumberOutline,
      cartOutline,
      qrCodeOutline,
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