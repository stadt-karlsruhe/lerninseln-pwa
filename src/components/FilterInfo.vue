<template>
  <ion-content class="ion-padding">
    <span class="filterInfo">{{info}}</span>
  </ion-content>
</template>

<script>
import { IonContent } from '@ionic/vue';
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'FilterInfo',
  props: ["info"],
  components: { IonContent }
});
</script>

<style scoped>

.filterInfo {
    color: #fff;
}


</style>
