<template>
  <!-- Default Refresher -->
  <ion-content>
    <ion-refresher slot="fixed" @ionRefresh="doRefresh($event)">
      <ion-refresher-content></ion-refresher-content>
    </ion-refresher>
  </ion-content>

  <!-- Custom Refresher Properties -->
  <ion-content>
    <ion-refresher slot="fixed" pull-factor="0.5" pull-min="100" pull-max="200">
      <ion-refresher-content></ion-refresher-content>
    </ion-refresher>
  </ion-content>

  <!-- Custom Refresher Content -->
  <ion-content>
    <ion-refresher slot="fixed" @ionRefresh="doRefresh($event)">
      <ion-refresher-content
        :pulling-icon="chevronDownCircleOutline"
        pulling-text="Pull to refresh"
        refreshing-spinner="circles"
        refreshing-text="Refreshing...">
      </ion-refresher-content>
    </ion-refresher>
  </ion-content>
</template>

<script lang="js">
import { IonContent, IonRefresher, IonRefresherContent } from '@ionic/vue';
import { chevronDownCircleOutline } from 'ionicons/icons'
import { defineComponent } from 'vue';



export default defineComponent({
  components: { IonContent, IonRefresher, IonRefresherContent },
  methods: {
    completed() {
      console.log("Completed")
    },
  },
  setup() {
      const action = function(e) {
        console.log("Action:",e)
      }
      // not ok with typescript: event.target.complete not exisiting
      //const doRefresh = (event: CustomEvent) => {
      const doRefresh = (event) => {
      console.log('Begin async operation');
      action(event.target)
      setTimeout(() => {
        console.log('Async operation has ended');
        //this.completed()
        event.target.complete();
      }, 2000);

    }
    return { chevronDownCircleOutline, doRefresh }
  }
});
</script>
