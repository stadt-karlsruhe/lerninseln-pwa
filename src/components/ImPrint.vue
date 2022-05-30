<template>
    <ion-card>
    <ion-card-content class="center">
        <div>
          <ion-button  :href="imprintUrl" target="_blank">
            <ion-icon :icon="informationCircleOutline" alt="Impressum"/>
          <ion-label>Impressum</ion-label>
          </ion-button>
          <ion-button  :href="gdprUrl" target="_blank">
            <ion-icon :icon="shieldHalfOutline" alt="Datenschutz"/>
          <ion-label>Datenschutz</ion-label>
          </ion-button>
          <ion-button  :href="gitUrl" target="_blank">
            <ion-icon :icon="logoGithub" alt="Github"/>
          <ion-label>Quellcode</ion-label>
          </ion-button>
        </div>

    </ion-card-content>
  </ion-card>

</template>

<script lang="ts">
import {IonCard, IonCardContent, IonButton, IonIcon, IonLabel } from '@ionic/vue';
import { defineComponent } from 'vue';


import { 
  informationCircleOutline,
  shieldHalfOutline,
  logoGithub,
 } from 'ionicons/icons';


export default defineComponent ({
  name: "ImPrint",
  components: { IonCard, IonCardContent, IonLabel, 
     IonButton, IonIcon
  },
  methods: {
  },
  setup() {
    return {
      informationCircleOutline,shieldHalfOutline,logoGithub,
      gdprUrl:"https://www.karlsruhe.de/impressum/datenschutz.de",
      imprintUrl: "https://www.karlsruhe.de/impressum.de",
      gitUrl: "https://github.com/digital-codes/lerninseln",
    }
  },

});
</script>

<style scoped>

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

.center {
  text-align: center;

}
</style>
